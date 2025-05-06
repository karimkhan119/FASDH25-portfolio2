# Import the library, reglar expression to search places names
import re
# Import os library to read files 
import os
# Import pandas library for data handling
import pandas as pd

# Define the path to the folder containing article text files
folder = "../articles"

# Define the path to the gazetteer file which contains the place names
gazetteer_path = "../gazetteers/geonames_gaza_selection.tsv"

# Open and read files (which contains all the place names we want to search for)
with open(gazetteer_path, encoding="utf-8") as file:
    data = file.read()

# Split the gazetteer files into rows to process each line individually
rows = data.strip().split("\n")

# Create a dictionary of patterns from place names in the first column and alternative name
# create an empty dictionary to store place_name an their count 
patterns = {}
# split the gazetteer data by a new line to each row
rows = data.split("\n")

# Loop through each row in the gazetteer (excluding the header)
for row in rows[1:]:
    # Split each row by tab to separate the columns of gazetteer 
    columns = row.split("\t")

    # extract the main place names (asciname)
    asciiname = columns[0].strip()  

    # Check if there are alternate names in the 6th column  
    if len(columns) > 5:
        # If alternate names exist (in column 6), add them to the list
        alternatenames = columns[5]
    else:
            alternatenames = "" # if no then leave it blank

# make a list of all the names by splitting alternate names by commas
    name_list = alternatenames.split(",")
    # Add the main place name to the list of alternate names
    name_list.append(asciiname)


    # create a regex pattern by joining the names with the '|' symbol #help from ChatGPT conversation 1 1
    regex_pattern = "|".join(re.escape(name) for name in set(name_list) if name)

    # add the patterns to the dictionary and start with the count 0
    if regex_pattern:
        patterns[asciiname] = regex_pattern
# dictionary to store total mentions per place
place_counts = {}

# dictionary to store mentions per month
mentions_per_month = {}

# Loop through each article file in the folder
for filename in os.listdir(folder):

    # build the file path
    file_path = os.path.join(folder, filename)# build the file path

    # Skip files before 2023-10-07
    if filename[:10] < "2023-10-07":  # goes through the first 10 characters in filename which represent YYYY-MM-DD
        continue

    # Extract the YYYY-MM part for the monthly count (e.g., "2023-11")
    month = filename[:7]

    with open(file_path, encoding="utf-8") as file: # Open and read the file content
        text = file.read()

        # Loop through all the place patterns and find their occurrences in the text:
        for placename, pattern in patterns.items():
            # Find all occurrences of the pattern in the text, considering word boundaries and ignoring case:
            matches = re.findall(r"\b(" + pattern + r")/b", text, flags=re.IGNORECASE)
            n_matches = len(matches)  # Count the number of occurrences of the place in the text.
            # add the number of times it was found to the total frequency
            if placename not in place_counts: # If the place is not already in the dictionary, initialize its count to 0
                place_counts[placename] = 0
            place_counts[placename] += n_matches

            if n_matches > 0:
                # Initialize if this pattern is not in the dictionary
                if placename not in mentions_per_month:
                    mentions_per_month[placename] = {}
                # Initialize the month entry for the placename if not present
                if month not in mentions_per_month[placename]:
                    mentions_per_month[placename][month] = 0
                # Add the current count of mentions to the existing total for the month
                mentions_per_month[placename][month] += n_matches
               
rows = []# Create an empty list to store the rows for saving data
# Loop through each place name in the mentions_per_month dictionary
for placename in mentions_per_month:
    # Loop through each month associated with the place name
    for month in mentions_per_month[placename]:
        # Get the mention count for the place and month
        count = mentions_per_month[placename][month]
        # Append a row with the place name, month, and mention count to the rows list
        rows.append([placename, month, count])

# Create DataFrame and export to a CSV file
df = pd.DataFrame(rows, columns=["placename", "month", "count"])
df.to_csv("regex_counts.tsv", sep="\t", index=False)
            



