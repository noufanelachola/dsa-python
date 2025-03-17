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
        queue = [next(iter(self.graph))]  
        visited = set()

        while queue:
            x = queue.pop(0)
            if x not in visited:
                print(x,end=" ")
                visited.add(x)
                queue.extend(self.graph[x])
        print("\n")
        

    def dfs(self):
        stack = [next(iter(self.graph))]  
        visited = set()

        while stack:
            x = stack.pop()
            if x not in visited:
                visited.add(x)
                print(x,end=" ")

                for neighbour in self.graph[x]:
                    if neighbour not in visited:
                        stack.append(neighbour)
                        # break
        print("\n")


    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.bfs()
g.dfs()

g.display()