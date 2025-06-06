import pandas as pd
import plotly.express as px

# Loading the data data usig which we will create the map
mentions_data = pd.read_csv("ner_counts.tsv", sep="\t")
coords_data = pd.read_csv("ner_gazetteer.tsv", sep="\t")

# Print column names to confirm that the columns are correct for smooth merging
print("Mentions columns:", mentions_data.columns.tolist())
print("Coords columns:  ", coords_data.columns.tolist())

# Rename columns to match for merging e.g the spelling column "place name" should be exactly the same for successful merging
mentions_data.rename(columns={"place name": "place_name", "count": "mention_count"}, inplace=True)
coords_data.rename(columns={"place name": "place_name", "Latitude": "latitude", "Longitude": "longitude"}, inplace=True)

# Merge datasets to use coordinates data of the places and frequency of mentions data at the same time
df = pd.merge(mentions_data, coords_data, on="place_name")

# Convert columns to numeric and drop rows with invalid/missing data
df[['mention_count', 'latitude', 'longitude']] = df[['mention_count', 'latitude', 'longitude']].apply(
    pd.to_numeric, errors='coerce'
)
df = df.dropna(subset=['mention_count', 'latitude', 'longitude'])

# Creating a scatter map for which we are setting values of variables which will define the attributes of the map
fig = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude",
    color="mention_count",
    size="mention_count",
    hover_name="place_name",
    color_continuous_scale=px.colors.sequential.Viridis,
    size_max=25,
    zoom=2
)

# Set layout and show map
fig.update_layout(title="Place Mentions Map", margin={"r":0, "t":40, "l":0, "b":0})
fig.show()

# Save as HTML
fig.write_html("place_mentions_map.html")


