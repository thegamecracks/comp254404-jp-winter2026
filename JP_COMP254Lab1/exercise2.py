from typing import Iterator, TypeVar

from comp254 import SinglyLinkedList, SingleNode

T = TypeVar("T")


class SwappableSinglyLinkedList(SinglyLinkedList[T]):
    def swap_nodes(self, a: SingleNode[T], b: SingleNode[T]) -> None:
        # Ap => A => Bp => B
        # Find the nodes that reference a and b (unless either is head)
        a_prev: SingleNode[T] | None = None
        b_prev: SingleNode[T] | None = None

        for node in self._iter_nodes():
            if node.next is a:
                a_prev = node
            if node.next is b:
                b_prev = node

            if a_prev is None and a is not self.head:
                continue
            elif b_prev is None and b is not self.head:
                continue

            break  # both nodes found, we can stop early

        if a_prev is None and a is not self.head:
            raise ValueError(f"Node not in list: {a}")
        elif b_prev is None and b is not self.head:
            raise ValueError(f"Node not in list: {b}")

        # # Optimization, not required
        # if a is b:
        #     return

        # Ap => B, Bp => A
        # Swap the prior nodes' next pointers
        if a_prev is None:
            self.head = b
        else:
            a_prev.next = b

        if b_prev is None:
            self.head = a
        else:
            b_prev.next = a

        # Ap => B => Bp => A
        # Swap both node's next pointers
        a.next, b.next = b.next, a.next

        # Ensure tail is updated
        if self.tail is a:
            self.tail = b
        elif self.tail is b:
            self.tail = a

    def _iter_nodes(self) -> Iterator[SingleNode[T]]:
        current = self.head
        while current is not None:
            yield current
            current = current.next


def main() -> None:
    L = SwappableSinglyLinkedList[int]()
    L.add_last(1)
    L.add_last(2)
    print("L:     ", L)

    assert L.head is not None
    assert L.tail is not None
    a, b = L.head, L.tail

    L.swap_nodes(a, b)
    print("L swap:", L)
    L.swap_nodes(a, b)
    print("L swap:", L)
    print()

    L.add_first(3)
    L.add_last(4)
    print("L add: ", L)

    L.swap_nodes(a, b)
    print("L swap:", L)
    L.swap_nodes(L.tail, L.head)
    print("L swap:", L)
    L.swap_nodes(b, L.tail)
    print("L swap:", L)
    L.swap_nodes(a, L.tail)
    print("L swap:", L)
    print()

    L.swap_nodes(L.head, L.tail)
    print("L swap:", L)
    L.swap_nodes(L.head.next, L.head.next.next)  # type: ignore
    print("L swap:", L)


if __name__ == "__main__":
    main()
