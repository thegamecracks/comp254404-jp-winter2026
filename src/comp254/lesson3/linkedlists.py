from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Generic, Iterator, TypeVar

T = TypeVar("T")


@dataclass(eq=False)  # identity-based hashing and comparisons
class CircularNode(Generic[T]):
    element: Final[T]
    next: CircularNode[T]

    def __str__(self) -> str:
        return f"{self.element} => {self.next.element}"


class CircularlyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.tail: CircularNode[T] | None = None
        self.size = 0

    def __repr__(self) -> str:
        return f"<{type(self).__name__} tail={self.tail} size={self.size}>"

    def __str__(self) -> str:
        return f"[{', '.join(map(repr, self))}]"

    def __iter__(self) -> Iterator[T]:
        if self.tail is None:
            return

        current = self.tail.next
        yield current.element

        while current is not self.tail:
            current = current.next
            yield current.element

    def is_empty(self) -> bool:
        return self.size == 0

    def first(self) -> T | None:
        if not self.is_empty():
            assert self.tail is not None
            assert self.tail.next is not None
            return self.tail.next.element

    def last(self) -> T | None:
        if not self.is_empty():
            assert self.tail is not None
            return self.tail.element

    def rotate(self) -> None:
        if self.tail is not None:
            self.tail = self.tail.next

    def add_first(self, element: T) -> None:
        if self.is_empty():
            self.tail = CircularNode(element, None)  # type: ignore
            self.tail.next = self.tail
        else:
            assert self.tail is not None
            new = CircularNode(element, self.tail.next)
            self.tail.next = new

        self.size += 1

    def add_last(self, element: T) -> None:
        self.add_first(element)
        assert self.tail is not None
        self.tail = self.tail.next

    def remove_first(self) -> T | None:
        if self.is_empty():
            return

        assert self.tail is not None
        head = self.tail.next
        if head == self.tail:
            self.tail = None
        else:
            self.tail.next = head.next

        self.size -= 1
        return head.element


def main() -> None:
    clist = CircularlyLinkedList[str]()
    clist.add_first("LAX")
    print(clist)
    clist.add_last("MSP")
    print(clist)
    clist.add_last("ATL")
    print(clist)
    clist.add_last("BOS")
    print(clist)

    clist.remove_first()
    print(clist)

    clist.rotate()
    print(clist)


if __name__ == "__main__":
    main()
