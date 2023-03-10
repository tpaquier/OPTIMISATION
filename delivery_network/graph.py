class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.list_of_neighbours = []
        self.list_of_edges = []
        self.max_power =0
    

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
        ancetres = self.bfs(src, dest, power)
        parcours=[]
        a=dest
        if dest not in ancetres:
            return None
        while a != src:
            parcours.append(a)
            a=ancetres[a]
            print("dans la boucle", parcours)
        parcours.append(src)
        parcours.reverse()
        print("resultat", parcours)
        return parcours

        












        #for i in ancetres:
            #infos = self.graph[i]
            #for v in infos : 
                #if v[2]>power : 
                    #return None
                #if v[2]<=power : 
                    #return ancetres


    def dfs(self, node, visites=[], composantes=[], power=-1) :  
        visites.append(node) 
    #on prend un point
        composantes.append(node)
        for i in self.graph[node] : 
            if i[0] not in visites and power!=-1:
                continue
                self.dfs(i[0], visites, composantes) 
        return visites
                
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
        
    def bfs(self, beg, dest, power=-1):
        ancetres={}
        queue=[]
        visited=set()
        queue.append(beg)
        while len(queue)>0:
            n = queue.pop()
            for v in self.graph[n]:
                if v[0] not in visited and power>=v[1]:
                    queue.append(v[0])
                    ancetres[v[0]]=n
                    visited.add(v[0])
        return ancetres


    def BS(self, liste, power):
        haut = len(liste)-1
        bas = 0
        mid = 0
        while bas <= haut:
            mid = (haut+bas)//2
            if liste[mid] < power:
                bas = mid+1
            elif liste[mid] > power:
                haut = mid-1
            elif liste[mid] == power:
                return mid
        return -1 #si on arrive la c est que l element etait po dans la liste

             


    def power_nodes(self, node1, node2):
        liste=self.graph[node1]
        for i in liste :
            if i[1] == node2 :
                power = i[3]
        return power
            

    def min_power(self, src, dest):
        debut=0
        fin=self.max_power
        if dest not in self.dfs(src):
            return None
        while debut != end: 
            mid = (debut+fin)//2
            if dest not in self.dfs(src, mid):
                debut=mid
            else:
                fin=mid
            if fin-debut == 1:
                fin=debut
        minus=fin
        print("la plus petiote puissance pour le chemin est : "+minus)
        #print("le chemin qui marche bien est :"+self.get_path_with_power(src, dest, minus))







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
    """
    Reads a text file and returns the graph as an object of the Graph class.
    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.
    Parameters: 
    -----------
    filename: str
        The name of the file
    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    #start = time.perf_counter()
    file = open(filename, 'r')
    dist=1
    #First line is read in order to properly intialize our graph
    line_1 = file.readline().split(' ')
    total_nodes = int(line_1[0])
    nb_edges = int(line_1[1].strip('\n'))
    new_graph = Graph([node for node in range(1,total_nodes+1)])
    new_graph.nb_edges = nb_edges
    new_graph.list_of_edges = [None]*nb_edges
    #Then, all lines are read to create a new edge for each line
    for line in file:
        list_line = line.split(' ')
        start_node = int(list_line[0])
        end_node = int(list_line[1])
        power = int(list_line[2])
        if list_line == []:
            continue
        if len(list_line) == 4:
            #In the case where a distance is included
            dist = int(list_line[3])
        new_graph.max_power = max(new_graph.max_power, power)
        new_graph.add_edge(start_node, end_node, power, dist)
    new_graph.list_of_neighbours = [list(zip(*new_graph.graph[node]))[0] for node in new_graph.nodes if new_graph.graph[node]!=[]]
    #stop = time.perf_counter()
    #print(stop-start)
    file.close()
    return new_graph





def minimum(self, liste):
    min = 0
    for i in liste:
        if i <= min:
            min=i
        if i > min:
            min=min
    return min