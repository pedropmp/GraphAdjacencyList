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
    def __init__(self, id, index=None):
        self.id = str(id)
        self.neighbors = []
        self.index = index
        self.color = None
        self.d = None
        self.pi = None

    def __str__(self):
        return "{}".format(self.id)
    
# ----- END OF VERTEX CLASS -----


# ----- GRAPH CLASS -----
'''
Graph is a data structure of Vertices and an adjacency list or matrix of adjacencies
'''
class Graph:
    def __init__(self, id, graphType):
        self.id = id
        self.adjList = []  #adjList is a list of heads (first vertex/node of a linked list)
        self.list = None
        if graphType.lower() == 'adjlist':
            self.list = True
        elif graphType.lower() ==  'adjmatrix':
            self.list = False

        self.adjMatrix = [] # stores if there is or there isn't an edge between two vertices 
        self.numberVertices = 0 # stores the number of vertices in order to specify a certain array index for each vertex
        self.vertices = [] # stores all vertices 


    '''Graph method that shows adjacency list and its linked lists'''
    def ShowList(self):
        if self.list:
            print('\n----- Adjacency list -----')
            for vertex in self.adjList:
                print('{}'.format(vertex), end=' -> ')
                for neighbor in vertex.neighbors:
                    print('{}'.format(neighbor), end=' -> ')
                print('none')
            print('')

        else:
            print('\n{}'.format('----- Adjacency matrix -----'))
            print('{0: ^8}'.format(' '), end=' ')
            for vertex in self.vertices:
                print('{0: ^8}'.format(str(vertex)), end=' ')
            print('')

            for lineIndex in range(0, len(self.adjMatrix)):
                print('{0: ^8}'.format(str(self.vertices[lineIndex])), end=' ')
                for edge in self.adjMatrix[lineIndex]:
                    print('{0: ^8}'.format(str(edge)), end=' ')
                print('')
            print('')

                

    '''
    Graph method that creates an Node, where the Vertex and adds a new index in the adjacency matrix.
    The node created does not have any edges from or to it.
    '''
    def InsertVertex(self, vertexId):
        if self.list:
            self.adjList.append(Vertex(vertexId))
        else:
            self.vertices.append(Vertex(vertexId, self.numberVertices))
            self.numberVertices += 1
            if len(self.adjMatrix) > 0:
                for line in self.adjMatrix:
                    line.append(0)
            self.adjMatrix.append([0]*self.numberVertices)


    '''Graph method that removes a vertex calling remove edge for its edges and then removing the 
    vertex itself'''
    def RemVertex(self, vertexId):
        if self.list:
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
        else:
            deleted = False
            for vertex in list(self.vertices):
                #deleting edges from vertex or bidirectional edges
                if vertex.id == vertexId:
                    del self.adjMatrix[vertex.index]
                    for i in range(0, len(self.adjMatrix)):
                        del self.adjMatrix[i][vertex.index]
                    self.numberVertices -= 1
                    self.vertices.remove(vertex)
                    print('{} vertex deleted.\n'.format(vertexId))
                    deleted = True
                else: 
                    if deleted:
                        vertex.index -= 1


    '''Graph method that searches for both vertices and updates its neighbors list adding a new neighbor
    due to edge creation'''
    def InsertEdge(self, vertexId1, vertexId2):
        if self.list:
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
        else:
            # search for first vertex
            for first_vertex in self.vertices:
                if str(first_vertex.id) == vertexId1:
                    # search for second vertex
                    for second_vertex in self.vertices:
                        if str(second_vertex.id) == vertexId2:
                            print('Both vertices found.', end=' ')
                            if directed or vertexId1 == vertexId2:
                                self.adjMatrix[first_vertex.index][second_vertex.index] = 1
                                print('Edge {} -> {} created.'.format(vertexId1, vertexId2))
                            else:
                                self.adjMatrix[first_vertex.index][second_vertex.index] = 1
                                self.adjMatrix[second_vertex.index][first_vertex.index] = 1
                                print('Edge {} <-> {} created.'.format(vertexId1, vertexId2))
                            sleep(.5)


    '''Graph method that searches for two vertices and if they exist in the adjacency list, their neighbor's list
    updated removing one from another's list, thus excluding the edge between them'''
    def RemEdge(self, vertexId1, vertexId2):
        if self.list:
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
        else:
            # search for first vertex
            for first_vertex in self.vertices:
                if str(first_vertex.id) == vertexId1:
                    # search for second vertex
                    for second_vertex in self.vertices:
                        if str(second_vertex.id) == vertexId2:
                            print('Both vertices found.')
                            if directed:
                                print('Deleting edge {} -> {}...'.format(vertexId1, vertexId2), end= ' ')
                                sleep(.5)
                                self.adjMatrix[first_vertex.index][second_vertex.index] = 0
                                print('Not a neighbor anymore.')
                                sleep(.5)

                            else:
                                print('Deleting edge {} -> {}...'.format(vertexId1, vertexId2), end= ' ')
                                sleep(.5)
                                self.adjMatrix[first_vertex.index][second_vertex.index] = 0
                                print('Not a neighbor anymore.')
                                sleep(.5)
                                
                                print('Deleting edge {} -> {}...'.format(vertexId2, vertexId1), end= ' ')
                                sleep(.5)
                                self.adjMatrix[second_vertex.index][first_vertex.index] = 0
                                print('Not a neighbor anymore.')
                                sleep(.5)
                            break

    '''Auxiliary method for the RemEdge method. This will search by a neighbor and pop it from the neighbor's list
    of the vertex object passed as argument'''
    def RemNeighbor(self, vertex_obj, neighbor):
        if self.list:
            for i in range(0, len(vertex_obj.neighbors)):
                if vertex_obj.neighbors[i] == neighbor:
                    vertex_obj.neighbors.pop(i)
                    print('Not a neighbor anymore.')
                    sleep(.5)
                    break

    '''This graph method identifies the sources and sinks in the and shows its ids'''
    def SourcesSinks(self):
        if self.list:
            sources = []
            for vertex in self.adjList:
                sources.append(vertex)
            sinks = []
            for vertex in self.adjList:
                # outdegree zero
                if len(vertex.neighbors) < 1:
                    sinks.append(vertex)
                else:
                    # indegree zero
                    for neighbor in vertex.neighbors:
                        if neighbor in sources:
                            sources.remove(neighbor)

        else:
            sources = []
            sinks = []
            indegreeCounter = [0]*len(self.vertices)
            for lineIndex in range(0, len(self.adjMatrix)):
                # outdegree zero
                if self.adjMatrix[lineIndex].count(1) == 0:
                    for vertex in self.vertices:
                        if vertex.index == lineIndex:
                            sinks.append(vertex)

                for targetIndex in range(0, len(self.adjMatrix[lineIndex])):
                    # hit counter
                    if self.adjMatrix[lineIndex][targetIndex] == 1:
                        indegreeCounter[targetIndex] += 1
            
            for targetIndex in range(0, len(indegreeCounter)):
                # no hit condition, indegree zero
                if indegreeCounter[targetIndex] == 0:
                    for vertex in self.vertices:
                        if vertex.index == targetIndex:
                            sources.append(vertex)

        print('----- Sources and sinks -----\nSources: ', end='')
        for source in sources:
            print(source, end=' ')
        print('')
        
        print('Sinks: ', end='')
        for sink in sinks:
            print(sink, end=' ')
        print('\n')

    '''This graph method counts the indegree and outdegree for a certain vertex'''
    def VertexDegree(self, vertexId):
        if self.list:
            indegree = 0
            outdegree = None
            for vertex in self.adjList:
                if vertex.id == vertexId:
                    outdegree = len(vertex.neighbors)
                else:
                    for neighbor in vertex.neighbors:
                        if neighbor.id == vertexId:
                            indegree += 1

        else:
            indegree = 0
            outdegree = None
            for vertex in self.vertices:
                if vertex.id == vertexId:
                    outdegree = self.adjMatrix[vertex.index].count(1)
                    for line in self.adjMatrix:
                        if line[vertex.index] == 1:
                            indegree += 1
            
        print('----- Vertex {} degree -----'.format(vertexId))
        print('Indegree: {}\nOutdegree: {}'.format(indegree, outdegree))


    def MatrixToList(self):
        # adding  vertices to adjacency list
        for i in range(0, len(self.vertices)):
            self.adjList.append(self.vertices.pop(0))

        # add neighbors for each vertex added to the adjacency list
        for vertex in self.adjList:
            # search for the respective vertex line index in the adjacency matrix
            for lineIndex in range(0, len(self.adjMatrix)):
                if lineIndex == vertex.index:
                    # search for target positions in the line that have 1 assigned to them
                    for targetIndex in range(0, len(self.adjMatrix[lineIndex])):
                        if self.adjMatrix[lineIndex][targetIndex] == 1:
                            # search for the vertex that has same index as the target
                            for otherVertex in self.adjList:
                                if otherVertex.index == targetIndex:
                                    vertex.neighbors.append(otherVertex)
                                    break # break after finding the target vertex
                    break # break after finding the right line of the matrix
        
        for vertex in self.adjList:
            vertex.index = None
        self.list = True
        self.adjMatrix = []


    def ListToMatrix(self):
        i = 0
        self.adjMatrix = []
        self.vertices = []
        for vertex in self.adjList:
            # creating adjacency matrix filled of zeros
            line = [0]*len(self.adjList)
            self.adjMatrix.append(line)

            # giving each vertex its index for the matrix representation
            vertex.index = i
            i += 1
        
        for vertex in self.adjList:
            for neighbor in vertex.neighbors:
                self.adjMatrix[vertex.index][neighbor.index] = 1
        
        for vertex in self.adjList:
            vertex.neighbors = []

        for vertex in list(self.adjList):
            self.vertices.append(self.adjList.pop(0))

        del self.adjList[:]
        self.adjList = []
        self.list = False


    def BFS(self, vertexId):
        if self.list:
            # setting up vertices for search
            queue = []
            for vertex in self.adjList:
                if vertex.id == vertexId:
                    vertex.color = 'gray'
                    vertex.d = 0
                    vertex.pi = None
                    queue.append(vertex)
                else:
                    vertex.color = 'white'
                    vertex.d = 1000
                    vertex.pi = None
            
            print('\nQueue: ', end= ' ')
            for vertex in queue:
                print(vertex, end=' ')
            print('')
            print('----- Graph colors -----')
            for vertex in self.adjList:
                print('{0: ^8}'.format(vertex.id), end= ' ')
            print('')
            for vertex in self.adjList:
                print('{0: ^8}'.format(vertex.color), end= ' ')
            print('')
            for vertex in self.adjList:
                    print('{0: ^8}'.format(vertex.d), end= ' ')
            print('')

            while queue:
                vertex = queue.pop(0)
                for neighbor in vertex.neighbors:
                    if neighbor.color == 'white':
                        neighbor.color = 'gray'
                        neighbor.d = vertex.d + 1
                        neighbor.pi = vertex
                        queue.append(neighbor)
                vertex.color = 'black'

                print('\nVertex: {}'.format(vertex))
                print('Queue: ', end= ' ')
                for vertex in queue:
                    print(vertex, end=' ')
                print('')
                print('----- Graph colors -----')
                for vertex in self.adjList:
                    print('{0: ^8}'.format(vertex.id), end= ' ')
                print('')
                for vertex in self.adjList:
                    print('{0: ^8}'.format(vertex.color), end= ' ')
                print('')
                for vertex in self.adjList:
                    print('{0: ^8}'.format(vertex.d), end= ' ')
                print('')


# ----- END OFGRAPH CLASS -----


# ----- MAIN FUNCTIONS -----


'''This functions creates a new graph object and adds it to the global list of graphs'''
def NewGraph(id, graphType):
    graphs.append(Graph(id, graphType))


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
            print('Graph found. Creating new edge...', end=' ')
            graph.InsertEdge(vertexId1, vertexId2)


'''This function tries to delete an edge between two vertices given its id's'''
def DelEdge(graphId, vertexId1, vertexId2):
    for graph in graphs:
        if graph.id == graphId:
            print('Graph found. Searching vertices(s)...', end= ' ')
            graph.RemEdge(vertexId1, vertexId2)


'''This function will call for the showlist method of the graph class given a certain graph and given
that it is in the global list of graphs'''
def ShowGraph(graphId):
    for graph in graphs:
        if graph.id == graphId:
            graph.ShowList()    

'''This function will call for the graph method SourcesSinks given a graph'''
def ShowSourceSinks(graphId):
    for graph in graphs:
        if graph.id == graphId:
            graph.SourcesSinks()

'''This function will calll for the VertexDegree graph method given a graph'''
def ShowVertexDegree(graphId, vertexId):
    for graph in graphs:
        if graph.id == graphId:
            graph.VertexDegree(vertexId)


'''This function calls the graph method that changes the graph representation from matrix to list of
adjacency'''
def ConfigMatrixToList(graphId):
    for graph in graphs:
        if graph.id == graphId:
            graph.MatrixToList()

    
'''This function calls the graph method that changes the graph representation from list to matrix of
adjacency'''
def ConfigListToMatrix(graphId):
    for graph in graphs:
        if graph.id == graphId:
            graph.ListToMatrix()


def CallBFS(graphId, vertexId):
    for graph in graphs:
        if graph.id == graphId:
            graph.BFS(vertexId)

'''This function opens, reads and closes the entrada.txt input file. 
After reading it, it produces de fileCommands global list, wich contains
a list of lists with commands and names for the instances of the classes.'''
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
    system('cls')
    newFile.close()
 
'''This function can be used to clear the terminal screen'''
def clear():
    pass
    if name == 'nt':
        system('cls')
    elif name == 'posix':
        system('clear')

'''This function reads a command and calls for a specific function'''
def menu():
    global directed
    for command in fileCommands:
        if command[0].lower() == 'graph':
            NewGraph(command[1], command[2])
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
        elif command[0].lower() == 'configmatrixtolist':
            ConfigMatrixToList(command[1])
        elif command[0].lower() == 'configlisttomatrix':
            ConfigListToMatrix(command[1])
        elif command[0].lower() == 'bfs':
            CallBFS(command[1], command[2])
            

# ----- END OF MAIN FUNCTIONS -----


# ----- MAIN -----

def main():
    CommandInput()
    global graphs
    graphs = []
    menu()


main()

# ----- END OF MAIN -----
