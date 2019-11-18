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
        self.next = None

    def __str__(self):
        return "{}".format(self.data)

    def set_data(self, newData): 
        self.data = newData
    
    def set_next(self, newNext):
        self.next = newNext


'''
Graph is a data structure of Vertices and an adjacency list or matrix of adjacencies
'''
class Graph:
    def __init__(self):
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
    def InsertVertex(self, data):
        self.adjList.append(Vertex(data))


def RemVertex():
    pass


def InsertEdge():
    pass


def RemEdge():
    pass


def NewGraph():
    graphs.append(Graph())


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
    graphs = []
    vertices = []
    for command in fileCommands:
        if command[0].lower() == 'graph':
            graphs.append(Graph())
        elif command[0].lower() == 'vertex':
            newVertex = Vertex(command[1])
            InsertVertex(graphs[0], newVertex)

    graphs[0].showList()

main()