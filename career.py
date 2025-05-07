def read_input(filename):
    with open(filename, 'r') as f:
        L = int(f.readline().strip())
        experience = []
        for _ in range(L):
            row = list(map(int, f.readline().strip().split()))
            experience.append(row)
        return L, experience

def build_graph(L, experience):
    graph = []
    values = []
    index = 0
    pos_id = [[-1] * (i + 1) for i in range(L)] 

    for i in range(L):
        for j in range(i + 1):
            pos_id[i][j] = index
            values.append(experience[i][j])
            graph.append([])  
            index += 1

    for i in range(L - 1):
        for j in range(i + 1):
            u = pos_id[i][j]
            v1 = pos_id[i + 1][j]
            v2 = pos_id[i + 1][j + 1]
            graph[u].append(v1)
            graph[u].append(v2)

    return graph, values

def topological_sort(graph):
    n = len(graph)
    visited = [False] * n
    order = []

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return order[::-1]

def compute_max_experience(graph, values, topo_order):
    dp = [0] * len(graph)
    parent = [-1] * len(graph) 

    for u in topo_order:
        if dp[u] == 0:
            dp[u] = values[u]
        for v in graph[u]:
            if dp[v] < dp[u] + values[v]:
                dp[v] = dp[u] + values[v]
                parent[v] = u

    max_value = max(dp)
    end_node = dp.index(max_value)

    path = []
    while end_node != -1:
        path.append(end_node)
        end_node = parent[end_node]
    path.reverse()

    return max_value, path

def write_output(filename, value, path, values):
    with open(filename, 'w') as f:
        f.write(str(value) + '\n')
        path_values = [str(values[i]) for i in path[::-1]]  
        f.write(' '.join(path_values) + '\n')

def main():
    L, experience = read_input('career.in')  
    graph, values = build_graph(L, experience)  
    topo_order = topological_sort(graph)  
    result, path = compute_max_experience(graph, values, topo_order)
    write_output('career.out', result, path, values)

main()
