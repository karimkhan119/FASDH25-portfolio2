# FASDH25-portfolio2
A repository for students' portfolios for mini-project 2
Syed Azhar Uddin

# 2B Use stanza to extract all place names from (part of) the corpus
This project aims to automatically identify, count, and map geographical place names found in news articles. By focusing on content written in January 2024, it compares two distinct methods—NER (using Stanza) and a regex+gazetteer approach—highlighting their advantages and limitations.

## 1. Named Entity Recognition with Stanza
Adapted a Colab notebook (Gaza_NER2_groupname.ipynb) to use a larger corpus.

Filtered the dataset to include only January 2024 articles.

Used Stanza’s NER module to extract locations only.

Cleaned and normalized names (e.g., “Gaza’s” merged into “Gaza”).

Wrote results into ner_counts.tsv, showing placename and count.

## 2. Building a Gazetteer
Script build_gazetteer.py reads ner_counts.tsv.

Used geocoding (via geopy or API) to find coordinates.

Output saved as NER_gazetteer.tsv with placename, latitude, and longitude.

Manual geocoding was done for places not found via automatic methods:

Beit Hanoun

Jabalia refugee camp

Nuseirat

Maghazi

Bureij camp

## 3. Mapping the Places
Visual maps created from the NER and regex-based datasets.

Stored in the maps/ folder as:

ner_map_jan2024.png

regex_map_jan2024.png
## structure of repository
 This project is clearly organized, and the folder structure is explained in this section. The main notebook, Gaza_NER2_groupname.ipynb, extracts place names from January 2024 news articles using Stanza. These names and their counts are saved in ner_counts.tsv. Then, build_gazetteer.py geocodes the names and saves the coordinates in gazetteer/NER_gazetteer.tsv. Two maps—one using NER data and one using regex—are stored in the maps folder. 

## Regex + Gazetteer
Advantages:
Simple and fast.
High accuracy if the gazetteer list is complete.
Easy to implement with minimal setup.
Disadvantages:
Misses place names that are not in the gazetteer.
cannot handle different spellings or variations.
Requires manual updates to the list.
## NER (Named Entity Recognition using Stanza)
Advantages:
Can detect new and unknown place names.
Understands context and can work across different sentence structures.
Does not rely on a fixed list.
Disadvantages:
Slower and more resource intensive.
Sometimes extracts incorrect or irrelevant entities.
Requires post-processing to clean the output.


