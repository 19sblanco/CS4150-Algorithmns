import heapq
import cProfile

g = None
heap = [] 

class graph:
    g = None
    dist = None
    mark = None
    n = None

    def __init__(self, n):
        self.g = [ {} for _ in range(n)]
        self.dist = [ None for _ in range(n)]
        self.mark = [ False for _ in range(n)]
        self.n = n

    def add_edge(self, u, v, f):
        self.g[u][str(v)] = f
        self.g[v][str(u)] = f

    def print(self):
        for i in range(self.n):
            print(self.g[i])

    # def get_weight(self, u, v):
    #     return self.g[u][v].f

    def get_neighbors(self, u):
        return self.g[u]

    def is_tense(self, u, v):
        """
        old_d = distance of v
        new_d = distance of u + w(u->v)
        if old_d > new_d:
            return true
        else:
            return false
        """
        # if self.pred[u] == v: return False

        old_d = self.dist[v]
        new_d = self.dist[u] * self.g[u][str(v)]
        if new_d > 0: new_d *= -1
        if new_d < old_d:
            return True
        else:
            return False

    def relax(self, u, v):
        """
        dist(v) = dist(u) + w(u->v)
        pred(v) = u
        """
        dist_u = self.dist[u]
        if dist_u < 0:
            dist_u *= -1
        self.dist[v] = dist_u * self.g[u][str(v)]

    def set_dist(self, u, dist):
        self.dist[u] = dist

    def get_dist(self, u):
        return self.dist[u]


        
def initSSSP(s):
    """
    dist(s) ← 0
    pred(s) ← Null
    for all vertices v != s
        dist(v) ← ∞
        pred(v) ← Null
    """
    for i in range(len(g.g)):
        g.set_dist(i, 2)
    g.set_dist(s, 1)


def dijkstras(s):
    """
    InitSSSP(s)
    Insert(s, 0)
    while the priority queue is not empty
        u ← ExtractMin( )
        for all edges u-> v
            if u-> v is tense
                Relax(u-> v)
                if v is in the priority queue
                    DecreaseKey(v, dist(v)) / pretty sure you can reinsert with new distance
                else
                    Insert(v, dist(v))
    """ 
    # f, node
    initSSSP(s)
    dist_s = g.get_dist(s)
    heapq.heappush(heap, (dist_s, s))
    while heap:
        temp = heapq.heappop(heap)
        dist_u = temp[0]
        u = temp[1]
        g.mark[u] = True
        neighbors = g.get_neighbors(u)
        for v,w in neighbors.items():
            v = int(v)
            if g.mark[v]: continue
            if g.is_tense(u, v):
                g.relax(u, v)
                # insert
                dist_v = g.get_dist(v)
                heapq.heappush(heap, (dist_v, v))







def main():
    global g, heap
    
    temp = input().split()
    n, m = int(temp[0]), int(temp[1])

    g = graph(n)
    for _ in range(m):
        temp = input().split()
        x, y, real = int(temp[0]), int(temp[1]), float(temp[2])
        g.add_edge(x, y, -1 * real)

   
    dijkstras(0)
    print(-1 * g.get_dist(n-1))

   


    

main()



