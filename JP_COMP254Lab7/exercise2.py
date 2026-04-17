# NOTE: this script does not require installing the previous comp254 package.
#
# Usage: python exercise2.py
# Requires: Python 3.11+
import argparse
import logging
import math
import random
import time
from collections import deque
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--number",
        default=100_000,
        help="The number of elements to sort per run (default: %(default)d)",
        type=int,
    )
    parser.add_argument(
        "-r",
        "--repeat",
        default=5,
        help="The number of runs (default: %(default)d)",
        type=int,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase logging verbosity",
    )

    args = parser.parse_args()

    number: int = args.number
    repeat: int = args.repeat
    verbose: int = args.verbose

    setup_logging(verbose)

    print("Initial test")
    print("============")
    data = generate_shuffled_data(11)
    print("Input: ", data)
    data = merge_sort(data)
    print("Output:", data)

    print()
    print("Benchmark")
    print("=========")
    print(f"Size: {number:,}")

    fastest = math.inf
    for i in range(repeat):
        data = generate_shuffled_data(number)
        elapsed, _ = timed(check_merge_sort, data)

        print(f"{i + 1}. {elapsed * 1000:,.3f}ms")
        fastest = min(fastest, elapsed)

    print(f"Fastest run: {fastest * 1000:,.3f}ms")

    data = generate_shuffled_data(number)
    ground_truth, _ = timed(sorted, data)
    print(f"(Powersort for reference: {ground_truth * 1000:,.3f}ms)")


def setup_logging(verbose: int) -> None:
    if verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(format="%(message)s", level=level)


def generate_shuffled_data(size: int) -> list[int]:
    data = [i for i in range(size)]
    random.shuffle(data)
    return data


def timed(func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> tuple[float, T]:
    start = time.perf_counter()
    ret = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return elapsed, ret


def check_merge_sort(data: list[int]) -> None:
    result = merge_sort(data)
    for i in range(len(result) - 1):
        a, b = result[i], result[i + 1]
        if a > b:
            raise ValueError(f"Merge sort failed at index {i}, {a} > {b}")


def merge_sort(data: list[int]) -> list[int]:
    def mark(label: str):
        nonlocal start
        elapsed = time.perf_counter() - start
        logging.debug(f"{label}: {elapsed * 1000:,.3f}ms")
        start = time.perf_counter()

    start = time.perf_counter()

    runs = deque(deque((n,)) for n in data)
    mark("Created runs")

    if len(runs) < 1:
        return []
    elif len(runs) == 1:
        return list(runs.popleft())

    i = 1
    while len(runs) > 1:
        for _ in range(len(runs) // 2):
            a, b = runs.popleft(), runs.popleft()
            c = deque()
            while a and b:
                if a[0] < b[0]:
                    c.append(a.popleft())
                else:
                    c.append(b.popleft())

            c.extend(a)
            c.extend(b)
            runs.append(c)

        mark(f"Pass {i:,d}")
        i += 1

    return list(runs.popleft())


if __name__ == "__main__":
    main()
