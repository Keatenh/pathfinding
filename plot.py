import networkx as nx
import matplotlib.pyplot as plt
import dijkstra
from tome_iii_lvl_i import node_list
from node import get_node_details
# G = nx.Graph()
G = nx.DiGraph()
def node_pos(node):
    return ([ord(char) - 97 for char in node[0].lower()][0],-int(node[1]))
def set_edges(nodes):
    l = []
    for n in nodes:
        for o in n["origins"]:
            l.append((o,n["name"]))
    return l
fixed_positions = {}
edges = []
# G.add_nodes_from([n["name"] for n in node_list])
for n in node_list:
    G.add_node(n["name"],s=get_node_details(n["kind"])["style"])
edges = set_edges(node_list) #list of tuples
G.add_edges_from(edges)
# G.add_edges_from([("A0","B0"),("B0","C0"),("C0","D0")])
for node in node_list:
    fixed_positions[node["name"]] = node_pos(node["name"])
# print(fixed_positions)
fixed_nodes = fixed_positions.keys()
pos = nx.spring_layout(G,pos=fixed_positions, fixed=fixed_nodes)
# fig, ax = plt.subplots()

#Get all distinct node classes according to the node shape attribute
node_shapes = set((a_shape[1]["s"] for a_shape in G.nodes(data = True)))
#For each node class...
for a_shape in node_shapes:
    #...filter and draw the subset of nodes with the same symbol in the positions that are now known through the use of the layout.
    nx.draw_networkx_nodes(G,pos,node_shape = a_shape, nodelist = [sNode[0] for sNode in filter(lambda x: x[1]["s"]==a_shape,G.nodes(data = True))])
#Finally, draw the edges between the nodes
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos,font_size=8, font_weight="bold", font_family="monospace")
# TODO: get node labels without redrawing graph
# nx.draw_networkx(G,pos,arrows=True,node_size=0)
# nx.draw(G, pos=pos, with_labels=True,  node_shape="s",  node_color="none", bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'))


# limits=plt.axis('on') # turns on axis
# ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

path1 = dijkstra.run()
path1_edges = []
for i in range(len(path1)-1):
    path1_edges.append((path1[i],path1[i+1]))
nx.draw_networkx_edges(G, pos, edgelist=path1_edges, edge_color='r', arrows=True)
plt.show()

