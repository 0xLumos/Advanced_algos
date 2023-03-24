class Graph(object):
    
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        #print(self.adjMatrix)
        self.size = size
        self.vertex = []
        for i in range(2):
            self.vertex.append([i+1 for i in range(size)])
        #print(self.vertex)
        
    def add(self, v):                                   #add vertex function takes one argument v
        if v <= self.size:                              #if vertex is less or equal to size of matrix
            print("Already in use.")                    #give feedback
            print(self.vertex, self.adjMatrix)          #print vertex, adjacency matrix
        else:
            print(self.vertex[0])                       #print first element of vertex list
            for vertex in self.vertex:                  #loop through vertex array
                v = vertex[-1] + 1                      #v is the last vertex in self.vertex + 1, i.e if there are 6 the new vertex will be 7
                vertex.append(v)                        #add v
                #print(vertex)
                i = self.vertex[0]                      #set variable i to first index of vertex
                for i in vertex:                        #loop through vertex
                    print(i)                            #print i on each loop
                #self.vertex.append([+1])
            return 
        
    def addEdge(self, v1, v2):                          ##this should check weather the edge already exists
        if v1 == v2:                                    #function that takes two arguments vertcies and connects them
            print("Same vertex %d and %d" % (v1, v2))   #if the vertecies are equal, print can not initiate edge between same node
        self.adjMatrix[v1][v2] = 1                      #add edge between v1 and v2 
        self.adjMatrix[v2][v1] = 1                      #add edge between v2 and v1
    
     def remove_edge(self, v1, v2):                     #function remove edge takes two arguements v1 and v2 and removes the edge between them
        if self.adjMatrix[v1][v2] == 0:                 #if there is no edge
            print("No edge between %d and %d" % (v1, v2)) #give feedback
            return
        self.adjMatrix[v1][v2] = 0                      #else if there is an edge set it to zero (remove)
        self.adjMatrix[v2][v1] = 0                      #set the edge from the other way to null

    def __len__(self):
        return self.size                                #sub function that reurns size

                                                                         # Print the matrix
    def print_matrix(self):                             #function that prints out the matrix
        for row in self.adjMatrix:                      #loop through rows in adjMatrix array
            for val in row:                             #loop through values in row from adjMatrix
                print('{:4}'.format(val)),              #print matrix
            print
    
    #methods for (1) adding a vertex; (2) adding an edge; (3) removing an edge; and (4) printing the
    #matrix should appear here




#remember list indexing - this is 1 out, unless we start the matrix at 0 (not a +ve integer)     
def main():
        g = Graph(6)
        g.add(7)
        #g.add(8)
        #g.print_matrix(Graph(6))
        
        
if __name__ == '__main__':
    main()
