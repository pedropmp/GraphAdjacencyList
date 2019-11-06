'''
Autor: Pedro Miranda Pinheiro
Matricula: 128012

Project developed for the Algorithms and Data Structures II course in 2019
Pourpose: To implement an algorithm to manipulate and show vertices and edges of a graph
'''

class Node:
    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return "{}".format(self.data)

    def set_data(self, newData): 
        self.data = newData
    
    def set_next(self, newNext):
        self.next = newNext
    
class Graph:
    def __init__(self, root=None):
        self.root = root

'''
Function that creates an Node and adds a new index in the adjacency matrix
'''
def InsertNode(newData):
    newNode = Node(newData)
    adjList.append([])
    return  newNode


def RemNode():
    pass


def InsertEdge():
    pass


def RemEdge():
    pass


def ShowGraph():
    pass


def IDSourceSink():
    pass

nodes = []
adjList = []
nodes.append(InsertNode('ola mundo'))
for i in range(0, len(nodes)):
    print(nodes[i])
    print(adjList[i])