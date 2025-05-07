class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []  
        self.graph[u].append(v)

    def dfs(self, v, visited):
        visited.add(v)
        for neighbor in self.graph.get(v, []): 
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def find_root(self):
        for u in range(self.vertices):
            visited = set()
            self.dfs(u, visited)
            if len(visited) == self.vertices:
                return u
        return -1

def read_graph(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    n = int(lines[0])  
    adj = [[] for _ in range(n)]
    for line in lines[1:]:
        u, v = map(int, line.strip().split())
        adj[u].append(v) 
    return adj

def dfs_iterative(graph, start, visited):
    stack = [start]
    while stack:
        vertex = stack.pop(0)
        if not visited[vertex]:
            visited[vertex] = True
            for neighbor in reversed(graph[vertex]):
                if not visited[neighbor]:
                    stack.append(neighbor)

def find_root_vertex_iterative(graph):
    n = len(graph)
    for i in range(n):
        visited = [False] * n
        dfs_iterative(graph, i, visited)
        if all(visited):
            return i
    return -1


def main():
    graph = read_graph('input.txt')
    print("Graph:", graph) 
    root = find_root_vertex_iterative(graph)
    with open('output.txt', 'w') as f:
        f.write(str(root))

main()
