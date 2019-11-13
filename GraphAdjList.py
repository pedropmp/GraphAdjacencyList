'''
Autor: Pedro Miranda Pinheiro
Matricula: 128012

Project developed for the Algorithms and Data Structures II course in 2019
Pourpose: To implement an algorithm to manipulate and show vertices and edges of a graph
'''

'''
Vertex are the elements of a Graph
'''
class Vertex:
    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return "{}".format(self.data)

    def set_data(self, newData): 
        self.data = newData
    
    def set_next(self, newNext):
        self.next = newNext


'''
Graph is a data structure of Vertices and a adjacency list or matrix
'''
class Graph:
    def __init__(self, root=None):
        self.adjList = []

    def showList(self):
        for node in self.adjList:
            while node != None:
                print(node.val)

'''
Nodes are the LinkedList elements
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None #pointer initially points to nothing


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


def CommandInput():    
    newFile = open('entrada.txt', 'r')
    fileLines = newFile.read().split('\n')
    global fileData
    fileData = []
    for line in fileLines:
        if line != '' and line[0] != '*':
            fileData.append(line)

CommandInput()
print(fileData)

'''nodes = []
adjList = []
nodes.append(InsertNode('ola mundo'))
for i in range(0, len(nodes)):
    print(nodes[i])
    print(adjList[i])'''