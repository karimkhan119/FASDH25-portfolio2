# FASDH25-portfolio2
A repository for students' portfolios for mini-project 2

# Find and Count Gaza Places Names Mentioned in Articles
-The aim of this project is to find and count the names of places in Gaza that have appeared in articles written after October 7, 2023, the start date of the war.
-We have used Python to do this with the help of a list of place names (called a gazetteer) and some smart searching using regular expressions (regex). 
-The goal is to understand how often, and which places are being mentioned or talked about during the war.


## 2A: Use gazetteer and regex to extract places in Gaza from the corpus 
In this part of the project, we used a gazetteer (the file with names of places in Gaza) and a method called regular expressions (regex) to search out places through the collection of articles and find out how often and when each place was mentioned.

### Read the Place Names (Gazetteer)
Firstly we started by loading a file that lists the correct and alternate spellings of place names in Gaza. It helps us to make sure we can catch mentions even if they were spelled differently example “Rafah and Refah”.

### Build Search Patterns (Regex)
Using these names, we create regex patterns, special search tools that allow us to look for many versions of a name at once in a text. For example, a pattern like Rafah|Refah will match either spelling.

### Go Through All the Articles
We open each article written after October 7, 2023, and search the text for all the place names using the patterns we built.

### Count Mentions by Place and by Month
Every time a place is mentioned, we add to its count. We also keep track of which month it was mentioned in, so we can see how the focus changes over time.

### Save the Results
Once all articles have been processed, we save the results in a file called regex_counts.tsv. This file includes, name of each place, the month it was mentioned, how many times it was mentioned in that month
This step turns a large, unstructured collection of news articles into organized data that shows which places in Gaza were being talked about most and when. These results are later visualized on maps to help us better understand patterns in media coverage during the conflict.

###  Advantages of Using Gazetteer + Regex
This method is easy to understand and implement. We know exactly what we are looking for (place names) and how we are searching for them (by matching names in text).
 We can control the gazetteer, we can decide which place names to include, add alternate spellings, or remove unnecessary entries. This gives us flexibility.
### Disadvantages of Using Gazetteer + Regex
Regex only matches exact words or patterns. If the place name appears with a typo or unexpected formatting, it might be missed.
