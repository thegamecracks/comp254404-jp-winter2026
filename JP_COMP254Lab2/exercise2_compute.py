"""Benchmark two prefix average functions and write their results to a CSV file."""

import argparse
import contextlib
import csv
import sys
import time
from pathlib import Path
from typing import Any, Callable, Iterable, ParamSpec, Protocol, Sequence, TypeVar

P = ParamSpec("P")
T = TypeVar("T")

# CWD should preferably be JP_COMP254Lab2, but we'll tolerate other CWDs
CWD = Path().resolve()
PARENT_DIR = Path(__file__).parent
DEFAULT_DEST = PARENT_DIR.joinpath("exercise2_data.csv").relative_to(CWD)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Write to dest even if it already exists",
    )
    parser.add_argument(
        "-n",
        "--end",
        default="1e4",
        help="The largest N to measure (default: %(default)s)",
        type=lambda s: int(float(s)),
    )
    parser.add_argument(
        "dest",
        default=DEFAULT_DEST,
        help="The file to write to",
        nargs="?",
        type=Path,  # a bit inconvenient to support "-" for stdout
    )

    args = parser.parse_args()
    force: bool = args.force
    end: int = args.end
    dest: Path = args.dest

    if dest.exists() and not force:
        sys.exit(f"{dest} already exists, use -f/--force to overwrite")

    start = time.perf_counter()
    with dest.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["func", "n", "time"])

        record_benchmark(prefix_average_1, writer=writer, end=end)
        print()
        record_benchmark(prefix_average_2, writer=writer, end=end)

    elapsed = time.perf_counter() - start
    print(f"Finished benchmark after {elapsed:.3f}s, results written to {dest}")


def prefix_average_1(data: Sequence[float]) -> list[float]:
    n = len(data)
    a: list[float] = []
    for j in range(n):
        total = 0.0
        for i in range(j + 1):
            total += data[i]
        a.append(total / (j + 1))
    return a


def prefix_average_2(data: Sequence[float]) -> list[float]:
    n = len(data)
    a: list[float] = []
    total = 0.0
    for j in range(n):
        total += data[j]
        a.append(total / (j + 1))
    return a


class Writer(Protocol):
    def writerow(self, row: Iterable[Any], /) -> Any: ...


def record_benchmark(
    func: Callable[[Sequence[float]], Sequence[float]],
    *,
    writer: Writer,
    end: int,
) -> None:
    print(f"Benchmarking {func.__name__} up to n = {end:,}")
    pad = len(format(end, ","))
    start = time.perf_counter()
    clock = 0


    for n in range(1, end):
        data = generate_unique_data(n)
        elapsed = timed_call(func, data)
        writer.writerow([func.__name__, n, elapsed])

        total_elapsed = time.perf_counter() - start
        if int(total_elapsed) > clock:
            print(f"  {n:{pad},}/{end:,}...")
            clock = int(total_elapsed)


def generate_unique_data(n: int) -> Sequence[int]:
    return range(n)


def timed_call(func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> float:
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start


if __name__ == "__main__":
    with contextlib.suppress(EOFError, KeyboardInterrupt):
        main()
