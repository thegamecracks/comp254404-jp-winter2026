# comp254404-jp-winter2026

## Structure

Project directories are located in the repository root. Each project contains
one or more Python scripts that can be run to perform a specific exercise or step,
e.g. `python exercise1.py`.

However, there are shared modules contained in an `src` directory providing
my translations of data structures, and those modules need to be available
to Python in order for the scripts to run correctly. See [Setup](#setup) below
for instructions.

## Setup

This section describes a few different setups that can be followed.
The steps below are the preferred method, but alternative setups can be
followed if they are more convenient.

1. Install [Python](https://www.python.org/downloads/) 3.11 or newer
2. Clone this repository and open a terminal inside it
3. Create a virtual environment and install the package into it (venv+pip):

   ```sh
   $ python -m venv
   $ .venv\Scripts\activate  # on Linux/MacOS: $ source .venv/bin/activate
   (.venv) $ pip install --editable .
   ```

4. Navigate to any lab or assignment directory to run the exercises:

   ```sh
   (.venv) /    $ cd xyz
   (.venv) /xyz $ python exercise1.py
   ...
   ```

### Alternative Setup (PYTHONPATH)

Instead of venv+pip, you can set the [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
environment variable to let Python import packages from the src/ directory:

```sh
$ set PYTHONPATH=C:\Absoulute\Path\to\src
# on Linux/MacOS:
$ export PYTHONPATH=/absolute/path/to/src

# Now run python as normal:
/               $ cd JP_COMP254Lab1
/JP_COMP254Lab1 $ python exercise1.py
...
```

This is not recommended, but can work in a pinch if creating a virtual environment
is undesirable.

### Alternative Setup (uv)

Instead of venv+pip, you can use Astral's [uv](https://docs.astral.sh/uv/) project manager
which will automatically create the virtual environment and use it:

```sh
/               $ uv sync
/               $ cd JP_COMP254Lab1
/JP_COMP254Lab1 $ uv run exercise1.py
...
```

uv will automatically install the `dev` dependency group in pyproject.toml,
but it is not required to run any of the assignments.
