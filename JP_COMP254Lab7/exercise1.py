# NOTE: this script does not require installing the previous comp254 package.
#
# Usage: python exercise1.py
# Requires: Python 3.11+
from contextlib import suppress
from dataclasses import dataclass
from typing import Generic, TypeVar

from trees import Position, Tree, LinkedBinaryTree

K = TypeVar("K")
V = TypeVar("V")


# I didn't implement TreeMap, but we'll treat a regular tree like one
@dataclass
class Entry(Generic[K, V]):
    key: K
    value: V


def main() -> None:
    # Create a heavily unbalanced tree
    # (must exceed recursion limit of 1000)
    tree = LinkedBinaryTree[Entry[int, str]]()

    leaf = tree.add_root(Entry(1, "Root node"))
    for i in range(2, 1001):
        leaf = tree.add_right(leaf, Entry(i, f"Node {i}"))

    print("Tree:", tree)
    print("Last leaf:", leaf)
    check_depth_height_recursion_limit(tree, leaf)
    check_recursive_tree_search(tree, leaf.element.key)
    check_iterative_tree_search(tree, leaf.element.key)


def check_depth_height_recursion_limit(tree: Tree[K], leaf: Position[K]) -> None:
    print("Testing tree depth and height")

    if not tree.is_external(leaf):
        raise ValueError(f"Expected leaf node, got {leaf}")

    with suppress(RecursionError):
        n = tree.depth(leaf)
        raise RuntimeError(f"Expected tree.depth to exceed recursion limit, got {n}")

    with suppress(RecursionError):
        n = tree.height(tree.root)
        raise RuntimeError(f"Expected tree.height to exceed recursion limit, got {n}")

    print("  Passed! tree.depth and tree.height raised RecursionError")


def check_recursive_tree_search(tree: Tree[Entry[K, V]], key: K) -> None:
    print("Testing recursive tree search")

    if tree.root is None:
        raise ValueError("Tree does not have a root node")

    with suppress(RecursionError):
        p = recursive_tree_search(tree, tree.root, key)
        raise RuntimeError(
            f"Expected recursive tree search to exceed recursion limit, got {p}"
        )

    print("  Passed! recursive_tree_search() raised RecursionError")


def check_iterative_tree_search(tree: Tree[Entry[K, V]], key: K) -> None:
    print("Testing iterative tree search")

    if tree.root is None:
        raise ValueError("Tree does not have a root node")

    p = iterative_tree_search(tree, tree.root, key)

    print(f"  Passed! iterative_tree_search() returned {p}")


def recursive_tree_search(
    tree: Tree[Entry[K, V]],
    p: Position[Entry[K, V]],
    key: K,
) -> Position[Entry[K, V]] | None:
    if tree.is_external(p):
        return p


def iterative_tree_search(
    tree: Tree[Entry[K, V]],
    p: Position[Entry[K, V]],
    key: K,
) -> Position[Entry[K, V]] | None:
    pass


if __name__ == "__main__":
    main()
