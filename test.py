import osmnx as ox

# Bereich definieren (z.B. Uni-Campus)
place = "Universität Leuphana, Lüneburg, Germany"
graph = ox.graph_from_place(place, network_type='walk')

# Als GeoDataFrame exportieren (optional)
nodes, edges = ox.graph_to_gdfs(graph)

# Visualisierung
ox.plot_graph(graph)