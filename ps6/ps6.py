top_graph = None

class Graph_node:
    __id = None
    __dependencies = None
    __mark = False
    __top_value = None

    def __init__(self, id):
        self.__id = id
        self.__dependencies = dict()

    def add_dependent(self, graph_node, weight):
        self.__dependencies[graph_node] = weight

    def get_dependencies(self):
        return self.__dependencies

    def print(self):
        print("id: ", self.__id, end=" ")
        for node in self.__dependencies:
            print(node, end="->")
        print()
    

    def get_id(self):
        return self.__id

    def __str__(self):
        return str(self.__id)

    def is_marked(self):
        return self.__mark

    def mark(self):
        self.__mark = True

    def un_mark(self):
        self.__mark = False

    def set_top_value(self, num):
        self.__top_value = num

    def get_top_value(self):
        return self.__top_value


def un_mark_all():
    for node in top_graph:
        node.un_mark()


def get_top__order(graph):
    post_order_list = []
    un_mark_all()
    for u in graph:
        if not u.is_marked():
            top_sort_DFS(u, post_order_list)

    return post_order_list
    

def top_sort_DFS(u, list):
    u.mark()
    
    for neighbor, neighbor_weight in u.get_dependencies().items():
        if not neighbor.is_marked():
            
            top_sort_DFS(neighbor, list)

    list.append(u.get_id())



def main():
    global top_graph

    temp = input().split()
    n, m = int(temp[0]), int(temp[1])

    food_amounts = [int(x) for x in input().split()]

    # add nodes to top graph
    top_graph = [] # topology graph
    for i in range(n):
        temp = Graph_node(i)
        top_graph.append(temp)

    # add dependencies in top_graph
    for i in range(m):
        temp = input().split()
        u, v, w = int(temp[0]), int(temp[1]), int(temp[2])

        graph_node = top_graph[v]

        top_graph[u].add_dependent(graph_node, w)

    # count the number of ingredients for each foood you want to make

    reverse_post_order = get_top__order(top_graph)
    for graph_node_id in reverse_post_order:
        
        curr_node = top_graph[graph_node_id]
        for parent, weight in curr_node.get_dependencies().items():
            p_id = parent.get_id()
            p_amount = food_amounts[p_id]

            food_amounts[graph_node_id] += p_amount * weight


    for num in food_amounts:
        print(num, end = " ")





main()
