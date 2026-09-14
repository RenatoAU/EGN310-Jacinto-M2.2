# Search Implementation and Defect Hunt

This project implements linear search and binary search, then tests a separate
AI-generated binary-search implementation for an edge-case defect.

## Files

- `search.py` — corrected `linear_search` and `binary_search` functions.
- `ai_binary_search.py` — the AI-generated version retained for review.
- `tests/test_search.py` — passing tests for the corrected functions.
- `tests/test_ai_binary_search_defect.py` — the intentionally failing edge-case test.
- `AI_LOG.md` — prompt, AI output, review, and independent verification.
- `DEFECT_REPORT.md` — failing test and one-paragraph defect explanation.

## Search behavior

- `linear_search` works with unsorted lists and returns the first matching index.
- `binary_search` requires an ascending sorted list and returns an index with a
  matching value, or `-1` if no match exists.
- Both functions return `-1` for an absent target.

## Run the passing tests

If `pytest` is not installed, install the project dependency once:

```bash
python -m pip install -r requirements.txt
```

From the project folder, run:

```bash
python -m pytest tests/test_search.py -q
```

These tests should pass.

## Reproduce the AI defect

Run the defect test separately:

```bash
python -m pytest tests/test_ai_binary_search_defect.py -q
```

This test is expected to fail because it intentionally exposes the bug in the
AI-generated implementation. The expected result is `0`, while the defective
function returns `-1`.

## Quiz reminder

Quiz 1 covers Modules 1 and 2 and is due at the end of this module.
