# graph (list of edges)
# assume directed graph
# for undirected add same edge bt node vice verse

class GraphListOfEdges:
    def __init__(self, number_of_nodes):
        self.total_nodes = number_of_nodes
        self.list_of_edges = []

    def add_edge(self, node1, node2, weight=1):
        self.list_of_edges.append([node1, node2, weight])
    
    def print_edges(self):
        total_edge = len(self.list_of_edges)

        for i in range(total_edge):
            print(f'edge {i+1}: {self.list_of_edges[i]}')

# graph_list_of_edges = GraphListOfEdges(5)

# graph_list_of_edges.add_edge(0, 0, 25)
# graph_list_of_edges.add_edge(0, 1, 5)
# graph_list_of_edges.add_edge(0, 2, 3)
# graph_list_of_edges.add_edge(1, 3, 1)
# graph_list_of_edges.add_edge(1, 4, 15)
# graph_list_of_edges.add_edge(4, 2, 7)
# graph_list_of_edges.add_edge(4, 3, 11)

# graph_list_of_edges.print_edges()

# adjacency matrix implementation

class GraphMatrix:
    def __init__(self, node_count):
        self.total_nodes = node_count

        # create 2D array with 0 weights
        self.adj_matrix = [[0 for _ in range(self.total_nodes)] for _ in range(self.total_nodes)]

    def add_edge(self, node1, node2, weight):
        self.adj_matrix[node1][node2] = weight

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(row)

# graph_adj = GraphMatrix(5)

# graph_adj.add_edge(0, 0, 25)
# graph_adj.add_edge(0, 1, 5)
# graph_adj.add_edge(0, 2, 3)
# graph_adj.add_edge(1, 3, 1)
# graph_adj.add_edge(1, 4, 15)
# graph_adj.add_edge(4, 2, 7)
# graph_adj.add_edge(4, 3, 11)

# graph_adj.print_adj_matrix()


# BFS(search Node)
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self,node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)
    
    def print_graph(self):
        print(self.graph)

    def bfs_search(self, start, target):
        visited = set()
        queue = deque([start])
        parent = {start: None}
        visited.add(start)

        while queue:
            node = queue.popleft()
            if target == node:
                path = []
                while node is not None:
                    path.append(node)
                    node = parent[node]
            
                return path[::-1]
            
            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
                    parent[neighbour] = node

    def bfs_traversal(self, start):
        visited = set()
        queue = deque()

        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    def dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    
    def dfs_start(self, start):
        visited = set()
        self.dfs(start, visited)


# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)

# print(g.bfs_search(0,3))
# g.bfs_traversal(1)
# g.dfs_start(0)

# g.print_graph()


# Topological Sorting
#   A → B → C
#   ↓    ↑
#   D → E
# valid order are: A, D, E, B, C
# valid order will be produced if there is not any cycle.

# Kahns Algorithm(BFS Based)
# key points: It uses indegree of nodes(num of incoming edges). Process node with 0 indegree. Then edges coming from this node are removed and decrement the indegree's of these neighbor's node. Continue these process.

# code in the respect of course schedule 2 problem.

def topo_bfs(num_courses, prereq):
    adj_list = {i:[] for i in range(num_courses)}
    in_degree = [0]*num_courses

    for crs, pre in prereq:
        adj_list[pre].append(crs) # [0,1] means you need to take course 1 first  to take 0. So, 1--->0
        in_degree[crs] += 1

    q = deque() # zero indegree queue
    for index, val in enumerate(in_degree):
        if val == 0:
            q.append(index)
    
    topo_order = []

    while q:
        node = q.popleft()
        topo_order.append(node)

        for neigh in adj_list[node]:
            in_degree[neigh] -= 1
            if in_degree[neigh] == 0:
                q.append(neigh)
    
    if len(topo_order) == num_courses:
        return topo_order
    else:
        return [] # Cycle found
    
numCourses = 6
prerequisites = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
print("Topological Sort (Kahn's Algorithm):", topo_bfs(numCourses, prerequisites))


# Disktra shortest path 
from collections import defaultdict, deque
import heapq

def dijkstra(edges, source, n):
    adj_list = {i: [] for i in range(n)}
    for u,v,wt in edges:
        adj_list[u].append((v,wt))
   
    #initialize all distance as infinity
    distances = {i:float('inf') for i in range(len(adj_list))}
    #source distance is 0
    distances[source] = 0
    heap = [(0, source)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        #explore neighbor

        for neighbor, weight in adj_list[current_node]:
            distance = weight + current_distance

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

print(dijkstra([[0,1,4], [0,2,1], [1,3,1], [2,1,2], [2,3,5]], 0, 4))
    



