def bellman_ford(graph: list[list[tuple[int, int]]], source: int) -> list[int]:
    n: int = len(graph)
    dist: list[int] = [10**18] * n

    dist[source] = 0

    for i in range(n - 1):
        is_updated: bool = False

        for curr_node, neighbors in enumerate(graph):
            for neighbor, weight in neighbors:
                if dist[curr_node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[curr_node] + weight
                    is_updated = True

        if not is_updated:
            break

    for curr_node, neighbors in enumerate(graph):
        for neighbor, weight in neighbors:
            if dist[curr_node] + weight < dist[neighbor]:
                raise ValueError()

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

    print(bellman_ford(graph, 0))
