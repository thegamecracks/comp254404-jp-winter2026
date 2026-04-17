# NOTE: this script does not require installing the previous comp254 package.
#
# Usage: python exercise1.py
# Requires: Python 3.11+
from collections import deque
from dataclasses import dataclass
from typing import Generic, TypeVar

from trees import LinkedBinaryNode, LinkedBinaryTree

K = TypeVar("K")
V = TypeVar("V")


# I didn't implement TreeMap, but we'll treat a regular tree like one
@dataclass
class Entry(Generic[K, V]):
    key: K
    value: V


LBT = LinkedBinaryTree[Entry[int, str]]
LBN = LinkedBinaryNode[Entry[int, str]]


def main() -> None:
    balanced, balanced_leaf = create_balanced_search_tree()
    unbalanced, unbalanced_leaf = create_unbalanced_search_tree()

    print("Balanced Search Tree")
    print("====================")
    test_tree(balanced, balanced_leaf)

    print()
    print("Unbalanced Search Tree")
    print("======================")
    test_tree(unbalanced, unbalanced_leaf)


def test_tree(tree: LBT, leaf: LBN) -> None:
    print(tree)
    print("Last leaf                  :", leaf)
    check_depth_height_recursion_limit(tree, leaf)
    check_recursive_tree_search(tree, leaf.element.key)
    check_iterative_tree_search(tree, leaf.element.key)


def create_balanced_search_tree() -> tuple[LBT, LBN]:
    tree = LBT()
    entries = [Entry(i, f"Node {i}") for i in range(1, 2048)]

    # https://www.geeksforgeeks.org/dsa/sorted-array-to-balanced-bst/
    mid = (len(entries) - 1) // 2
    root = tree.add_root(entries[mid])

    queue: deque[tuple[LBN, int, int]] = deque()
    queue.append((root, 0, len(entries) - 1))

    while queue:
        node, start, end = queue.popleft()
        mid = (start + end) // 2
        if start < mid:
            i = (start + mid - 1) // 2
            left = tree.add_left(node, entries[i])
            queue.append((left, start, mid - 1))
        if end > mid:
            i = (mid + end + 1) // 2
            right = tree.add_right(node, entries[i])
            queue.append((right, mid + 1, end))

    return tree, node  # type: ignore  # node should always be bound


def create_unbalanced_search_tree() -> tuple[LBT, LBN]:
    tree = LBT()
    leaf = tree.add_root(Entry(1, "Root node"))
    for i in range(2, 2048):
        leaf = tree.add_right(leaf, Entry(i, f"Node {i}"))
    return tree, leaf


def check_depth_height_recursion_limit(tree: LBT, leaf: LBN) -> None:
    if tree.root is None:
        raise ValueError("Tree does not have a root node")
    elif not tree.is_external(leaf):
        raise ValueError(f"Expected leaf node, got {leaf}")

    try:
        depth = tree.depth(leaf)
    except RecursionError:
        print("tree.depth(leaf)           : RecursionError")
    else:
        print(f"tree.depth(leaf)           : {depth}")

    try:
        height = tree.height(tree.root)
    except RecursionError:
        print("tree.height(root)          : RecursionError")
    else:
        print(f"tree.height(root)          : {height}")


def check_recursive_tree_search(tree: LBT, key: int) -> None:
    if tree.root is None:
        raise ValueError("Tree does not have a root node")

    try:
        p = recursive_tree_search(tree, tree.root, key)
    except RecursionError:
        print(f"recursive_tree_search({key}): RecursionError")
    else:
        print(f"recursive_tree_search({key}): {p}")


def check_iterative_tree_search(tree: LBT, key: int) -> None:
    if tree.root is None:
        raise ValueError("Tree does not have a root node")

    p = iterative_tree_search(tree, tree.root, key)

    print(f"iterative_tree_search({key}): {p}")


def recursive_tree_search(tree: LBT, p: LBN | None, key: int) -> LBN | None:
    if p is None or tree.is_external(p):
        return p

    if p.element.key == key:
        return p
    elif key < p.element.key:
        return recursive_tree_search(tree, tree.left(p), key)
    else:
        return recursive_tree_search(tree, tree.right(p), key)


def iterative_tree_search(tree: LBT, p: LBN | None, key: int) -> LBN | None:
    while p is not None and p.element.key != key and not tree.is_external(p):
        if key < p.element.key:
            p = tree.left(p)
        else:
            p = tree.right(p)
    return p


if __name__ == "__main__":
    main()
