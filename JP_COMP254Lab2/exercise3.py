import math
import time
from dataclasses import dataclass
from typing import Callable, ParamSpec, Sequence, TypeVar

P = ParamSpec("P")
T = TypeVar("T")

DURATION = 1


def main() -> None:
    results = find_optimal_runtime(
        unique1,
        start=DURATION * 500,  # hint: it's very slow!
        end=DURATION * 5000,
        duration=DURATION,
    )
    print(results)

    print()
    results = find_optimal_runtime(
        unique2,
        start=DURATION * 10_000_000,
        end=DURATION * 15_000_000,
        duration=DURATION,
    )
    print(results)


def unique1(data: Sequence[int]) -> bool:
    n = len(data)
    for j in range(n):
        for k in range(j + 1, n):
            if data[j] == data[k]:
                return False
    return True


def unique2(data: Sequence[int]) -> bool:
    n = len(data)
    temp = sorted(data)  # implied copy, O(n) + O(n log n)
    for j in range(n - 1):
        if temp[j] == temp[j + 1]:
            return False
    return True


@dataclass
class OptimalRuntime:
    n: int
    duration: float
    trials: int
    total_elapsed: float

    def __str__(self) -> str:
        return (
            f"Found {self.n:,} / {self.duration:.3f}s after {self.trials:,} "
            f"trials (total time: {self.total_elapsed:.3f}s)"
        )


def find_optimal_runtime(
    func: Callable[[Sequence[int]], bool],
    *,
    start: int,
    end: int,
    duration: float,
) -> OptimalRuntime:
    max_trials = math.ceil(math.log2(end - start)) if start + 1 < end else 0
    print(f"{start    = :,}")
    print(f"{end      = :,}")
    print(f"{duration = :.3f}s")
    print(f"Finding optimal runtime for {func.__name__}, max {max_trials} trials...")

    trials = 0
    elapsed = 0.0
    last_mid = 0
    last_elapsed = 0.0
    time_start = time.perf_counter()
    pad = math.ceil(math.log10(end)) + 2

    # Below condition makes end exclusive, range is [start, end)
    while (mid := start + (end - start) // 2) != start:
        trials += 1
        if last_mid > 0:
            print(f"  {trials:2d}. {mid:,} ", end="", flush=True)
        else:
            print(f"  {trials:2d}. {mid:,} ", end="", flush=True)

        data = generate_unique_data(mid)
        elapsed = timed_call(func, data)

        if last_mid and last_elapsed:
            diff_mid = mid - last_mid
            diff_elapsed = elapsed - last_elapsed
            print(f"/ {elapsed:.3f}s  ({diff_mid:+{pad},d}, {diff_elapsed:+.3f}s)")
        else:
            print(f"/ {elapsed:.3f}s")

        last_mid = mid
        last_elapsed = elapsed

        if math.isclose(elapsed, duration, abs_tol=1e-3):  # 1ms tolerance
            break
        elif elapsed > duration:
            end = mid
        else:
            start = mid

    return OptimalRuntime(
        n=mid,
        duration=elapsed,
        trials=trials,
        total_elapsed=time.perf_counter() - time_start,
    )


def generate_unique_data(n: int) -> Sequence[int]:
    return range(n)  # no memory overhead


def timed_call(func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> float:
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start


if __name__ == "__main__":
    main()
