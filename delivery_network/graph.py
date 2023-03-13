class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.list_of_neighbours = []
        self.list_of_edges = []
        self.max_power = 0
    

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
        ancetres = self.bfs(src, dest, power) #ancetres est encore le dicitonnaire qui a comme clé un noeud et comme valeur 
        #celui par lequel on a pu parvenir à ce noeud.
        parcours = []
        #on crée une liste parcours qui nous donnera le parcours entre les deux noeuds choisis en respectant toujours la puissance 
        #exigée.
        a = dest #on renomme dest en a pour faciliter la suite.
        if a not in ancetres:
            return None
            #s'il n'y a pas de graphe connexe avec la puissance exigée, on retourne none.
        while a != src:
            #On met cette condition car on part de l'arrivée de notre bfs, donc on remonte point par point jusqu'à arriver à 
            #notre point de départ.
            parcours.append(a)
            a = ancetres[a]
            #on rajoute le sommet a à notre liste de noeuds parcourus et on définit "le nouveau" a comme étant son ancêtre pour
            #rebrousser chemin.
        parcours.append(src)
        #on doit ajouter l'origine a la main parce que notre boucle while s'arrête dès lors que a prend la valeur du noeud de départ
        #et ne le rajoute donc pas dans la liste.
        parcours.reverse()
        return parcours


    def dfs(self, node, visites, composantes, power=1000000000):  
    #on a rajouté une condition de puissance afin de pouvoir conditionner les chemins possible dans la question 
    #traitant de la puissance minimale à avoir pour un trajet. On met une valeur très importante par défaut pour 
    #éviter qu'il n'ampute des trajectoires possibles sur des graphes
        visites.append(node) 
    #on prend un point à partir duquel on veut commencer notre dfs et on l'ajoute à la liste 
    #visites qui conservera tous les noeuds déjà visités
        composantes.append(node)
    #la liste composantes n'est ici pas indispensable mais sera utile pour la question qui suit 
        for i in self.graph[node]: 
            if i[0] not in visites and power >= i[1]: 
                self.dfs(i[0], visites, composantes, power=power) 
                #ici est la recursion de la fonction. On lui demande de s'appliquer elle-même à chaque noeud qui n'est pas 
                #encore présent dans la liste "visites". On rajoute également une condition sur la puissance lorsque cela est nécessaire. 
        return visites
                
#et on applique à nouveau la fonction pour qu elle visite tous les voisins des voisins etc...   

    def connected_components(self) :
        visites = []
        gde_liste = []
        #on crée une grande liste qui sera une liste de liste de tous les noeuds reliés. C'es-à-dire que chaque liste 
        #présente dans la liste soit un graphe connexe avec tous les noeuds qu'elle contient. 
        for i in self.graph:
            if i not in visites:
                composantes=[]
                #on a donc ici la liste de compostantes qui se reset à chaque itération tandis que la liste de visites
                #reste inchangé. 
                #Comme on parcours chaque noeud et que visites garde en mémoire tous les noeuds qui ont été visités,
                #on a donc une nouvelle liste qui se crée qu'à condition qu'il n'y ait aucuun noeud dans une précédente liste.
                self.dfs(i, visites, composantes)
                gde_liste.append(composantes)
        return gde_liste
        
    def bfs(self, beg, dest, power=-1):
        ancetres = {}
        #le dictionnaire ancetres est le dicitonnaire qui permet d'avoir le lien entre chaque sommet, c'est-à-dire que la clé est le 
        #sommet en question et sa valeur est le noeud par lequel on est arrivés. 
        queue = []
        visited = set()
        #on fait un set pour les noeuds visités pour éviter d'avoir des boucles étant donné que le set ne gardera
        #qu'une fois chaque noeud. 
        queue.append(beg)
        while len(queue) > 0:
            n = queue.pop()
            #le while est conditionné par la longueur de la queue du fait de l'utilisation de pop. Comme on a une queue on supprime le 
            #dernier élément de cette liste pour chercher les autres sommets. 
            for v in self.graph[n]:
                if v[0] not in visited and power >= v[1]:
                    #on garde la condition dans les visites pour ne pas faire de boucle et on rajoute celle sur la puissance pour coller
                    #aux conditions de base. De la sorte, on considère qu'il n'y a pas d'arêtes si la puissance de celle-ci
                    #est supérieure à la puissance donnée comme paramètre. 
                    queue.append(v[0])
                    #on rajoute tous les voisins du noeud en question à la liste de queue pour avoir tous les chemins
                    ancetres[v[0]] = n
                    #on définit la valeur comme le noeur à partir duquel on est arrivés.
                    visited.add(v[0])
                    #et on le rajoute au set des visites comme pour éviter les boucles.
        return ancetres


    def BS(self, liste, power):
        #code de BS "de base" utilisé pour avoir une idée de comment coder le binary search de min_power
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

    def power_nodes(self, node1, node2): #fonction un peu inutile utilisée à des fins d'entraînement
        liste = self.graph[node1]
        for i in liste:
            if i[1] == node2:
                power = i[3]
        return power
    



    def min_power(self, src, dest):
        debut = 1
        fin = self.max_power
        if dest not in self.dfs(src, [], []):
            return None, None
        #si les deux noeuds en question ne sont pas sur un graphe connexe, on retourne none car il n'y a pas de chemins possible. 
        while debut != fin: 
            #on fait une recherche binaire. 
            #Pour être tout à fait honnête, la condition sur le while est un peu désuète étant donné qu'on fait un break
            #avant que cette condition puisse se remplir mais c'est la solution qui a le mieux marché sur plusieurs tests : 
            #network.1 et network.2, lentement mais sûrement.
            mid = ((debut+fin)//2)
            actu=self.dfs(src, [], [], power=mid)
            #on actualise à chaque itération le graphe des sommets formant un graphe connexe et permettant un chemin. 
            if dest in actu:
                fin = mid
            #si le sommet qu'on veut atteindre est dans le graphe fait à partir de la médiane des puissances
            #on redéfinit la "borne sup" comme étant l'ancien milieu pour retrécir notre champ de recherche.
            elif dest not in actu:
                debut=mid
            #on procède pareillement mais avec la plus petite puissance dans le cas contraire.
            if fin-debut == 1 :
                break
            #Comme on ne prend pas comme valeurs de power les puissances présentes dans le graphe mais simplement 
            #les entiers situés entre la plus grande puissance et la plus petite, 
            #la condition pour sortir de la boucle while est que la différence entre les deux extrêmes soit égale à un. 
            #Ainsi, cela signifierait que ce sont deux entiers qui se suivent et on doit donc nécessairement prendre 
            #"fin" car début serait trop petit. 
        minus=fin
        return self.get_path_with_power(src, dest, minus), minus


    """
        def connected_components_set(self):
        return set(map(frozenset, self.connected_components()))
    """
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
            min = i 
        if i > min:
            min = min
    return min

def connected_components_set(self):


        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))

