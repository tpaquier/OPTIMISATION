class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):


        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
                    """
       
        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
    

    def get_path_with_power(self, src, dest, power):
        raise NotImplementedError

    def dfs(self, node, visites=[], composantes=[]) :  
        visites.append(node) 
#on prend un point
        composantes.append(node)
        for i in self.graph[node] : 
            if i[0] not in visites :
                self.dfs(i[0], visites, composantes)  
                
#et on applique à nouveau la fonction pour qu elle visite tous les voisins des voisins etc...   


    def connected_components(self) :
        visites=[]
        gde_liste=[]
        for i in self.graph:
            if i not in visites :
                composantes=[]
                self.dfs(i, visites, composantes)
                gde_liste.append(composantes)
        return gde_liste
        

    def connected_components_set(self):


        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    '''
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        raise NotImplementedError
        '''

def graph_from_file(filename):
    file = open(filename, 'r')
    dist=1
    #First line is read in order to properly intialize our graph
    line_1 = file.readline().split(' ')
    new_graph = Graph([node for node in range(1,int(line_1[0])+1)])
    new_graph.nb_edges = int(line_1[1].strip('\n'))
    #Then, all lines are read to create a new edge for each line
    for line in file:
        list_line = line.split(' ')
        if list_line == []:
            continue
        if len(list_line) == 4:
            #In the case where a distance is included
            dist = int(list_line[3])
        new_graph.add_edge(int(list_line[0]), int(list_line[1]), int(list_line[2]),dist)
    print(new_graph.graph)
    file.close()
    return new_graph