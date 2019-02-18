########################################################################
#							   Plot									   #
#						GOEKHAN POLAT (0830690)						   #
########################################################################

# -*- coding: UTF-8 -*-
import codecs
import networkx as nX
import matplotlib.pyplot as plot

def main():
    plotNetworkA()
    plotNetworkB()


def plotNetworkA():
    actors = getData('../networks/actorLabelsA.txt')
    events = getData('../networks/eventLabelsA.txt')
    matrix = getMatrix('../networks/networkA.csv')

    network = nX.Graph()
    
    for i in range(0, len(actors)):
        row = matrix[i]
        for j in range(0, len(events)):
            if row[j]:
                network.add_edge(actors[i], events[j])
                
    plot.figure(figsize = (20, 20))
    pos = nX.spring_layout(network)
    nX.draw_networkx_edges(network, pos)
    nX.draw_networkx_nodes(network, pos, actors, node_color='r')
    nX.draw_networkx_nodes(network, pos, events , node_color='b')	
    nX.draw_networkx_labels(network, pos)
    plot.savefig('visualNetworkA.png')

def plotNetworkB():
    actors = getData('../networks/nodeLabelsB.txt')
    matrix = getMatrix('../networks/networkB.csv')
    network = nX.Graph()
    
    for i in range(0, len(actors)):
        row = matrix[i]
        for j in range(0, len(actors)):
            if row[j]:
                network.add_edge(actors[i], actors[j])
                
    plot.figure(figsize = (30, 30))
    pos = nX.spring_layout(network)
    nX.draw_networkx_edges(network, pos)
    nX.draw_networkx_nodes(network, pos, actors, node_color='g')	
    nX.draw_networkx_labels(network, pos)
    plot.savefig('visualNetworkB.png')    
    
    
def getData(path):
    file = codecs.open(path,'r', 'utf-8')
    array = []
    for entry in file:
        array.append(entry)
    return array

def getMatrix(file):
    matrix = []    
    file = codecs.open(file, 'r',  'utf-8')
    
    for line in file:
        i = 0
        row = []
        for i in range (0, len(line)):
            if (line[i] == '0'):
                row.append(0)           
            if (line[i] == '1'):
                row.append(1)
        matrix.append(row)
    return matrix

if __name__ == '__main__':
    main()
