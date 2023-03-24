import sys                                                                                      #needed for maxsize

class Graph(): 
  
    def __init__(self, vertices):                                                               #implements graph as adjacency matrix
        self.V = vertices                                                                       #number of vertices
        self.graph = [[0 for column in range(vertices)]                                         #adjacency matrix with no edges (all connections set to zero)
                    for row in range(vertices)] 
  
    def printMST(self, parent): 
        print ("Edge \t Weight")
        for i in range(1, self.V): 
            print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ])
  
                                                                                                #from reached nodes find the unreached node with the minimum cost
    def minKey(self, key, mstSet): 
        min = sys.maxsize                                                                       #set min to infinity (use maxsize which is next best thing!)
        for v in range(self.V):                                                                 #count through number of vertices
            if key[v] < min and mstSet[v] == False:                                             #if vertex is less than min and unreached
                min = key[v]                                                                    #assign to min 
                min_index = v                                                                   #min_index is position of min in key
        return min_index                                                                        #return min_index
  
                                                                                                #find MST 
    def primMST(self): 
        key = [sys.maxsize] * self.V                                                            #initialise key to list of values all set to infinity; same length as self.V              
        parent = [None] * self.V                                                                #list for constructed MST 
        key[0] = 0                                                                              #set first element of key to zero (this is where we start)                                                                                   
        mstSet = [False] * self.V                                                               #mstSet is list of booleans set to False
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:   # the set of vertices not yet processed. 
                    key[v] = self.graph[u][v]                                                      # u is always equal to src in first iteration
                    parent[v] = u
  
                                                                                                # Put the minimum distance vertex in 
                                                                                                # the shortest path tree
            
                                                                                                # Update dist value of the adjacent vertices 
                                                                                                # of the picked vertex only if the current 
                                                                                                # distance is greater than new distance and
                                                                                                # the vertex in not in the shotest path tree
                                                                                                # Pick the minimum distance vertex from
                                                                                                # the vertex in not in the shotest path tree
                                                                                                # graph[u][v] is non zero only for adjacent vertices of m
                                                                                                # mstSet[v] is false for vertices not yet included in MST
                                                                                                  # Update the key only if graph[u][v] is smaller than key[v]
        self.printMST(parent)
                               
g = Graph(5)
g.graph =  [[0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
g.primMST()