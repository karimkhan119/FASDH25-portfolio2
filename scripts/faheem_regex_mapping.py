#importing the necessary libraries
import pandas as pd
import plotly.express as px

#loading the regex-extracted place frequencies with month
regex_df = pd.read_csv("regex_counts.tsv", sep="\t")

# Cleaning the column names (remove extra spaces)
regex_df.columns = regex_df.columns.str.strip()

#loading the coordinates
coordinates_df = pd.read_csv("gazetteers/geonames_gaza_selection.tsv", sep="\t")
coordinates_df.columns = coordinates_df.columns.str.strip()
#coordinates_df = pd.read_csv(coordinates_path, sep="\t")
#print the dataframe
#print(coordinates_df)

#merging regex data with coordinates using the common column "asciiname"
merged_df = pd.merge(regex_df, coordinates_df, left_on="placename", right_on="asciiname")

#print(merged_df)
# Cleaning data (remove rows with missing lat, lon, or frequency)
merged_df = merged_df.dropna(subset=["latitude", "longitude", "count"])

# Check the merged dataframe for correctness
#print(merged_df.head())
  
# Creating animated map of all the place names
fig = px.scatter_mapbox(
    merged_df,
    lat="latitude",
    lon="longitude",
    hover_name="placename",
    size="count",
    color="count",
    animation_frame="month",
    color_continuous_scale=px.colors.sequential.YlOrRd,
    title="Regex-Extracted Place Names by Month"
)
#  Setting map style 
fig.update_layout(mapbox_style="carto-positron-nolables")
# Save outputs
#fig.write_html("regex_map.html")

fig.write_image("regex_map.png")

# Show the map
#fig.show()






 

 
