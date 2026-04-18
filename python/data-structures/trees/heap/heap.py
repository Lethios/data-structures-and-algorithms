from typing import Iterator


class Heap:
    def __init__(self, is_min_heap: bool = True) -> None:
        self.heap: list[int] = []
        self.is_min_heap: bool = is_min_heap

    def __len__(self) -> int:
        return len(self.heap)

    def __iter__(self) -> Iterator[int]:
        return iter(self.heap)

    def __repr__(self) -> str:
        return f"{self.heap}"

    def _compare(self, x: int, y: int) -> bool:
        if self.is_min_heap:
            return self.heap[x] < self.heap[y]

        return self.heap[x] > self.heap[y]

    def insert(self, val) -> None:
        self.heap.append(val)
        self._heapify_up()

    def pop(self) -> int:
        if len(self.heap) == 0:
            raise IndexError

        if len(self.heap) == 1:
            return self.heap.pop(-1)

        val: int = self.heap[0]
        self.heap[0] = self.heap.pop(-1)

        self._heapify_down(0)

        return val

    def peek(self) -> int:
        if len(self.heap) == 0:
            raise IndexError

        return self.heap[0]

    def _heapify_up(self) -> None:
        idx: int = len(self.heap) - 1

        while idx > 0 and self._compare(idx, (idx - 1) // 2):
            parent_idx: int = (idx - 1) // 2

            self.heap[idx], self.heap[parent_idx] = (
                self.heap[parent_idx],
                self.heap[idx],
            )
            idx: int = parent_idx

    def _heapify_down(self, i) -> None:
        idx: int = i

        while True:
            target: int = idx
            left: int = 2 * idx + 1
            right: int = 2 * idx + 2

            if left < len(self.heap) and self._compare(left, target):
                target: int = left

            if right < len(self.heap) and self._compare(right, target):
                target: int = right

            if target == idx:
                break

            self.heap[idx], self.heap[target] = self.heap[target], self.heap[idx]
            idx: int = target
