
import re
import os
import pandas as pd


# saves dictionary data to tsv file with specified columns.
# to store place_name counts
def write_tsv(data,column_list, path): 
    

    # converts the dictionary into a list of (key, value) for dataframe creation:
    items = list(data.items())
    # converts the list of place counts into a table:
    df = pd.DataFrame.from_records(items, columns=column_list)
    # write the dataframe in tsv form to avoid commas:
    df.to_csv(path, sep="\t", index=False)



# Define path to the folder conatining all article text files:
folder = "../articles"  

# define the patterns we want to search:

# path to the gazeteer file from the portfolio:
path = "../gazetteers/geonames_gaza_selection.tsv"
# read file with UTF-8 to handle Arabic/Hebrew place names:
with open(path, encoding="utf-8") as file:
    # read entire file content into a string
    data = file.read()

# create an empty dictionary to store place_name: count:
patterns = {}
# split gazetteer text into rows one per line to access each place name:
rows = data.split("\n")
# skip the first row and include the remaining to form regex pattern:
for row in rows[1:]:
    #split row into tab-separated columns:
    columns = row.split("\t")
    all_names = [column[0], column[1]] + column[2].split(',')
    patterns[name] = 0

# count the number of times each pattern is found in the entire folder:
for filename in os.listdir(folder):
    # build the file path:
    file_path = f"{folder}/{filename}"
    #print(f"The path to the article is: {file_path}")

    # load the article (text file) into Python:
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # find all the occurences of the patterns in the text:
    for pattern in patterns:
        matches = re.findall(pattern, text)
        n_matches = len(matches)
        # add the number of times it was found to the total frequency:
        patterns[pattern] += n_matches

# print the frequency of each pattern:
for pattern in patterns:
    count = patterns[pattern]
    if count >= 1:
        print(f"found {pattern} {count} times")

# call the function to write your tsv file:
columns = ["asciiname", "frequency"]
tsv_filename = "frequencies.tsv"
write_tsv(patterns, columns, tsv_filename)
