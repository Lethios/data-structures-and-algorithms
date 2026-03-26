from typing import Iterator


class Node:
    def __init__(
        self, val: int = 0, prev: "Node | None" = None, next: "Node | None" = None
    ):
        self.val: int = val
        self.prev: Node | None = prev
        self.next: Node | None = next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[int]:
        current = self.head

        while current is not None:
            yield current.val
            current = current.next

    def __repr__(self) -> str:
        nodes = " <-> ".join(str(val) for val in self)
        return (nodes if nodes else "empty") + " -> None"

    def append(self, val: int) -> None:
        node = Node(val)

        if self.head is None:
            self.head = self.tail = node
        else:
            if self.tail is not None:
                self.tail.next = node
                node.prev = self.tail

            self.tail = node

        self._size += 1

    def prepend(self, val: int) -> None:
        node = Node(val)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self._size += 1

    def delete(self, val: int) -> None:
        current = self.head

        while current is not None:
            if current.val == val:
                if current.prev is None:
                    self.head = current.next
                else:
                    current.prev.next = current.next

                if current.next is None:
                    self.tail = current.prev
                else:
                    current.next.prev = current.prev

                self._size -= 1
                break

            current = current.next

    def search(self, val: int) -> int:
        current = self.head
        idx: int = 0

        while current is not None:
            if current.val == val:
                return idx

            current = current.next
            idx += 1

        return -1
