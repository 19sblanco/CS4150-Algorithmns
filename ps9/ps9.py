import math as m
import sys

def run(g):
    # best_total = g.all_pair_dist(g.dist)
    best_temp = g.all_pair_dist(g.dist)
    for a in range(g.n):
        for b in range(g.n):
            if a == b or g.has_edge(a, b): continue
            g.temp = copy(g.dist)
            g.add_edge_temp(a, b)

            best_a_b = 0

            for u in range(g.n):
                for v in range(g.n):
                    u_a = g.temp[u][a]
                    a_b = g.temp[a][b]
                    b_v = g.temp[b][v]
                    u_v = g.temp[u][v]
                    new_dist = u_a + a_b + b_v
                    # if  new_dist < u_v:
                    #     g.set_dist_temp(u, v, new_dist)
                    if u > v:
                        if  new_dist < u_v:
                            best_a_b += new_dist
                        else:
                            best_a_b += u_v
                        
                        

                    """
                    if only there was some way of knowing when you are at
                    the last iteration of this pair and then you 
                    could just count up the best answer that you
                    got up to that point, then you wouldn't have
                    to do all_pair_dist

                    maybe:
                        when u > v then you know its the last time you do it

                    """

            # potential_best = g.all_pair_dist(g.temp)
            # if potential_best < best_total:
            #     best_total = potential_best
            if best_a_b < best_temp:
                best_temp = best_a_b

    print(best_temp)
    # print(best_total)

def floyd_warshall(g):
    for r in range(g.n):
        for u in range(g.n):
            for v in range(g.n):
                u_v = g.dist[u][v]
                u_r = g.dist[u][r]
                r_v = g.dist[r][v]
                if u_v > u_r + r_v:
                    g.set_dist(u, v, u_r + r_v)

def copy(list):
    n = len(list)
    new_list = [ [None]*n for _ in range(n) ]
    for i in range(n):
        for j in range(len(list)):
            new_list[i][j] = list[i][j]
    return new_list


class graph:
    n = None
    loc = None
    dist = None
    temp = None
    edges = None


    def __init__(self, n):
        self.n = n
        self.loc = [ None for _ in range(n) ]
        self.dist = [ [sys.maxsize]*n for _ in range(n) ]
        self.temp = [ [sys.maxsize]*n for _ in range(n) ]
        self.edges = [ [False]*n for _ in range(n) ]

        for i in range(self.n):
            self.dist[i][i] = 0
            self.temp[i][i] = 0

    def add_node(self, n, x, y):
        self.loc[n] = (x, y)

    def add_edge(self, u, v):
        u_x = self.loc[u][0]
        u_y = self.loc[u][1]
        v_x = self.loc[v][0]
        v_y = self.loc[v][1]

        dist = m.sqrt( (v_x - u_x)**2 + (v_y - u_y)**2 )
        self.dist[u][v] = dist
        self.dist[v][u] = dist

        self.edges[u][v] = True
        self.edges[v][u] = True

    def add_edge_temp(self, u, v):
        u_x = self.loc[u][0]
        u_y = self.loc[u][1]
        v_x = self.loc[v][0]
        v_y = self.loc[v][1]

        dist = m.sqrt( (v_x - u_x)**2 + (v_y - u_y)**2 )
        self.temp[u][v] = dist
        self.temp[v][u] = dist

    def get_dist(self, u, v):
        return self.dist[u][v]

    def set_dist_temp(self, u, v, w):
        self.temp[u][v] = w
        self.temp[v][u] = w

    def set_dist(self, u, v, w):
        self.dist[u][v] = w
        self.dist[v][u] = w
        
    def print(self):
        print("===loc===")
        for i in range(self.n):
            print(self.loc[i])
        print("===dist===")
        for i in range(self.n):
            print(str(i), self.dist[i])

    def all_pair_dist(self, matrix):
        total = 0
        for i in range(self.n):
            for j in range(self.n):
                if i == j: break
                total += matrix[i][j]
        return total

    def has_edge(self, u, v):
        return self.edges[u][v]


def main():
    n = int(input())

    g = graph(n)

    for i in range(n):
        temp = input().split()
        x, y = int(temp[0]), int(temp[1])
        g.add_node(i, x, y)

    m = int(input())
    for i in range(m):
        temp = input().split()
        u, v = int(temp[0]), int(temp[1])
        g.add_edge(u, v)

    floyd_warshall(g)
    run(g)

    

main()

