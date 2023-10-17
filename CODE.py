#!/usr/bin/env python
# coding: utf-8
import networkx as nx
import random
import matplotlib.pyplot as plt
# Set the seed value for the random number generator
random.seed(45)
# Create a graph representing a 5G network with 15 nodes
G_5g=nx.connected_watts_strogatz_graph(15,4, 0.5)
# Create a graph representing a 6G network with 15 nodes
G_6g=nx.connected_watts_strogatz_graph(15, 4, 0.1)
# Draw the network graphs
nx.draw(G_5g,with_labels=True)
plt.title('5G Network Graph')
plt.show()
nx.draw(G_6g,with_labels=True)
plt.title('6G Network Graph')
plt.show()
# Generate fixed random traffic for each network
traffic_5g=[2,6,9,10,4,8,7,1,3,5,2,4,9,7,3]
traffic_6g=[8,4,2,10,1,9,6,5,7,3,2,5,3,4,7]
# Calculate the total bandwidth of each network
bandwidth_5g=sum(traffic_5g)*nx.average_shortest_path_length(G_5g)
bandwidth_6g=sum(traffic_6g)*nx.average_shortest_path_length(G_6g)
# print results
print("5G network bandwidth: ",bandwidth_5g)
print("6G network bandwidth: ",bandwidth_6g)
# Plot the results
labels=['5G','6G']
bandwidths=[bandwidth_5g,bandwidth_6g]
plt.bar(labels,bandwidths,color=['blue','red'])
plt.ylabel('Bandwidth')
plt.title('Bandwidth Comparison')
plt.show()
