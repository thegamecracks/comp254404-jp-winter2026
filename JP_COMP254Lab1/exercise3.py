from typing import Iterator, Self, TypeVar

from comp254 import CircularlyLinkedList, CircularNode

T = TypeVar("T")


class CloneableCircularlyLinkedList(CircularlyLinkedList[T]):
    def clone(self) -> Self:
        copy = type(self)()

        for node in self._iter_nodes():
            copy.add_last(node.element)

        return copy

    def _iter_nodes(self) -> Iterator[CircularNode[T]]:
        if self.tail is None:
            return

        current = self.tail.next
        yield current

        while current is not self.tail:
            current = current.next
            yield current


def main() -> None:
    L = CloneableCircularlyLinkedList[int]()
    L.add_first(2)
    L.add_first(1)
    L.add_last(3)
    print("L:     ", L)

    M = L.clone()
    print("M copy:", M)


if __name__ == "__main__":
    main()
