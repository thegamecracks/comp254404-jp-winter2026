def main() -> None:
    ...


def unique1(data: list[int]) -> bool:
    n = len(data)
    for j in range(n):
        for k in range(j + 1, n):
            if data[j] == data[k]:
                return False
    return True


def unique2(data: list[int]) -> bool:
    n = len(data)
    temp = sorted(data)  # implied copy, O(n) + O(n log n)
    for j in range(n - 1):
        if temp[j] == temp[j + 1]:
            return False
    return True


if __name__ == "__main__":
    main()
