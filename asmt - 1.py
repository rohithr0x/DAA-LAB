import heapq

def time_taken(n, m, portals, unsafe_minutes):
    graph = [[] for _ in range(n+1)]
    for u, v, w in portals:
        graph[u].append((v, w))
        graph[v].append((u, w))

    distances = [float('inf')] * (n+1)
    distances[1] = 0

    heap = [(0, 1)]

    while heap:
        d, u = heapq.heappop(heap)
        if d != distances[u]:
            continue
        for v, w in graph[u]:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                heapq.heappush(heap, (distances[v], v))

    for i in range(1, n+1):
        if distances[i] == float('inf'):
            return -1

    return distances[n]
print
n, m = map(int, input("Enter the number of universes and portals (n m): " ).split())
portals = [tuple(map(int, input("Enter portal details (a b c): ").split())) for _ in range(m)]
unsafe_minutes = [list(map(int, input("Enter unsafe time details: ").split())) for _ in range(n)]

print('Output =',time_taken(n, m, portals, unsafe_minutes))
