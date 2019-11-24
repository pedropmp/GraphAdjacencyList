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
        self.id = str(id)
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


    '''Graph method that shows adjacency list and its linked lists'''
    def ShowList(self):
        print('\n----- Adjacency list -----')
        for vertex in self.adjList:
            print('{}'.format(vertex), end=' -> ')
            for neighbor in vertex.neighbors:
                print('{}'.format(neighbor), end=' -> ')
            print('none')
            sleep(.5)
        print('')
        sleep(1)
                

    '''
    Graph method that creates an Node, where the Vertex and adds a new index in the adjacency matrix.
    The node created does not have any edges from or to it.
    '''
    def InsertVertex(self, vertexId):
        self.adjList.append(Vertex(vertexId))


    '''Graph method that removes a vertex calling remove edge for its edges and then removing the 
    vertex itself'''
    def RemVertex(self, vertexId):
        for vertex in self.adjList:
            #deleting edges from vertex or bidirectional edges
            if vertex.id == vertexId:
                for neighbor in vertex.neighbors:
                    self.RemEdge(vertexId, neighbor.id)
            else:
                #deleting edges to vertex
                if directed:
                    for neighbor in vertex.neighbors:
                        if neighbor.id == vertexId:
                            self.RemNeighbor(vertex, neighbor)

        for i in range(0, len(self.adjList)):
            if str(self.adjList[i].id) == vertexId:  # needed to use str so that the interpreter could compare the strings
                self.adjList.pop(i)
                print('{} vertex deleted.\n'.format(vertexId))
                break

    '''Graph method that searches for both vertices and updates its neighbors list adding a new neighbor
    due to edge creation'''
    def InsertEdge(self, vertexId1, vertexId2):
        # search for first vertex
        for first_vertex in self.adjList:
            if str(first_vertex.id) == vertexId1:
                # search for second vertex
                for second_vertex in self.adjList:
                    if str(second_vertex.id) == vertexId2:
                        print('Both vertices found.', end=' ')
                        if directed or vertexId1 == vertexId2:
                            first_vertex.neighbors.append(second_vertex)
                            print('Edge {} -> {} created.'.format(vertexId1, vertexId2))
                        else:
                            first_vertex.neighbors.append(second_vertex)
                            second_vertex.neighbors.append(first_vertex)
                            print('Edge {} <-> {} created.'.format(vertexId1, vertexId2))
                        sleep(.5)


    '''Graph method that searches for two vertices and if they exist in the adjacency list, their neighbor's list
    updated removing one from another's list, thus excluding the edge between them'''
    def RemEdge(self, vertexId1, vertexId2):
        # search for first vertex
        for first_vertex in self.adjList:
            if str(first_vertex.id) == vertexId1:
                # search for second vertex
                for second_vertex in self.adjList:
                    if str(second_vertex.id) == vertexId2:
                        print('Both vertices found.')
                        if directed:
                            print('Deleting edge {} -> {}...'.format(vertexId1, vertexId2), end= ' ')
                            sleep(.5)
                            self.RemNeighbor(first_vertex, second_vertex)
                        else:
                            print('Deleting edge {} -> {}...'.format(vertexId1, vertexId2), end= ' ')
                            sleep(.5)
                            self.RemNeighbor(first_vertex, second_vertex)

                            print('Deleting edge {} -> {}...'.format(vertexId2, vertexId1), end= ' ')
                            sleep(.5)
                            self.RemNeighbor(second_vertex, first_vertex)
                        break

    '''Auxiliary method for the RemEdge method. This will search by a neighbor and pop it from the neighbor's list
    of the vertex object passed as argument'''
    def RemNeighbor(self, vertex_obj, neighbor):
        for i in range(0, len(vertex_obj.neighbors)):
            if vertex_obj.neighbors[i] == neighbor:
                vertex_obj.neighbors.pop(i)
                print('Not a neighbor anymore.')
                sleep(.5)
                break


    def SourcesSinks(self):
        sources = []
        for vertex in self.adjList:
            sources.append(vertex)
        sinks = []
        for vertex in self.adjList:
            # grau de saida zero
            if len(vertex.neighbors) < 1:
                sinks.append(vertex)
            else:
                # grau de entrada zero
                for neighbor in vertex.neighbors:
                    if neighbor in sources:
                        sources.remove(neighbor)

        print('----- Sources and sinks -----\nSources: ', end='')
        for source in sources:
            print(source, end=' ')
        print('')
        
        print('Sinks: ', end='')
        for sink in sinks:
            print(sink, end=' ')
        print('\n')


    def VertexDegree(self, vertexId):
        indegree = 0
        outdegree = None
        for vertex in self.adjList:
            if vertex.id == vertexId:
                outdegree = len(vertex.neighbors)
            else:
                for neighbor in vertex.neighbors:
                    if neighbor.id == vertexId:
                        indegree += 1
        
        print('----- Vertex {} degree -----'.format(vertexId))
        print('Indegree: {}\nOutdegree: {}'.format(indegree, outdegree))



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
    sleep(1)
    for graph in graphs:
        if graph.id == graphId:
            graph.RemVertex(vertexId) #calling graph remove vertex method

'''This function will try to create an edge between two vertices'''
def NewEdge(graphId, vertexId1, vertexId2):
    for graph in graphs:
        if graph.id == graphId:
            print('Graph found. Creating new edge...', end=' ')
            sleep(.5)
            graph.InsertEdge(vertexId1, vertexId2)

'''This function tries to delete an edge between two vertices given its id's'''
def DelEdge(graphId, vertexId1, vertexId2):
    for graph in graphs:
        if graph.id == graphId:
            print('Graph found. Searching vertices(s)...', end= ' ')
            sleep(.5)
            graph.RemEdge(vertexId1, vertexId2)

'''This functions creates a new graph object and adds it to the global list of graphs'''
def NewGraph(id):
    graphs.append(Graph(id))

'''This function will call for the showlist method of the graph class given a certain graph and given
that it is in the global list of graphs'''
def ShowGraph(graphId):
    for graph in graphs:
        if graph.id == graphId:
            graph.ShowList()    


def ShowSourceSinks(graphId):
    for graph in graphs:
        if graph.id == graphId:
            graph.SourcesSinks()


def ShowVertexDegree(graphId, vertexId):
    for graph in graphs:
        if graph.id == graphId:
            graph.VertexDegree(vertexId)

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
    print('\n')
    sleep(2)
    system('cls')
    newFile.close()
 

def clear():
    pass
    if name == 'nt':
        system('cls')
    elif name == 'posix':
        system('clear')


def menu():
    global directed
    for command in fileCommands:
        if command[0].lower() == 'graph':
            NewGraph(command[1])
        elif command[0].lower() == 'vertex':
            NewVertex(command[1], command[2])
        elif command[0].lower() == 'delvertex':
            DelVertex(command[1], command[2])
        elif command[0].lower() == 'edge':
            NewEdge(command[1], command[2], command[3])
        elif command[0].lower() == 'deledge':
            DelEdge(command[1], command[2], command[3])
        elif command[0].lower() == 'show':
            ShowGraph(command[1])
        elif command[0].lower() == 'directedgraph':
            directed = True
        elif command[0].lower() == 'bidirectedgraph':
            directed = False
        elif command[0].lower() == 'sourcessinks':
            ShowSourceSinks(command[1])
        elif command[0].lower() == 'degree':
            ShowVertexDegree(command[1], command[2])

# ----- END OF MAIN FUNCTIONS -----


# ----- MAIN -----

def main():
    CommandInput()
    global graphs
    graphs = []
    menu()


main()

# ----- END OF MAIN -----
