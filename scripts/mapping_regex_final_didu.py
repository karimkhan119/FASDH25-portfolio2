# Import required libraries
import pandas as pd  # For data manipulation
import plotly.express as px  # For interactive visualizations
import kaleido  # For saving static images

# Load the gazetteer file with coordinates of places
coordinates_path = "../gazetteers/geonames_gaza_selection.tsv"
coordinates_df = pd.read_csv(coordinates_path, sep="\t")

# Load regex counts per place per month
counts_path = "../outputs/regex_counts.tsv"
counts_df = pd.read_csv(counts_path, sep="\t")

# Print the column names of both dataframes to check for compatibility
print("Coordinates DF Columns:", coordinates_df.columns)
print("Counts DF Columns:", counts_df.columns)

# Rename 'placename' to 'asciiname' in counts_df for consistency in merging
counts_df = counts_df.rename(columns={'placename': 'asciiname'})

# Merge the dataframes on the common 'asciiname' column
merge_df = pd.merge(coordinates_df, counts_df, on="asciiname")

# Check the merged dataframe to ensure the merge was successful
print(merge_df)

# Create a static map using frequency (count) as the color scale
fig = px.scatter_map(merge_df, 
                     lat="latitude", 
                     lon="longitude", 
                     hover_name="asciiname", 
                     color="count", 
                     color_continuous_scale=px.colors.sequential.Plasma)  # Changed color scale to Plasma

# Customize the map layout with a dark background style
fig.update_layout(map_style="carto-positron")  # Changed map style to light
fig.show()  # Display the static map

# Further customize the map with geographic features
fig.update_geos(
    projection_type="orthographic",  # Changed projection to orthographic for a globe-like appearance
    fitbounds="locations", 
    showcoastlines=True, coastlinecolor="DarkRed",  # Changed coastline color to DarkRed
    showland=True, landcolor="DarkGreen",  # Changed land color to DarkGreen
    showocean=True, oceancolor="LightSeaGreen",  # Changed ocean color to LightSeaGreen
    showlakes=False, lakecolor="RoyalBlue",  # Lakes hidden, can adjust color if visible
    showrivers=True, rivercolor="RoyalBlue",  # Changed river color to RoyalBlue
    showcountries=False, countrycolor="DarkSlateGray"  # Disabled country borders, dark color if enabled
)

# Show the customized static map with the new settings
fig.show()

# Save the static version of the map as a PNG image
fig.write_image("regex_map.png", scale=2)  # Higher scale for better resolution

# Create an animated map showing mentions per place over different months
fig = px.scatter_geo(merge_df, 
                     lat="latitude", 
                     lon="longitude", 
                     size="count", 
                     hover_name="asciiname", 
                     animation_frame="month", 
                     color="count", 
                     color_continuous_scale=px.colors.sequential.Plasma,  # Changed color scale to Plasma
                     projection="orthographic")  # Changed projection to orthographic for consistency

# Customize the layout and appearance of the animated map
fig.update_layout(
    title="Regex Mentions Over Time",  # Added title to the map
    title_font_size=22,  # Increased font size for title
    geo=dict(
        showland=True, 
        landcolor="lightgray",  # Lighter land color for contrast
        showocean=True, 
        oceancolor="lightblue",  # Light blue for ocean
        showrivers=True, 
        rivercolor="deepskyblue"  # Changed river color to DeepskyBlue for a clearer view
    )
)

# Display the animated map
fig.show()

# Save the interactive animated map as an HTML file
fig.write_html("regex_map.html")
