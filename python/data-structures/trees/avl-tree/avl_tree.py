from typing import Iterator


class Node:
    def __init__(
        self,
        val: int,
        left: "Node | None" = None,
        right: "Node | None" = None,
        height: int = 0,
    ) -> None:
        self.val: int = val
        self.left: Node | None = left
        self.right: Node | None = right
        self.height: int = height


class AVLTree:
    def __init__(self) -> None:
        self.root: Node | None = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[int]:
        def _inorder(node):
            if node is not None:
                yield from _inorder(node.left)
                yield node.val
                yield from _inorder(node.right)

        yield from _inorder(self.root)

    def __repr__(self) -> str:
        return f"{list(self)}"

    def __contains__(self, val: int) -> bool:
        curr_node = self.root

        if curr_node is None:
            return False

        while True:
            if val < curr_node.val:
                if curr_node.left is None:
                    return False
                curr_node = curr_node.left

            elif val > curr_node.val:
                if curr_node.right is None:
                    return False
                curr_node = curr_node.right

            else:
                return True

    def _get_height(self, node: Node | None) -> int:
        return node.height if node is not None else 0

    def _balance_factor(self, node: Node | None) -> int:
        return (
            self._get_height(node.left) - self._get_height(node.right)
            if node is not None
            else 0
        )

    def _left_rotate(self, node: Node) -> Node:
        assert node.right is not None

        new_root: Node = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(
            self._get_height(new_root.left), self._get_height(new_root.right)
        )

        return new_root

    def _right_rotate(self, node: Node) -> Node:
        assert node.left is not None

        new_root: Node = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(
            self._get_height(new_root.left), self._get_height(new_root.right)
        )

        return new_root

    def _insert_node(self, val: int, node: Node | None) -> Node | None:
        if node is None:
            node = Node(val=val, height=1)
            return node

        if val < node.val:
            node.left = self._insert_node(val, node.left)
        elif val > node.val:
            node.right = self._insert_node(val, node.right)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        bal: int = self._balance_factor(node)

        if bal > 1:
            assert node.left is not None

            if val < node.left.val:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        elif bal < -1:
            assert node.right is not None

            if val > node.right.val:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def insert(self, val: int) -> None:
        self.root = self._insert_node(val, self.root)
        self._size += 1

    def search(self, val: int) -> bool:
        return self.__contains__(val)

    def delete(self):  #
        pass

    def height(self) -> int:
        return self._get_height(self.root)

    def min(self) -> int:
        curr_node = self.root

        if curr_node is None:
            raise ValueError

        while curr_node.left is not None:
            curr_node = curr_node.left

        return curr_node.val

    def max(self) -> int:
        curr_node = self.root

        if curr_node is None:
            raise ValueError

        while curr_node.right is not None:
            curr_node = curr_node.right

        return curr_node.val
