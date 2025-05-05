# Import necessary libraries
import re
import os
import pandas as pd
import datetime
from collections import defaultdict

# Define the start date of the war so we can ignore earlier files
war_start_date = datetime.datetime(2023, 10, 7)

# Define the path to the folder containing article text files
folder = "../articles"

# Define the path to the gazetteer file which contains the place names
gazetteer_path = "../gazetteers/geonames_gaza_selection.tsv"

# Read the gazetteer file (which contains all the place names we want to search for)
with open(gazetteer_path, encoding="utf-8") as file:
    gazetteer_data = file.read()

# Split the file into lines (each line contains one place and its alternate names)
rows = gazetteer_data.strip().split("\n")

# Create a dictionary to store the compiled regex pattern for each place
# The key will be the main place name, and the value will be the compiled regex pattern
patterns = {}

# Loop over each row (skipping the header row)
for row in rows[1:]:
    columns = row.split("\t")
    main_name = columns[0].strip()  # The main place name
    all_names = [main_name]  # Start with the main name
    if len(columns) > 5:
        # If alternate names exist (in column 6), add them to the list
        alternates = [name.strip() for name in columns[5].split(',') if name.strip()]
        all_names.extend(alternates)

    # Create a regex pattern that matches any of the names using word boundaries
    # \b ensures we only match whole words (e.g., 'Gaza' not in 'Magazine')
    # re.escape ensures special characters are treated literally
    pattern = r'\b(?:' + '|'.join(re.escape(name) for name in all_names) + r')\b'

    # Compile the regex with case-insensitive flag to match names like "gaza" or "Gaza"
    patterns[main_name] = re.compile(pattern, flags=re.IGNORECASE)

# Create a dictionary to store the number of mentions per month for each place
# Structure: { "place_name": { "YYYY-MM": count, ... } }
mentions_per_month = defaultdict(lambda: defaultdict(int))

# Loop through all the article text files in the folder
for filename in os.listdir(folder):
    if not filename.endswith(".txt"):
        continue  # Skip non-text files just in case

    # Extract the date part from the filename (e.g., "2023-10-08_article.txt" → "2023-10-08")
    file_date_str = filename.split('_')[0]
    try:
        file_date = datetime.datetime.strptime(file_date_str, "%Y-%m-%d")
    except ValueError:
        continue  # Skip files that don't have a proper date format

    # Skip files before the war start date
    if file_date < war_start_date:
        continue

    # Read the text content of the article
    file_path = os.path.join(folder, filename)
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # Extract the month in format YYYY-MM (e.g., "2023-10")
    month_str = file_date.strftime("%Y-%m")

    # Loop through all place regex patterns and count matches
    for place_name, regex in patterns.items():
        # Find all matches of the regex in the text
        matches = regex.findall(text)
        count = len(matches)  # Number of times the place was mentioned

        # Add the count to the monthly total for that place
        mentions_per_month[place_name][month_str] += count

# Now print out the results, skipping places that were never mentioned
for place_name, months in mentions_per_month.items():
    if all(count == 0 for count in months.values()):
        continue  # Skip places that have zero mentions in all months

    print(f"{place_name}:")
    for month, count in sorted(months.items()):
        if count > 0:
            print(f"  {month}: {count} time(s)")

# Prepare the results to save them in a table format (TSV)
# Define column names
columns = ["placename", "month", "mentions"]
rows = []

# Convert the nested dictionary to a list of rows
for place_name, months in mentions_per_month.items():
    for month, count in months.items():
        if count > 0:
            rows.append([place_name, month, count])

# Create a pandas DataFrame and save it as a .tsv file
df = pd.DataFrame(rows, columns=columns)
df.to_csv("regex_counts.tsv", sep="\t", index=False)

