map = None
graph = None
w = None
h = None

class graph_node:
    __marked = False
    __neighbors = None
    __id = None
    __item = None

    def __init__(self, id, item):
        self.__id = id
        self.__item = item
        self.__neighbors = []

    def get_id(self):
        return self.__id

    def get_item(self):
        return self.__item

    def mark(self):
        self.__marked = True

    def is_marked(self):
        return self.__marked

    def add(self, neighbor):
        self.__neighbors.append(neighbor)

    def get_neighbors(self):
        return self.__neighbors



"""
Check if the up, down, left, right neighbors of node i, j contain "T"
"""
def is_drafty(i, j):
    if can_up(i, j) and up_item(i, j) == "T":
        return True
    if can_down(i, j) and down_item(i, j) == "T":
        return True
    if can_left(i, j) and left_item(i, j) == "T":
        return True
    if can_right(i, j) and right_item(i, j) == "T":
        return True

    return False
        
"""
can_up, can_down, can_left, can_right all return if withing the game
there is a legal move up, down, left, right of the current cell, the (i, j) value
"""
def can_up(i, j):
    if i > 0 and up_item(i, j) != "#": # you aren't at the ceiling so you can go up
        return True
    else:
        return False

def can_down(i, j):
    if i < h - 1 and down_item(i, j) != "#":
        return True
    else:
        return False

def can_left(i, j):
    if j > 0 and left_item(i, j) != "#":
        return True
    else:
        return False

def can_right(i, j):
    if j < w - 1 and right_item(i, j) != "#":
        return True
    else:
        return False

"""
up_item, down_item, left_item, right_item all return the character of the item
that is either up, down, left, or right of the entered in cell, the (i,j) value
"""
def up_item(i, j):
    return map[i - 1][j]

def down_item(i, j):
    return map[i + 1][j]

def left_item(i, j):
    return map[i][j - 1]

def right_item(i, j):
    return map[i][j + 1]


# def DFS(node):
#     neighbors = graph[node.get_id()].get_neighbors()
#     gold = 0

#     for neighbor in neighbors:
#         if not neighbor.is_marked():
#             neighbor.mark()
#             if neighbor.get_item() == "G":
#                 gold += 1

#             gold += DFS(neighbor)

#     return gold

def DFS(node):
    stack = list()
    stack.append(node)

    gold = 0

    while stack:
        v = stack.pop()

        if not v.is_marked():
            v.mark()

            if v.get_item() == "G":
                gold += 1

            for w in v.get_neighbors():
                stack.append(w)

    return gold
    



"""
get input

create the graph
    find edges

run DFS on graph 
"""
def main():
    global map, graph, w, h

    temp = input().split()
    w = int(temp[0])
    h = int(temp[1])

    # create map
    map = []
    for i in range(h):
        row = input()
        temp = []
        for j in range(w):
            temp.append(row[j])
        map.append(temp)

    start_node = None # Where the node we want to DFS on is

    # make graph
    graph = []
    for i in range(h):
        for j in range(w):
            id = w * i + j
            item = map[i][j]

            node = graph_node(id, item)
            graph.append(node)

    # add edges
    for i in range(h):
        for j in range(w):
            node_idx = w * i + j
            node = graph[node_idx]

            if node.get_item() == "P":
                start_node = node

            if is_drafty(i, j):
                continue
            if node.get_item() == "#" or node.get_item() == "T": 
                continue
 
            if can_up(i, j):
                up_neighbor_idx = w * (i - 1) + j # up_neighbor is the index of the up neighbor of the current node_idx
                up_neighbor = graph[up_neighbor_idx]
                graph[node_idx].add(up_neighbor)

            if can_down(i, j):
                down_neighbor_idx = w * (i + 1) + j
                down_neighbor = graph[down_neighbor_idx]
                graph[node_idx].add(down_neighbor)

            if can_left(i, j):
                left_neighbor_idx = w * i + j - 1
                left_neighbor = graph[left_neighbor_idx]
                graph[node_idx].add(left_neighbor)
            
            if can_right(i, j):
                right_neighbor_idx = w * i + j + 1
                right_neighbor = graph[right_neighbor_idx]
                graph[node_idx].add(right_neighbor)
    
    max_safe_gold = DFS(start_node)
    print(max_safe_gold)

    



main()
