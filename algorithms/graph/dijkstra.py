import heapq


def dijkstra(graph: list[list[tuple[int, int]]], source: int) -> list[int]:
    dist: list[int] = [10**18] * len(graph)
    dist[source] = 0

    heap: list[tuple[int, int]] = [(0, source)]

    while heap:
        curr_dist, curr_node = heapq.heappop(heap)

        if curr_dist > dist[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            new_dist = curr_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist


if __name__ == "__main__":
    graph: list[list[tuple[int, int]]] = [
        [(1, 4), (2, 1)],
        [(3, 1)],
        [(1, 2), (3, 5)],
        [(4, 3)],
        [(5, 1)],
        [],
    ]

    print(dijkstra(graph, 0))
