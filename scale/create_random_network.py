import plotly.graph_objects as go
import networkx as nx
import random
import os

n = 10
print('Creating '+str(n)+' random geometric node graph ')
G = nx.random_geometric_graph(n, 0.5)

ip_list =[]
print('Creating '+str(n)+' random IP address for the node')
while len(ip_list) < n:
    x1 = 99
    x2 = random.randint(0,255)
    x3 = random.randint(0,255)        
    x4 = random.randint(0,255)
    result = ".".join(map(str,([x1,x2,x3,x4])))
    if result not in ip_list:    
        ip_list.append(result)

# preparing for node configuration
node_att =[]
for i,node in enumerate(G.nodes()):
    host_name = 'host'+str(node+1)
    host_ip = ip_list[i]
    as_name = 'AS'+str(node+1)
    router_name = 'router'+str(node+1)
    node_att.append(host_name+';'+host_ip+';'+router_name+';'+as_name)

#write node configuration to file
print('Writing the node configuration to the file ')
with open('node_setup.txt','w') as node_seed:
    for row in node_att :
        node_seed.write(row+'\n')

#Preparing for Peer configuration
peer_att=[]
for x,edge in enumerate(G.edges()):
    peer = str(edge)
    peer_x, peer_y = map(str.strip,peer.split(','))
    peer_x = int(peer_x.lstrip('(').rstrip('\n'))+1
    peer_y = int(peer_y.rstrip(')'))+1
    ip_x = ip_list[peer_x-1]
    ip_y = ip_list[peer_y-1]
    peer_att.append(str(peer_x)+';'+str(ip_x)+';'+str(peer_y)+';'+str(ip_y))
    peer_att.append(str(peer_y)+';'+str(ip_y)+';'+str(peer_x)+';'+str(ip_x))
    # print('this is peer x :' +str(peer_x) +'and peer y :' + str(peer_y)+ 'this is x' +ip_x+'this is ip y'+ip_y)

print('Writing the Peer Configuration to the file')
with open('peer_setup.txt','w') as peer_seed:
    for peer in peer_att:
        peer_seed.write(peer+'\n')

edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

# print(edge_trace)
node_x = []
node_y = []
for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(G.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('# of connections: '+str(len(adjacencies[1]))+';'+node_att[node])

node_trace.marker.color = node_adjacencies
node_trace.text = node_text

fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Network graph made with Python',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.show()
