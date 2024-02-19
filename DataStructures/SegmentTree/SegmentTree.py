from typing import List, Callable, TypeVar, Optional


T = TypeVar('T')


class SegmentTree:
    """
    Segment Tree data structure for efficient range queries and updates.

    Attributes:
        leaves (List[T]): Initial list of values from which the segment tree is built.
        accumulator (Callable[[T, T], T]): Function to accumulate two values. Must be commutative and associative.
    """

    def __init__(self, leaves: List[T], accumulator: Callable[[T, T], T]) -> None:
        """
        Initializes the segment tree with the given leaves and accumulator function.

        Args:
            leaves (List[T]): The list of values that the segment tree will manage.
            accumulator (Callable[[T, T], T]): The function that defines how to accumulate two segment values.
        """
        self.__n = len(leaves)
        self.acc: Callable[[T, T], T] = accumulator
        self.tree: List[Optional[T]] = [None] * (self.__n * 4)

        self.__build_tree(leaves)

    def __build_tree(self, leaves: List[T]) -> None:
        """
        Builds the segment tree from the initial list of leaves using an iterative approach.
        """
        NEITHER_DONE, LEFT_DONE, BOTH_DONE = 0, 1, 2
        stack = [(0, 0, self.__n, NEITHER_DONE)]

        while stack:
            treeIdx, l, r, state = stack.pop()
            mid = (l + r) // 2
            if l + 1 == r:
                self.tree[treeIdx] = leaves[l]
            elif state == NEITHER_DONE:
                stack.append((treeIdx, l, r, LEFT_DONE))
                stack.append((treeIdx * 2 + 1, l, mid, NEITHER_DONE))
            elif state == LEFT_DONE:
                stack.append((treeIdx, l, r, BOTH_DONE))
                stack.append((treeIdx * 2 + 2, mid, r, NEITHER_DONE))
            else:
                self.tree[treeIdx] = self.acc(
                    self.tree[treeIdx * 2 + 1], self.tree[treeIdx * 2 + 2]
                )

    def query(self, start: int, end: int) -> Optional[T]:
        """
        Performs a range query over the segment defined by [start, end).

        Args:
            start (int): The start index of the range (inclusive).
            end (int): The end index of the range (exclusive).

        Returns:
            The accumulated value over the specified range.
        """
        result: Optional[T] = None
        stack = [(0, 0, self.__n)]

        while stack:
            treeIdx, l, r = stack.pop()
            mid = (l + r) // 2
            if start <= l and r <= end:
                result = self.tree[treeIdx] if result is None else self.acc(result, self.tree[treeIdx])
            else:
                if start < mid:
                    stack.append((treeIdx * 2 + 1, l, mid))
                if mid < end:
                    stack.append((treeIdx * 2 + 2, mid, r))

        return result

    def update(self, i: int, value: T) -> None:
        """
        Updates the value of the leaf at index i.

        Args:
            i (int): The index of the leaf to update.
            value (T): The new value for the leaf.
        """
        CHILD_NOT_DONE, CHILD_DONE = 0, 1
        stack = [(0, 0, self.__n, CHILD_NOT_DONE)]

        while stack:
            treeIdx, l, r, state = stack.pop()
            mid = (l + r) // 2
            if l + 1 == r:
                self.tree[treeIdx] = value
            elif state == CHILD_NOT_DONE:
                stack.append((treeIdx, l, r, CHILD_DONE))
                if i < mid:
                    stack.append((treeIdx * 2 + 1, l, mid, CHILD_NOT_DONE))
                else:
                    stack.append((treeIdx * 2 + 2, mid, r, CHILD_NOT_DONE))
            else:
                self.tree[treeIdx] = self.acc(
                    self.tree[treeIdx * 2 + 1], self.tree[treeIdx * 2 + 2]
                )