import osmnx as ox
import networkx as nx

# 1. Graph laden
place = "Universität Leuphana, Lüneburg, Germany"
G = ox.graph_from_place(place, network_type='walk')

# 2. Start- und Zielpunkt (Koordinaten)
start = (53.566, 9.984)  # Beispielkoordinaten
end = (53.568, 9.987)

start_node = ox.nearest_nodes(G, start[1], start[0])
end_node = ox.nearest_nodes(G, end[1], end[0])

# 3. Kürzeste Route berechnen (z.B. nach Länge)
route = nx.shortest_path(G, start_node, end_node, weight='length')

# Route visualisieren
ox.plot_graph_route(G, route)

import matplotlib.pyplot as plt
plt.show()