from typing import Iterator


class DisjointSetUnion:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = [i for i in range(n)]
        self.size: list[int] = [1 for _ in range(n)]

    def __len__(self) -> int:
        return len(self.parent)

    def __iter__(self) -> Iterator[tuple[int, list[int]]]:
        sets: dict[int, list[int]] = {}

        for i in range(len(self.parent)):
            root = self.find(i)

            if root not in sets:
                sets[root] = []

            sets[root].append(i)

        yield from sets.items()

    def __repr__(self) -> str:
        return f"{dict(self)}"

    def find(self, node: int) -> int:
        if self.parent[node] == node:
            return node

        self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u: int, v: int) -> None:
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        if self.size[u] >= self.size[v]:
            heavy, light = u, v
        else:
            heavy, light = v, u

        self.parent[light] = heavy
        self.size[heavy] += self.size[light]
