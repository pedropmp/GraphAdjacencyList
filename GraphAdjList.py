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

'''
This function opens, reads and closes the entrada.txt input file. 
After reading it, it produces de fileCommands global list, wich contains
a list of lists with commands and names for the instances of the classes.
'''
def CommandInput():    
    newFile = open('entrada.txt', 'r')
    fileLines = newFile.read().split('\n')
    global fileCommands
    fileCommands = []
    i = 0
    while i < len(fileLines):
        if fileLines[i] != '' and fileLines[i][0] != '*':
            fileCommands.append([fileLines[i], fileLines[i+1]])
            i += 2
        else:
            i += 1
    newFile.close()

def main():
    CommandInput()
    print(fileCommands)
    graphs = []
    vertices = []
    for command in fileCommands:
        if command[0].lower() == 'graph':
            graphs.append(Graph())
        elif command[0].lower() == 'vertex':
            vertices.append(Vertex(command[1]))

    print(graphs[0])
    print(vertices[0])
            

main()