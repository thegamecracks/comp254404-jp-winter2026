# comp254404-jp-winter2026

## Setup

1. Install [Python](https://www.python.org/downloads/) 3.11 or newer
2. Clone this repository
3. Choose one of two options below to set up the package:

   1. Create a virtual environment and install the package into it:

      ```sh
      $ python -m venv
      $ .venv\Scripts\activate  # on Linux/MacOS: $ source .venv/bin/activate
      (.venv) $ pip install --editable .
      ```

   2. Set the [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
      environment variable to import packages from the src/ directory:

      ```sh
      $ set PYTHONPATH=C:\Absoulute\Path\to\src
      # on Linux/MacOS:
      $ export PYTHONPATH=/absolute/path/to/src
      ```
      This avoids invoking pip, but is more inconvenient to set up each run.

4. Navigate to any lab or assignment directory to run the exercises:

   ```sh
   (.venv) /    $ cd xyz
   (.venv) /xyz $ python main.py
   ...
   ```

For step 3.1, you can also use [astral-uv](https://docs.astral.sh/uv/) to set up the environment:

```sh
/    $ uv sync
/    $ cd xyz
/xyz $ uv run main.py
...
```

Note that uv will automatically install the `dev` dependency group in pyproject.toml,
but it is not required to run any of the labs.
