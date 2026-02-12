import math
import time
from dataclasses import dataclass
from typing import Callable, ParamSpec, Sequence, TypeVar

P = ParamSpec("P")
T = TypeVar("T")

DURATION = 1


def main() -> None:
    # Based on the desired duration above, try to guess N where each function's
    # runtime will match that duration, and then use binary search to emperically
    # determine N.
    #
    # The heuristics below were manually tested on a single system.
    # On different systems, this may be wildly inaccurate.
    approx_unique1 = int(math.sqrt(DURATION) * 4500)
    approx_unique2 = DURATION * 12500000
    lower_tolerance = 0.15
    upper_tolerance = 0.15

    results = find_optimal_runtime(
        unique1,
        start=int(approx_unique1 * (1 - lower_tolerance)),
        end=int(approx_unique1 * (1 + upper_tolerance)),
        duration=DURATION,
    )
    print(results)

    print()
    results = find_optimal_runtime(
        unique2,
        start=int(approx_unique2 * (1 - lower_tolerance)),
        end=int(approx_unique2 * (1 + upper_tolerance)),
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
    temp = sorted(data)  # implied copy, O(n log n) worst-case, O(n) best-case
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

    # Various statistics to keep track
    trials = 0
    elapsed = 0.0
    last_mid = 0
    last_elapsed = 0.0
    started_at = time.perf_counter()

    # Related to output formatting
    pad = math.ceil(math.log10(end)) + 2

    # Below condition makes end exclusive, so actual range is [start, end)
    while (mid := start + (end - start) // 2) != start:
        trials += 1
        _print_trial_start(trials, last_mid, mid)

        data = generate_unique_data(mid)
        elapsed = timed_call(func, data)

        _print_trial_end(elapsed, last_mid, last_elapsed, pad, mid)
        last_mid = mid
        last_elapsed = elapsed

        if math.isclose(elapsed, duration, abs_tol=1e-3):  # 1ms tolerance
            break
        elif elapsed > duration:
            end = mid
        else:
            start = mid

    return OptimalRuntime(
        n=last_mid,
        duration=last_elapsed,
        trials=trials,
        total_elapsed=time.perf_counter() - started_at,
    )


def generate_unique_data(n: int) -> Sequence[int]:
    # While the below sequence has no memory overhead, range is always sorted
    # which inadvertently guarantees O(n) runtime for Timsort / Powersort.
    return range(n)


def _print_trial_start(trials: int, last_mid: int, mid: int) -> None:
    if last_mid > 0:
        print(f"  {trials:2d}. {mid:,} ", end="", flush=True)
    else:
        print(f"  {trials:2d}. {mid:,} ", end="", flush=True)


def _print_trial_end(
    elapsed: float,
    last_mid: int,
    last_elapsed: float,
    pad: int,
    mid: int,
) -> None:
    if last_mid and last_elapsed:
        diff_mid = mid - last_mid
        diff_elapsed = elapsed - last_elapsed
        print(f"/ {elapsed:.3f}s  ({diff_mid:+{pad},d}, {diff_elapsed:+.3f}s)")
    else:
        print(f"/ {elapsed:.3f}s")


def timed_call(func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> float:
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start


if __name__ == "__main__":
    main()
