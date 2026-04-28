from collections import deque


def bfs(graph: list[list[int]], source: int) -> list[int]:
    res: list[int] = []

    visited: set[int] = set()
    visited.add(source)

    queue: deque[int] = deque([source])

    while queue:
        node: int = queue.popleft()

        res.append(node)

        for neighbor in graph[node]:
            if neighbor in visited:
                continue

            visited.add(neighbor)
            queue.append(neighbor)

    return res


if __name__ == "__main__":
    graph: list[list[int]] = [
        [1, 2],
        [0, 3, 4],
        [0, 5],
        [1],
        [1, 5],
        [2, 4],
    ]

    print(bfs(graph, 0))
