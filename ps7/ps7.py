import sys
import math

def find_components(G):
    component = [None for _ in G.G]
    count = -1
    def dfs(u):
        if component[u] == None:
            component[u] = count
            for v in range(len(G.G[u])):
                if G.G[u][v] != None:
                    dfs(v)

    for i in range(len(G.G)):
        if component[i] == None:
            count += 1
            dfs(i)

    return component

"""
add safe edges between nodes
excluding nodes that are both on the ground
"""
def get_safe_edges(G, C):
    num_c = max(C) + 1
    best_edge = [(-1, -1, sys.maxsize) for _ in range(num_c)]

    # find components, then determine the best edge out of them
    for u,v,wt in G.get_edges():
        Cu = C[u]
        Cv = C[v]
        if Cu == Cv: 
            continue
        if wt < best_edge[Cu][2]:
            best_edge[Cu] = (u, v, wt)
        if wt < best_edge[Cv][2]:
            best_edge[Cv] = (u, v, wt)
    
    return best_edge

def add_safe_edges(F, safe):
    for u,v,wt in safe:
        if not F.has_edge(u, v):
            F.add_edge_wt(u, v, wt)

def boruvka(G, F):
    MAX_EDGES = 2 * (len(G.G) - 1)
    components = [sys.maxsize]

    while max(components) + 1 != 1:
        components = find_components(F)
        
        safe_edges = get_safe_edges(G, components)

        add_safe_edges(F, safe_edges)

    return F


class graph:
    G = None

    # build adjacency matrix with n nodes, and no edges
    def __init__(self, n):
        self.G = [ [None]*n for _ in range(n) ]

    def add_edge(self, u, v , uX, uY, vX, vY):
        dist = math.sqrt( (uX - vX)**2 + (uY - vY)**2 )

        self.G[u][v] = dist
        self.G[v][u] = dist

    def add_edge_wt(self, u, v, wt):
        self.G[u][v] = wt
        self.G[v][u] = wt

    def print(self):
        for i in range(len(self.G)):
            print(self.G[i])

    def get_edges(self):
        edges = []
        for i in range(len(self.G)):
            for j in range(len(self.G)):
                if i != j and self.G[i][j] != None:
                    edge = (i, j, self.G[i][j])
                    edges.append(edge)
        return edges

    def has_edge(self, u, v):
        if self.G[u][v] != None:
            return True
        else:
            return False

    def get_length(self):
        length = 0
        for i in range(len(self.G)):
            for j in range(len(self.G)):
                dist = self.G[i][j]
                if dist != None:
                    length += dist
        return length / 2
        

def main():
    firstLine = input().split()
    n, e, p = int(firstLine[0]), int(firstLine[1]), int(firstLine[2])


    g = graph(n) # dense graph that we will prune
    f = graph(n) # graph that we start with

    loc = []
    for i in range(n):
        coordinates = input().split()
        x, y = float(coordinates[0]), float(coordinates[1])
        loc.append((x, y))

    # add edges in graph w/ distances
    for u in range(n):
        uX = loc[u][0]
        uY = loc[u][1]
        for v in range(n):
            vX = loc[v][0]
            vY = loc[v][1]
            g.add_edge(u, v, uX, uY, vX, vY)
    # transportation between these is easy by foot
    for u in range(e):
        for v in range(e):
            g.add_edge(u, v, 0, 0, 0 ,0) 
            f.add_edge(u, v, 0, 0, 0, 0)
    # prebuilt cable
    for i in range(p):
        neighbors = input().split()
        u, v = int(neighbors[0]) - 1, int(neighbors[1]) - 1
        g.add_edge(u, v, 0, 0, 0, 0)
        f.add_edge(u, v, 0, 0, 0, 0)
    for i in range(n):
        f.add_edge_wt(i, i, 0)

    # print("F")
    # f.print()
    # print("G")
    # g.print()
    minSpanningTree = boruvka(g, f)
    print(minSpanningTree.get_length())



main()
