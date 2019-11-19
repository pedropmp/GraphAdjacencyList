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
    def __init__(self, id=None):
        self.id = id
        self.next = None

    def __str__(self):
        return "{}".format(self.id)

'''
Graph is a data structure of Vertices and an adjacency list or matrix of adjacencies
'''
class Graph:
    def __init__(self, id):
        self.id = id
        self.adjList = []  #adjList is a list of heads (first vertex/node of a linked list)


    def showList(self):
        print(self.adjList)
        for vertex in self.adjList:
            while vertex.next != None:
                print(vertex)
                

    '''
    Graph method that creates an Node, where the Vertex and adds a new index in the adjacency matrix.
    The node created does not have any edges from or to it.
    '''
    def InsertVertex(self, vertexId):
        self.adjList.append(Vertex(vertexId))

    def RemVertex(self, vertexId):
        for i in range(0, len(adjList)):
            if adjList[i].


def NewVertex(graphId, vertexId):
    newVertex = Vertex(vertexId)
    for graph in graphs:
        if graph.id == graphId:
            graph.InsertVertex(newVertex)

def DelVertex(graphId, vertexId):
    for graph in graphs:
        if graph.id == graphId:
            graph.RemVertex(vertexId)


def InsertEdge():
    pass


def RemEdge():
    pass


def NewGraph(id):
    graphs.append(Graph(id))


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
    for line in fileLines:
        if line != '':
            if line[0] != '*':
                fileCommands.append(line.split(' '))
    
    print('##### Comandos lidos #####\n')
    for commandLine in fileCommands:
        for command in commandLine:
            print('{} '.format(command), end= '')
        print('')
    print('\n\n')
    newFile.close()

def menu():
    for command in fileCommands:
        if command[0].lower() == 'graph':
            NewGraph(command[1])
        elif command[0].lower() == 'vertex':
            NewVertex(command[1], command[2])


def main():
    CommandInput()
    global graphs
    graphs = []
    vertices = []
    menu()

  
    graphs[0].showList()

main()