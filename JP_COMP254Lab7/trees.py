from abc import ABC, abstractmethod
from typing import Generic, Iterable, Iterator, Protocol, Self, TypeVar

E = TypeVar("E")
E_co = TypeVar("E_co", covariant=True)


class Position(Protocol, Generic[E_co]):
    @property
    def element(self) -> E_co: ...


class Tree(ABC, Generic[E]):
    def __iter__(self) -> Iterator[E]:
        for node in self.positions():
            yield node.element

    @property
    @abstractmethod
    def root(self) -> Position[E] | None:
        raise NotImplementedError

    @abstractmethod
    def parent(self, p: Position[E], /) -> Position[E] | None:
        raise NotImplementedError

    @abstractmethod
    def children(self, p: Position[E], /) -> Iterable[Position[E]]:
        raise NotImplementedError

    def num_children(self, p: Position[E], /) -> int:
        return sum(1 for _ in self.children(p))

    def is_internal(self, p: Position[E], /) -> bool:
        return self.num_children(p) > 0

    def is_external(self, p: Position[E], /) -> bool:
        return self.num_children(p) == 0

    def is_root(self, p: Position[E], /) -> bool:
        return self.root is p

    @property
    def size(self) -> int:
        return sum(1 for _ in self.positions())

    def is_empty(self) -> bool:
        return self.size == 0

    def depth(self, p: Position[E] | None, /) -> int:
        if p is None or self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def height(self, p: Position[E] | None, /) -> int:
        if p is None:
            return 0

        height = 0
        for child in self.children(p):
            height = max(height, 1 + self.height(child))
        return height

    def positions(self) -> Iterator[Position[E]]:
        return self._preorder(self.root)

    def _preorder(self, p: Position[E] | None) -> Iterator[Position[E]]:
        if p is None:
            return

        yield p

        for child in self.children(p):
            yield from self._preorder(child)


class LinkedNode(Position, Generic[E_co]):
    def __init__(
        self,
        element: E_co,
        *,
        parent: Self | None,
        children: list[Self],
    ) -> None:
        super().__init__()
        self._element = element
        self._parent = parent
        self._children = children

    def __repr__(self) -> str:
        return f"<{type(self).__name__} element={self.element!r} children={len(self._children)}>"

    def __str__(self) -> str:
        return str(self.element)

    @property
    def element(self) -> E_co:
        return self._element


class LinkedTree(Tree[E], Generic[E]):
    _root: LinkedNode[E] | None
    _size: int

    def __init__(self) -> None:
        super().__init__()
        self._root = None
        self._size = 0

    def __repr__(self) -> str:
        return f"<{type(self).__name__} root={self.root!r} size={self.size}>"

    @property
    def root(self) -> LinkedNode[E] | None:
        return self._root

    @property
    def size(self) -> int:
        return self._size

    def parent(self, p: LinkedNode[E], /) -> LinkedNode[E] | None:  # type: ignore
        return p._parent

    def children(self, p: LinkedNode[E], /) -> Iterable[LinkedNode[E]]:  # type: ignore
        yield from p._children

    def add_root(self, e: E) -> LinkedNode[E]:
        if self._root is not None:
            raise ValueError("Tree is not empty")

        self._root = LinkedNode(e, parent=None, children=[])
        self._size += 1
        return self._root

    def add_child(self, p: LinkedNode[E], e: E) -> LinkedNode[E]:
        node = LinkedNode(e, parent=p, children=[])
        p._children.append(node)
        self._size += 1
        return node
