import pandas as pd
import plotly.express as px

# Load the mentions data (place_name and count)
mentions_data = pd.read_csv('ner_counts', sep='\t')

# Load the coordinates data (place_name, latitude, longitude)
coordinates_data = pd.read_csv('ner_gazetteer', sep='\t')

# Merge the two datasets on place_name
combined_data = pd.merge(mentions_data, coordinates_data, on='place_name')

# Create the map visualization
map_figure = px.scatter_mapbox(
    combined_data,
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

# Set map style and layout
map_figure.update_layout(
    mapbox_style="open-street-map",
    title="Place Mentions Frequency Map",
    margin={"r": 0, "t": 40, "l": 0, "b": 0}
)

# Show the map
map_figure.show()

# Save as HTML file
map_figure.write_html("place_mentions_map.html")
