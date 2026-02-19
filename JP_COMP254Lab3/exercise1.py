from typing import Iterable


def main() -> None:
    table: list[list[int]] = [[] for _ in range(12)]
    for i, row in enumerate(table):
        for j in range(12):
            row.append(recursive_product(i + 1, j + 1))

    print("Multiplicative table of recursive_product(m, n):")
    print("   ", format_row(i + 1 for i in range(len(table[0]))), " M")

    for i, row in enumerate(table):
        print(f"{i + 1:2d} ", format_row(row))

    print(" N")


def recursive_product(m: int, n: int) -> int:
    assert m >= 0 and n >= 0

    if m == 0 or n == 0:
        return 0
    else:
        return m + recursive_product(m, n - 1)


def format_row(row: Iterable[int]) -> str:
    return "  ".join(f"{n:3d}" for n in row)


if __name__ == "__main__":
    main()
