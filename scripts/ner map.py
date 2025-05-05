import os
import pandas as pd
import numpy as np
import plotly.express as px

# 0. Sanity-check: working directory and files
print("CWD:", os.getcwd())
print("Files:", os.listdir())

# 1. Load with explicit extensions
mentions_data   = pd.read_csv('ner_counts.tsv',   sep='\t', dtype=str)
coords_data     = pd.read_csv('ner_gazetteer.tsv', sep='\t', dtype=str)

# 2. Inspect and print columns
print("Mentions columns:", mentions_data.columns.tolist())
print("Coords columns:  ",   coords_data.columns.tolist())

# 3. Standardize and rename columns for clarity/merge
#    Adjust the left/right names below to match what you actually saw printed.

# Example: if your mentions file has columns ['place', 'count']:
mentions_data = mentions_data.rename(columns={
    'place':       'place_name',     # or adjust to whatever your file uses
    'count':       'mention_count'
})

# Example: if your coords file has ['place', 'lat', 'lon']:
coords_data = coords_data.rename(columns={
    'place':       'place_name',
    'lat':         'latitude',
    'lon':         'longitude'
})

# 4. Merge on place_name
combined = pd.merge(
    mentions_data, 
    coords_data, 
    on='place_name', 
    how='inner'      # or 'left' if you want to keep unmapped mentions
)

# 5. Convert coords to numeric, handle missing
combined['latitude']  = pd.to_numeric(combined['latitude'],  errors='coerce')
combined['longitude'] = pd.to_numeric(combined['longitude'], errors='coerce')
combined['mention_count'] = pd.to_numeric(combined['mention_count'], errors='coerce')

# 6. Drop any rows missing coordinates
clean = combined.replace({0: np.nan}).dropna(subset=['latitude','longitude'])

# 7. Build the map
fig = px.scatter_mapbox(
    clean,
    lat="latitude",
    lon="longitude",
    size="mention_count",
    color="mention_count",
    hover_name="place_name",
    hover_data={"mention_count": True},
    color_continuous_scale=px.colors.sequential.Redor,
    size_max=25,
    zoom=1
)
fig.update_layout(
    mapbox_style="open-street-map",
    title="Place Mentions Frequency Map",
    margin={"r":0,"t":40,"l":0,"b":0}
)

# 8. Display & save
fig.show()
fig.write_html("place_mentions_map.html")
print("✔ Map saved to place_mentions_map.html")

