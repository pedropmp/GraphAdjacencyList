'''
Author: Pedro Miranda Pinheiro


Project developed for the Algorithms and Data Structures II course in 2019
Pourpose: To implement an algorithm to manipulate and show vertices and edges of a graph
'''

from os import system, name
from time import sleep


# ----- VERTEX CLASS -----
'''
Vertex are the elements of a Graph
'''
class Vertex:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def __str__(self):
        return "{}".format(self.id)
    
# ----- END OF VERTEX CLASS -----


# ----- GRAPH CLASS -----
'''
Graph is a data structure of Vertices and an adjacency list or matrix of adjacencies
'''
class Graph:
    def __init__(self, id):
        self.id = id
        self.adjList = []  #adjList is a list of heads (first vertex/node of a linked list)


    def ShowList(self):
        print('----- Adjacency list -----')
        for vertex in self.adjList:
            print('{}'.format(vertex), end=' -> ')
            for neighbor in vertex.neighbors:
                print('{}'.format(neighbor), end=' -> ')
            print('none')
                

    '''
    Graph method that creates an Node, where the Vertex and adds a new index in the adjacency matrix.
    The node created does not have any edges from or to it.
    '''
    def InsertVertex(self, vertexId):
        self.adjList.append(Vertex(vertexId))


    '''Graph method that removes a vertex calling remove edge for its edges and then removing the 
    vertex itself'''
    def RemVertex(self, vertexId):
        for i in range(0, len(self.adjList)):
            if str(self.adjList[i].id) == vertexId:  # needed to use str so that the interpreter could compare the strings
                self.adjList.pop(i)
                print('{} vertex deleted.\n'.format(vertexId))

    def InsertEdge(self, vertexId1, vertexId2):
        # search for first vertex
        for first_vertex in self.adjList:
            if str(first_vertex.id) == vertexId1:
                # search for second vertex
                for second_vertex in self.adjList:
                    if str(second_vertex.id) == vertexId2:
                        print('Both vertices found.\n')
                        first_vertex.neighbors.append(second_vertex)
                        second_vertex.neighbors.append(first_vertex)


# ----- END OFGRAPH CLASS -----


# ----- MAIN FUNCTIONS -----

'''This function creates a vertex for a specific graph'''
def NewVertex(graphId, vertexId):
    newVertex = Vertex(vertexId)
    for graph in graphs:
        if graph.id == graphId:
            graph.InsertVertex(newVertex)

'''This function will try to delete a vertex given its ID for a specific graph'''
def DelVertex(graphId, vertexId):
    print('Deleting vertex {}...'.format(vertexId))
    for graph in graphs:
        if graph.id == graphId:
            graph.RemVertex(vertexId) #calling graph remove vertex method

'''This function will try to create an edge between two vertices'''
def NewEdge(graphId, vertexId1, vertexId2):
    for graph in graphs:
        if graph.id == graphId:
            print('Graph found. Creating new edge...')
            graph.InsertEdge(vertexId1, vertexId2)


def DelEdge():
    pass


def NewGraph(id):
    graphs.append(Graph(id))


def ShowGraph(graphId):
    for graph in graphs:
        if graph.id == graphId:
            graph.ShowList()    


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
    for line in fileLines:
        if line != '':
            if line[0] != '*':
                fileCommands.append(line.split(' '))
    
    print('----- Comandos lidos -----\n')
    for commandLine in fileCommands:
        for command in commandLine:
            print('{} '.format(command), end= '')
        print('')
    print('')
    sleep(2)
    system('cls')
    newFile.close()

def menu():
    for command in fileCommands:
        if command[0].lower() == 'graph':
            NewGraph(command[1])
        elif command[0].lower() == 'vertex':
            NewVertex(command[1], command[2])
        elif command[0].lower() == 'delvertex':
            DelVertex(command[1], command[2])
        elif command[0].lower() == 'edge':
            NewEdge(command[1], command[2], command[3])
        elif command[0].lower() == 'show':
            ShowGraph(command[1])

# ----- END OF MAIN FUNCTIONS -----


# ----- MAIN -----

def main():
    CommandInput()
    global graphs
    graphs = []
    menu()


main()

# ----- END OF MAIN -----
