from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Generic, Iterator, TypeVar

T = TypeVar("T")


@dataclass(eq=False)  # identity-based hashing and comparisons
class SingleNode(Generic[T]):
    element: Final[T]
    next: SingleNode[T] | None

    def __str__(self) -> str:
        if self.next is not None:
            return f"{self.element} => {self.next.element}"
        else:
            return f"{self.element}"


class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: SingleNode[T] | None = None
        self.tail: SingleNode[T] | None = None
        self.size = 0

    def __repr__(self) -> str:
        return f"<{type(self).__name__} head={self.head} tail={self.tail} size={self.size}>"

    def __str__(self) -> str:
        return f"[{', '.join(map(repr, self))}]"

    def __iter__(self) -> Iterator[T]:
        frontier = set()  # detect circular references for safety
        current = self.head
        while current is not None:
            if current in frontier:
                raise RuntimeError(f"Circular reference detected: {current}")

            frontier.add(current)
            yield current.element
            current = current.next

    def is_empty(self) -> bool:
        return self.size == 0

    def first(self) -> T | None:
        if not self.is_empty():
            assert self.head is not None
            return self.head.element

    def last(self) -> T | None:
        if not self.is_empty():
            assert self.tail is not None
            return self.tail.element

    def add_first(self, element: T) -> None:
        new = SingleNode(element, self.head)

        self.head = new
        if self.is_empty():
            self.tail = new

        self.size += 1

    def add_last(self, element: T) -> None:
        new = SingleNode(element, None)

        if self.is_empty():
            self.head = new
        else:
            assert self.tail is not None
            self.tail.next = new

        self.tail = new
        self.size += 1

    def remove_first(self) -> T | None:
        if self.is_empty():
            return

        assert self.head is not None
        element = self.head.element
        self.head = self.head.next

        self.size -= 1
        if self.is_empty():
            self.tail = None

        return element


@dataclass(eq=False)  # identity-based hashing and comparisons
class DoubleNode(Generic[T]):
    element: Final[T]
    prev: DoubleNode[T] | None
    next: DoubleNode[T] | None

    def __str__(self) -> str:
        prev, element, next = self.prev, self.element, self.next
        if prev is not None and next is not None:
            return f"{prev.element} <= {element} => {next.element}"
        elif prev is not None:
            return f"{prev.element} <= {element}"
        elif next is not None:
            return f"{element} => {next.element}"
        return f"{element}"


class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.header = DoubleNode[T](None, None, None)  # type: ignore
        self.trailer = DoubleNode[T](None, self.header, None)  # type: ignore
        self.header.next = self.trailer
        self.size = 0

    def __repr__(self) -> str:
        return f"<{type(self).__name__} header={self.header} trailer={self.trailer} size={self.size}>"

    def __str__(self) -> str:
        return f"[{', '.join(map(repr, self))}]"

    def __iter__(self) -> Iterator[T]:
        frontier = set()  # detect circular references for safety
        current = self.header.next
        while current is not None and current.next is not None:
            if current in frontier:
                raise RuntimeError(f"Circular reference detected: {current}")

            frontier.add(current)
            yield current.element
            current = current.next

    def __reversed__(self) -> Iterator[T]:
        frontier = set()  # detect circular references for safety
        current = self.trailer.prev
        while current is not None and current.prev is not None:
            if current in frontier:
                raise RuntimeError(f"Circular reference detected: {current}")

            frontier.add(current)
            yield current.element
            current = current.prev

    def is_empty(self) -> bool:
        return self.size == 0

    def first(self) -> T | None:
        if not self.is_empty():
            assert self.header.next is not None
            return self.header.next.element

    def last(self) -> T | None:
        if not self.is_empty():
            assert self.trailer.prev is not None
            return self.trailer.prev.element

    def add_first(self, element: T) -> None:
        assert self.header.next is not None
        self.add_between(element, self.header, self.header.next)

    def add_last(self, element: T) -> None:
        assert self.trailer.prev is not None
        self.add_between(element, self.trailer.prev, self.trailer)

    def remove_first(self) -> T | None:
        if not self.is_empty():
            assert self.header.next is not None
            return self.remove(self.header.next)

    def remove_last(self) -> T | None:
        if not self.is_empty():
            assert self.trailer.prev is not None
            return self.remove(self.trailer.prev)

    def add_between(self, element: T, prev: DoubleNode[T], next: DoubleNode[T]) -> None:
        new = DoubleNode(element, prev, next)
        prev.next = new
        next.prev = new
        self.size += 1

    def remove(self, node: DoubleNode[T]) -> T:
        assert node.prev is not None, "cannot remove the header sentinel"
        assert node.next is not None, "cannot remove the trailer sentinel"
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node.element


def main() -> None:
    slist = SinglyLinkedList[str]()
    slist.add_first("MSP")
    slist.add_last("ATL")
    slist.add_last("BOS")
    slist.add_first("LAX")
    print(slist)
    slist.remove_first()
    print(slist)

    dlist = DoublyLinkedList[str]()
    dlist.add_first("MSP")
    dlist.add_last("ATL")
    dlist.add_last("BOS")
    dlist.add_first("LAX")
    print(dlist)
    dlist.remove_first()
    dlist.remove_last()
    print(dlist)


if __name__ == "__main__":
    main()
