def dfs(graph: list[list[int]], source: int) -> list[int]:
    res: list[int] = []

    visited: set[int] = set()

    def traverse(node: int) -> None:
        visited.add(node)
        res.append(node)

        for neighbor in graph[node]:
            if neighbor in visited:
                continue

            traverse(neighbor)

    traverse(source)

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

    print(dfs(graph, 0))
