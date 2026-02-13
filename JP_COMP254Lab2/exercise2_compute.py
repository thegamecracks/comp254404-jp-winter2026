"""Benchmark two prefix average functions and write their results to a CSV file."""

import argparse
import contextlib
import csv
import re
import sys
import time
from pathlib import Path
from dataclasses import dataclass
from typing import Any, Callable, Iterable, ParamSpec, Protocol, Self, Sequence, TypeVar

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
        "--runtime",
        default="3e4/60s",
        help="The maximum N/time to test per function (default: %(default)s)",
        type=Runtime.from_str,
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
    runtime: Runtime = args.runtime
    dest: Path = args.dest

    if dest.exists() and not force:
        sys.exit(f"{dest} already exists, use -f/--force to overwrite")

    start = time.perf_counter()
    with dest.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["func", "n", "time"])

        record_benchmark(prefix_average_1, writer=writer, runtime=runtime)
        print()
        record_benchmark(prefix_average_2, writer=writer, runtime=runtime)

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


@dataclass
class Runtime:
    end: int
    duration: float

    @classmethod
    def from_str(cls, s: str) -> Self:
        m = re.fullmatch(r"([\de]+)(?:/(\d+)s?)", s)
        if m is None:
            raise ValueError(f"Invalid format {s!r}, expected N/duration")
        return cls(end=int(float(m[1])), duration=float(m[2]))

    def __str__(self) -> str:
        return f"n = {self.end:,} or {self.duration}s"


class Writer(Protocol):
    def writerow(self, row: Iterable[Any], /) -> Any: ...


def record_benchmark(
    func: Callable[[Sequence[float]], Sequence[float]],
    *,
    writer: Writer,
    runtime: Runtime,
) -> None:
    print(f"Benchmarking {func.__name__} up to {runtime}")
    pad = len(format(runtime.end, ","))
    start = time.perf_counter()
    clock = 0

    for n in range(1, runtime.end):
        data = generate_unique_data(n)
        elapsed = timed_call(func, data)
        writer.writerow([func.__name__, n, elapsed])

        total_elapsed = time.perf_counter() - start
        remaining = runtime.duration - total_elapsed
        if remaining <= 0:
            return print(
                f"  Reached max runtime of {runtime.duration}s, "
                f"terminating benchmark"
            )
        elif int(total_elapsed) > clock:
            print(f"  {n:{pad},}/{runtime.end:,}, {remaining:.1f}s left...")
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
