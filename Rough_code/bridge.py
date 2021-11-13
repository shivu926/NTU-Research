# number of nodes in the graph
n = int(input())

# number of edges in the graph
m = int(input())

# adjacency list of the graph
graph = [[] for i in range(n + 1)]

for i in range(m):
    u, v = list(map(int, input().split()))  # input edge
    # Assuming graph to be undirected.
    graph[u].append(v)
    graph[v].append(u)

visited = [False for i in range(n + 1)]
tin = [-1 for i in range(n+1)]
low = [-1 for i in range(n+1)]
time = 0


def dfs(node, parent):
    global time

    # marking node as visited.
    visited[node] = True
    tin[node] = time
    low[node] = time
    time += 1
    for neighbour in graph[node]:
        if neighbour == parent:
            continue
        if visited[neighbour] == True:
            low[node] = min(low[node], tin[neighbour])
        else:
            dfs(neighbour, node)
            low[node] = min(low[node], low[neighbour])
            if low[neighbour] > tin[node]:
                print(node, neighbour, 'is a bridge')


for i in range(n):
    if visited[i] == False:
        dfs(i, -1)