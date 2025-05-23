import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Step 1: Load the regex_counts data from the Outputs folder
df = pd.read_csv("../Outputs/regex_counts.tsv", sep="\t")

# Step 2: Geocode the placenames using Nominatim
geolocator = Nominatim(user_agent="geoapi")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

df["location"] = df["placename"].apply(geocode)
df["latitude"] = df["location"].apply(lambda loc: loc.latitude if loc else None)
df["longitude"] = df["location"].apply(lambda loc: loc.longitude if loc else None)

# Remove rows with missing coordinates
df = df.dropna(subset=["latitude", "longitude"])

# Step 3: Plot the map using Plotly
fig = px.scatter_geo(
    df,
    lat="latitude",
    lon="longitude",
    text="placename",
    size="count",
    size_max=20,
    hover_name="placename",
    projection="natural earth",
    title="Place Mentions from Regex Counts"
)

fig.update_layout(geo=dict(showland=True, landcolor="lightgray"))

# Save the map as HTML in the Outputs folder
fig.write_html("../Outputs/regex_map.html")

# Optional: also display the map in a browser
fig.show()
