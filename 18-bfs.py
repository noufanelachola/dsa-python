class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self,node):
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self,node1,node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def bfs(self):
        queue = queue = [next(iter(self.graph))]  
        visited = set()

        while queue:
            x = queue.pop(0)
            if x not in visited:
                print(x,end=" ")
                visited.add(x)
                queue.extend(self.graph[x])


    def show(self):
        print(self.graph)

graph = Graph()
graph.add_node(5)
graph.add_node(4)
graph.add_node(3)
graph.add_edge(5,3)
graph.add_edge(3,4)
graph.bfs()
