import copy

class GrafMatriu:
    def __init__(self, ln:int ,lv=[],lp=[]):
        self._nodes = copy.deepcopy(list(range(1,ln+1)))
        self._numNodes = ln
        self._matriuAdj = [ [0] * self._numNodes for j in range(self._numNodes ) ]
        self._numEdges = 0 
        if lp==[]:
            self._ponderat = 0
            for v in lv:
                indNod1 =self._nodes.index(v[0])
                indNod2 =self._nodes.index(v[1])
                self.insert_edge(indNod1, indNod2)
        else:
            self._ponderat = 1
            for v,p in zip(lv,lp):
                indNod1 =self._nodes.index(v[0])
                indNod2 =self._nodes.index(v[1])
                self.insert_edge(indNod1, indNod2, p)

    def insert_edge(self, u, v,p=1):
        if (0<=u<self._numNodes) and (0<=v<self._numNodes):
            if (self._matriuAdj[u][v] == 0):
                self._numEdges += 1
                self._matriuAdj[u][v] = p
                self._matriuAdj[v][u] = p

    def insert_vertex(self, x=None):
        self._nodes.append(x)
        for j in range(self._numNodes):
            self._matriuAdj[j].append(0)
        self._numNodes += 1
        self._matriuAdj.append([0]*self._numNodes)

    def vertices(self):
        return self._nodes.__iter__( )
    def edges(self, v):
        for col in range(0,self._numNodes):
            if (self._matriuAdj[v][col]==1):
                yield (self._nodes[v], self._nodes[col])

    def cicles(self):
        p_cicles = []
        for fil in range(0,self._numNodes):
            for col in range(fil+1,self._numNodes):
                if (self._matriuAdj[fil][col] != 0):
                    for vei in range(col+1,self._numNodes):
                        if ((self._matriuAdj[fil][vei] != 0) and (self._matriuAdj[col][vei] != 0)):
                            p_cicles.append([self._nodes[fil],self._nodes[col],self._nodes[vei]])
        return p_cicles


'''def minTrioDegree(n: int, edges: list[list[int]]) -> int:
    
    G=GrafMatriu(n,edges)
    cicles= G.cicles()
    graus=[]
    for cicle in cicles:
        grau=0
        for num in cicle:
            for vei in G.edges(G._nodes.index(num)):
                if vei[0] not in cicle or vei[1] not in cicle:
                    grau+=1
        graus.append(grau) 
    if graus:
        return min(graus)
    else:
        return -1'''
def minTrioDegree(n: int, edges: list[list[int]]) -> int:
    
    G=GrafMatriu(n,edges)
    cicles= G.cicles()
    graus=[]
    graus_nodes = [sum(fila) for fila in G._matriuAdj]
    for cicle in cicles:
        g1 = graus_nodes[cicle[0] - 1] - 2
        g2 = graus_nodes[cicle[1] - 1] - 2
        g3 = graus_nodes[cicle[2] - 1] - 2
        grau = g1 + g2 + g3
        graus.append(grau) 
    if graus:
        return min(graus)
    else:
        return -1

print(minTrioDegree(6, [[1, 2], [1, 3], [2, 3], [1, 4], [2, 5], [3, 6], [4, 5], [5, 6]]))

print(minTrioDegree(7, [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 6], [6, 4], [6, 7]]))