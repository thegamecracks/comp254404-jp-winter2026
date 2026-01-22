# comp254404-jp-winter2026

## Setup

1. Install [Python](https://www.python.org/downloads/) 3.11 or newer
2. Clone this repository
3. Create a virtual environment and install the package into it (venv+pip):

   ```sh
   $ python -m venv
   $ .venv\Scripts\activate  # on Linux/MacOS: $ source .venv/bin/activate
   (.venv) $ pip install --editable .
   ```

4. Navigate to any lab or assignment directory to run the exercises:

   ```sh
   (.venv) /    $ cd xyz
   (.venv) /xyz $ python main.py
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
/    $ cd xyz
/xyz $ python main.py
...
```

This is not recommended, but can work in a pinch if creating a virtual environment
is undesirable.

### Alternative Setup (uv)

Instead of venv+pip, you can use Astral's [uv](https://docs.astral.sh/uv/) project manager
which will automatically create the virtual environment and use it:

```sh
/    $ uv sync
/    $ cd xyz
/xyz $ uv run main.py
...
```

uv will automatically install the `dev` dependency group in pyproject.toml,
but it is not required to run any of the assignments.
