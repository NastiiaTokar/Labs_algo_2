import csv


def merge_sort(edges):
    if len(edges) <= 1:
        return edges

    mid = len(edges) // 2
    left = merge_sort(edges[:mid])
    right = merge_sort(edges[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            self.parent[root2] = root1
            return True
        return False

def read_edges_from_csv(filename):
    edges = []
    wells = set()
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 3:
                continue
            k1, k2, dist = row
            dist = int(dist)
            edges.append((dist, k1, k2))
            wells.update([k1, k2])
    return sorted(edges), wells

def compute_min_fiber_length(file_path):
    edges, nodes = read_edges_from_csv(file_path)
    edges.sort()  

    uf = UnionFind(nodes)
    total_length = 0
    connected_edges = 0

    for distance, well1, well2 in edges:
        if uf.union(well1, well2):
            total_length += distance
            connected_edges += 1

    if connected_edges == len(nodes) - 1:
        return total_length
    return -1

result = compute_min_fiber_length("communication_wells.csv")
print("Мінімальна довжина кабелю:", result)