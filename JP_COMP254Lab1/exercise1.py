from typing import Generic, TypeVar

from comp254 import DoublyLinkedList

T = TypeVar("T")


class ExtendableDoublyLinkedList(DoublyLinkedList[T], Generic[T]):
    def extend(self, other: DoublyLinkedList[T]) -> None:
        # Example:
        #     H A B C T ---> H A B C D E F T
        #     H D E F T
        #     Make C and D point to each other, and likewise for F and T
        #
        # We have to connect the node prior to our trailer to the other's first node,
        # and connect the other's last node to our trailer.
        # We must not connect the headers or trailers to each other.

        if other.is_empty():
            return  # nothing to connect

        assert self.trailer.prev is not None, "header-trailer link is broken"
        assert other.header.next is not None, "other header-trailer link is broken"
        assert other.trailer.prev is not None, "other header-trailer link is broken"

        # C <=> D
        self.trailer.prev.next = other.header.next
        other.header.next.prev = self.trailer.prev

        # F <=> T
        other.trailer.prev.next = self.trailer
        self.trailer.prev = other.trailer.prev

        # Because we've stolen the other list's nodes, we should fix
        # their header and trailer so its structure remains valid.
        other.header.next = other.trailer
        other.trailer.prev = other.header

        self.size += other.size


def main() -> None:
    L = ExtendableDoublyLinkedList[int]()
    L.add_last(1)
    L.add_last(2)
    L.add_last(3)
    print("L:", L)

    M = ExtendableDoublyLinkedList[int]()
    M.add_last(4)
    M.add_last(5)
    M.add_last(6)
    print("M:", M)

    L.extend(M)
    print("M:", M)
    print("L extended:", L)

    print("L reversed:", list(reversed(L)))


if __name__ == "__main__":
    main()
