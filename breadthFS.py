from collections import defaultdict
class bfsgraph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, a, b):
        self.graph[a].append(b)
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

g = bfsgraph()
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(5, 3)
g.add_edge(5, 6)
g.add_edge(6, 6)

print("BFS Traversal:")
g.bfs(3)

