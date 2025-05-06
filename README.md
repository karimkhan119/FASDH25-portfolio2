# FASDH25-portfolio2
A repository for students' portfolios for mini-project 2
FASDH25-portfolio2/
│
├── AI Documentations/         
│   → Notes or documents explaining how AI was used in the project.
│
├── articles/                  
│   → This is where all the news articles are stored. These are the texts we analyzed.
│
├── gazetteers/               
│   → This folder has place name lists.
│   ├── countries.tsv          
│   │   → A general list of countries (not used directly in our part).
│   └── geonames_gaza_selection.tsv  
│       → This is the main file we used it has names of places in Gaza and their alternate spellings.
│
├── Maps/                     
│   → This is where we have saved maps.
│
├── Outputs/                  
│   → The results from running our scripts are here. For example: `regex_counts.tsv`, which shows how often each place was mentioned.
│
├── scripts/                  
│   → This is where the Python scripts are. It processes the articles and counts the place names.
│
└── README.md                 
    → This guide that explains about the whole project.


# Find and Count Gaza Places Names Mentioned in Articles

-The aim of this project is to find and count the names of places in Gaza that have appeared in articles written after October 7, 2023, the start date of the war.
-We have used Python to do this with the help of a list of place names (called a gazetteer) and some smart searching using regular expressions (regex). 
-The goal is to understand how often, and which places are being mentioned or talked about during the war.


## 2A: Use gazetteer and regex to extract places in Gaza from the corpus

-In this part of the project, we used a gazetteer (the file with names of places in Gaza) and a method called regular expressions (regex) to search out places through the collection of -articles and find out how often and when each place was mentioned.

### Read the Place Names (Gazetteer)

-Firstly we started by loading a file that lists the correct and alternate spellings of place names in Gaza. 
-It helps us to make sure we can catch mentions even if they were spelled differently example “Rafah and Refah”.

### Build Search Patterns (Regex)

-Using these names, we create regex patterns, special search tools that allow us to look for many versions of a name at once in a text. 
-For example, a pattern like Rafah|Refah will match either spelling.

### Go Through All the Articles

-We open each article written after October 7, 2023, and search the text for all the place names using the patterns we built.

### Count Mentions by Place and by Month

-Every time a place is mentioned, we add to its count. We also keep track of which month it was mentioned in, so we can see how the focus changes over time.

### Save the Results

-Once all articles have been processed, we save the results in a file called regex_counts.tsv. 
-This file includes, name of each place, the month it was mentioned, how many times it was mentioned in that month
-This step turns a large, unstructured collection of news articles into organized data that shows which places in Gaza were being talked about most and when.
-These results are later visualized on maps to help us better understand patterns in media coverage during the conflict.

###  Advantages of Using Gazetteer + Regex

-This method is easy to understand and implement. We know exactly what we are looking for (place names) and how we are searching for them (by matching names in text).
-We can control the gazetteer, we can decide which place names to include, add alternate spellings, or remove unnecessary entries. This gives us flexibility.
### Disadvantages of Using Gazetteer + Regex

-Regex only matches exact words or patterns. If the place name appears with a typo or unexpected formatting, it might be missed.
-If place names appear in different languages like Arabic they are spelled differently than what is in the gazetteer, they would not be matched unless we have included every variation

# 2B Use stanza to extract all place names from (part of) the corpus

-This project aims to automatically identify, count, and map geographical place names found in news articles. 
-By focusing on content written in January 2024, it compares two distinct methods—NER (using Stanza) and a regex+gazetteer approach—highlighting their advantages and limitations.

### Named Entity Recognition with Stanza

-Adapted a Colab notebook (Gaza_NER2_groupname.ipynb) to use a larger corpus.
-Filtered the dataset to include only January 2024 articles.
-Used Stanza’s NER module to extract locations only.
-Cleaned and normalized names (e.g., “Gaza’s” merged into “Gaza”).
-Wrote results into ner_counts.tsv, showing placename and count.

### Building a Gazetteer

-Script build_gazetteer.py reads ner_counts.tsv.
-Used geocoding (via geopy or API) to find coordinates.
-Output saved as NER_gazetteer.tsv with placename, latitude, and longitude.
-Manual geocoding was done for places not found via automatic methods:
-Beit Hanoun
-Jabalia refugee camp
-Nuseirat
-Maghazi
-Bureij camp

### Mapping the Places

-Visual maps created from the NER and regex-based datasets.
-Stored in the maps/ folder as:
-ner_map_jan2024.png
-regex_map_jan2024.png

### structure of repository
 
 -This project is clearly organized, and the folder structure is explained in this section. 
 -The main notebook, Gaza_NER2_groupname.ipynb, extracts place names from January 2024 news articles using Stanza. 
 -These names and their counts are saved in ner_counts.tsv. 
 -Then, build_gazetteer.py geocodes the names and saves the coordinates in gazetteer/NER_gazetteer.tsv.
 -Two maps—one using NER data and one using regex—are stored in the maps folder. 



### Advantages

-Can detect new and unknown place names.
-Understands context and can work across different sentence structures.
-Does not rely on a fixed list.
### Disadvantages

-Slower and more resource intensive.
-Sometimes extracts incorrect or irrelevant entities.
-Requires post-processing to clean the output.

## Style used for regex map and why (comparision)

-The map generated in this project uses a natural earth projection with a scatter geo style, which plots geographical coordinates as individual points on a global map.
-This style was chosen because it effectively visualizes the spatial distribution of place name mentions across different regions.
-The natural earth projection provides a visually balanced and proportionally accurate view of the continents, making it ideal for global datasets.
-The scatter plot format allows each place to be marked with a circle whose size corresponds to its frequency of mention, enabling quick visual comparison of prominence.
-This style is both intuitive and informative, making it easy for viewers to interpret the density and spread of place references without overwhelming them with unnecessary geographic detail. -It’s particularly suitable for digital humanities work, where clarity, simplicity, and contextual insight into textual geographies are essential.
-regex_map/Maps/FASDH25-portfolio2
-ner_map/Maps/FASDH25-portfolio2
