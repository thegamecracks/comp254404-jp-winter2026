"""Read a CSV benchmark file and visualize it."""

import argparse
import csv
import itertools
from dataclasses import dataclass
from pathlib import Path
from typing import Self

from bokeh.io import curdoc
from bokeh.palettes import Bokeh8
from bokeh.plotting import figure, show

# CWD should preferably be JP_COMP254Lab2, but we'll tolerate other CWDs
CWD = Path().resolve()
PARENT_DIR = Path(__file__).parent
DEFAULT_SOURCE = PARENT_DIR.joinpath("exercise2_data.csv").relative_to(CWD)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "source",
        default=DEFAULT_SOURCE,
        help="The file to read from",
        nargs="?",
        type=Path,
    )

    args = parser.parse_args()
    source: Path = args.source

    print(f"Reading from {source}...")
    with source.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ["func", "n", "time"]
        rows = [Row.from_dict(row) for row in reader]

    func_xy: dict[str, tuple[list[int], list[float]]] = {}
    for row in rows:
        x, y = func_xy.setdefault(row.func, ([], []))
        x.append(row.n)
        y.append(row.time)

    print("Plotting...")
    curdoc().theme = "dark_minimal"
    colors = itertools.cycle(Bokeh8)
    p = figure(
        title=f"Benchmark results of {source}",
        width=1280,
        height=720,
        x_axis_label="Data size (n)",
        x_axis_type="log",
        y_axis_label="Time (s)",
        y_axis_type="log",
    )
    for func, (x, y) in func_xy.items():
        p.line(x, y, legend_label=func, color=next(colors))
    show(p)


@dataclass(slots=True)
class Row:
    func: str
    n: int
    time: float

    @classmethod
    def from_dict(cls, d: dict[str, str]) -> Self:
        return cls(func=d["func"], n=int(d["n"]), time=float(d["time"]))


if __name__ == "__main__":
    main()
