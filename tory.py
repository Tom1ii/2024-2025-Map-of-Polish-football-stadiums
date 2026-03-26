import osmnx as ox
import geopandas as gpd

# Określamy obszar
place = "Poland"

# Pobieramy sieć torów
tags_rail = {"railway": ["rail", "light_rail", "subway", "tram"]}
G_rail = ox.graph_from_place(place, network_type="all", custom_filter='["railway"~"rail|light_rail|subway|tram"]')
gdf_edges_rail = ox.graph_to_gdfs(G_rail, nodes=False, edges=True)

# Pobieramy stacje
tags_stations = {"railway": "station"}
gdf_stations = ox.features_from_place(place, tags_stations)

# Zapisujemy sieć torów kolejowych jako Shape
filepath_rail_edges = "poland_rail_edges.shp"
gdf_edges_rail.to_file(filepath_rail_edges, driver="ESRI Shapefile", encoding="utf-8")

# Zapisujemy stacje jako Shapefile
filepath_stations = "poland_rail_stations.shp"
gdf_stations.to_file(filepath_stations, driver="ESRI Shapefile", encoding="utf-8")

print(f"Sieć torów kolejowych zapisana jako: {filepath_rail_edges}")
print(f"Stacje kolejowe zapisane jako: {filepath_stations}")