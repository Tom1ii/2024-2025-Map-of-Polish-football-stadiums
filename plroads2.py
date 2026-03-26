import osmnx as ox
import geopandas as gpd

# Określamy obszar dla jakiego pobieramy
place = "Poland"

# Definicja tagów co chcemy pobrać
tags_dk = {"highway": ["motorway", "trunk", "primary"]}  # Autostrady, drogi ekspresowe, drogi krajowe (uproszczenie)
tags_a = {"highway": ["motorway"]}  # Tylko autostrady

# Pobierz graf sieci drogowej dla dróg krajowych
G_dk = ox.graph_from_place(place, network_type="drive", custom_filter='["highway"~"motorway|trunk|primary"]')

# Pobierz graf sieci drogowej dla autostrad
G_a = ox.graph_from_place(place, network_type="drive", custom_filter='["highway"~"motorway"]')

# Konwertujemy na geodataframe
gdf_edges_dk = ox.graph_to_gdfs(G_dk, nodes=False, edges=True)
gdf_edges_a = ox.graph_to_gdfs(G_a, nodes=False, edges=True)

# Zapisujemy gdf do shape'a
filepath_dk = "poland_national_roads_edges.shp"
gdf_edges_dk.to_file(filepath_dk, driver="ESRI Shapefile", encoding="utf-8")

filepath_a = "poland_motorways_edges.shp"
gdf_edges_a.to_file(filepath_a, driver="ESRI Shapefile", encoding="utf-8")

print(f"Odcinki dróg krajowych zapisane jako: {filepath_dk}")
print(f"Odcinki autostrad zapisane jako: {filepath_a}")