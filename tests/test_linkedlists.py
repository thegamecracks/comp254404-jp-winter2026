from comp254.lesson2.linkedlists import DoublyLinkedList, SinglyLinkedList


def test_slist_is_empty() -> None:
    slist = SinglyLinkedList[int]()
    assert slist.is_empty()

    slist.add_first(1)
    assert not slist.is_empty()

    slist.remove_first()
    assert slist.is_empty()

    slist.add_first(2)
    slist.add_last(3)
    assert not slist.is_empty()

    slist.remove_first()
    assert not slist.is_empty()
    slist.remove_first()
    assert slist.is_empty()


def test_slist_first_and_last() -> None:
    slist = SinglyLinkedList[int]()
    assert slist.first() is None
    assert slist.last() is None

    slist.add_first(1)
    assert slist.first() == 1
    assert slist.last() == 1

    slist.remove_first()
    assert slist.first() is None
    assert slist.last() is None

    slist.add_first(2)
    slist.add_last(3)
    assert slist.first() == 2
    assert slist.last() == 3

    slist.remove_first()
    assert slist.first() == 3
    assert slist.last() == 3
    slist.remove_first()
    assert slist.first() is None
    assert slist.last() is None


def test_dlist_is_empty() -> None:
    dlist = DoublyLinkedList[int]()
    assert dlist.is_empty()

    dlist.add_first(1)
    assert not dlist.is_empty()

    dlist.remove_first()
    assert dlist.is_empty()

    dlist.add_first(2)
    dlist.add_last(3)
    assert not dlist.is_empty()

    dlist.remove_first()
    assert not dlist.is_empty()
    dlist.remove_first()
    assert dlist.is_empty()


def test_dlist_first_and_last() -> None:
    dlist = DoublyLinkedList[int]()
    assert dlist.first() is None
    assert dlist.last() is None

    dlist.add_first(1)
    assert dlist.first() == 1
    assert dlist.last() == 1

    dlist.remove_first()
    assert dlist.first() is None
    assert dlist.last() is None

    dlist.add_first(2)
    dlist.add_last(3)
    assert dlist.first() == 2
    assert dlist.last() == 3

    dlist.remove_first()
    assert dlist.first() == 3
    assert dlist.last() == 3
    dlist.remove_first()
    assert dlist.first() is None
    assert dlist.last() is None
