## Repo purpose (big picture)

This repository contains small, self-contained Python examples of classic algorithms (search and sort). Each top-level file (for example `selectionsort.py`, `binarysearch.py`, `linearsearch.py`) implements a single algorithm function and includes a small "Example usage" block at the bottom that runs the function and prints results. There are no services, packages, or external dependencies.

## What an AI coding agent should know up-front

- Files are single-module examples: functions are defined at top-level, then a short example run prints outputs. Use these example blocks as runnable tests/examples.
- Function naming and return conventions: e.g. `binary_search(arr, target)` returns an index or `-1` when not found; `linear_search` follows the same `-1` convention. `selection_sort(arr)` mutates `arr` in-place and prints sample outputs.
- Input shapes are plain Python lists of ints/floats (see `salaries` in `selectionsort.py` and `accounts` in `binarysearch.py`).
- `binary_search` assumes its input is already sorted (this precondition is documented in the file docstring). Do not change algorithm semantics unless adding explicit checks or tests.

## Code patterns and conventions in this repo

- Minimal, imperative style: no classes, no packages, no tests, no type hints. Keep changes simple and consistent with this style unless the user asks to add typing or restructure.
- Example usage is included directly in the module (not behind `if __name__ == '__main__'`). If you add new example runs, follow the existing pattern so examples remain runnable when the file is executed.
- Error signaling: search functions return `-1` for "not found" rather than raising exceptions or returning `None`.

## Running and quick checks (discoverable)

- Run any example directly with the system Python (Windows `cmd.exe`):

  python selectionsort.py
  python binarysearch.py
  python linearsearch.py

- Expect stdout prints from the example blocks; files are runnable as-is and are the primary smoke tests.

## Helpful concrete prompts for this codebase

- "Refactor `selectionsort.py` to add an `if __name__ == '__main__'` guard while preserving the printed example output." (Example target: move the example usage into a guarded main block.)
- "Add a unit test for `binary_search` that verifies it returns `-1` on missing items and correct indices for present items." (Note: there is no test framework in the repo; the agent should add `tests/` and a lightweight `unittest` file if asked.)
- "Convert `linearsearch.py` to include basic input validation (non-list or empty list) while preserving its `-1` return behavior." — show code diff that returns `-1` for invalid inputs.

## Files to reference when making changes

- `selectionsort.py` — demonstrates an in-place sort (`selection_sort`) and prints the sorted list and a slice example.
- `binarysearch.py` — demonstrates precondition (sorted list) and `-1` return convention.
- `linearsearch.py` — simple linear scan with `-1` return convention.

## Constraints and things *not* present (important)

- No packaging (no setup.py/pyproject/requirements). Avoid adding heavy dependencies without a clear need.
- No existing tests or CI configuration. If adding tests, also include minimal instructions or a task to run them.

## Suggested behaviour for the AI agent when editing

- Keep changes minimal and explicit. Preserve the example usage outputs and function signatures unless the user asks for API changes.
- When adding tests or restructuring, mention the new files and provide a runnable command (e.g., `python -m unittest discover`) in the commit message or PR description.
- Use the repository's concrete examples when demonstrating changes (copy the `salaries` or `accounts` arrays into tests/examples).

If any of these points are incomplete or you'd like the instructions to emphasize other files or workflows, tell me what to add or change and I'll revise the file.
