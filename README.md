# ap-stats-calculator

`ap-stats-calculator` is a small command-line Python project that supports common one-sample AP Statistics inference procedures. It is designed to help students choose the correct method, review the required conditions, and complete the setup, calculations, and conclusion expected on free-response work.

## Why This Project Matters

AP Statistics students often know the formulas but still struggle with procedure selection, condition checks, and writing complete statistical conclusions. This project focuses on that full workflow, combining method selection with computation and short response templates in a format that can later be adapted for a TI-84 Python calculator.

## Features

- Menu-based command-line interface
- Procedure chooser based on data type and goal
- Built-in checks and conditions for each supported method
- Formula and setup reminders for full-credit written work
- Computation of test statistics, p-values, critical values, and intervals
- Short conclusion templates written in context
- Beginner-friendly Python with no external dependencies beyond `math`

## Current Procedures

Version 1 includes:

- One-proportion z-test
- One-proportion z-interval
- One-mean t-test
- One-mean t-interval

For each procedure, the program provides:

- Method name
- Conditions and checks
- Formula/setup
- Required input values
- Computed values
- Conclusion template

## Project Structure

- `apinf.py` - main application
- `examples/sample_problems.txt` - sample AP Statistics-style prompts
- `README.md` - project overview and usage

## How to Run

Use Python 3 and run:

```bash
python apinf.py
```

## Example Usage

Example menu flow:

```text
=================================
AP Stats Inference Helper
=================================
1) Choose procedure
2) One-prop z-test
3) One-prop z-int
4) One-mean t-test
5) One-mean t-int
6) Exit
Choice: 1

Data type?
1) Proportion
2) Mean
Choice: 1

Goal?
1) Test a claim
2) Build an interval
Choice: 1

Use: One-Proportion z-Test
```

Example run for a one-proportion z-test:

```text
Context: students who get at least 8 hours of sleep
Successes x: 102
Sample size n: 150
Null proportion p0: 0.60
Alt hypothesis?
1) >
2) <
3) !=
Choice: 3

Alpha (ex: 0.05 or 5): 0.05

Values
- p-hat = 102 / 150 = 0.6800
- SE0 = sqrt((0.6000)(0.4000) / 150) = 0.0400
- z = (0.6800 - 0.6000) / 0.0400 = 2.0000
- p-value = 0.0455
```

Additional practice prompts are available in `examples/sample_problems.txt`.

## Design Notes

The implementation is intentionally simple:

- Only the standard `math` module is used
- Functions are organized by procedure and task
- Prompts stay short for future calculator adaptation
- Numerical methods are implemented directly so the project stays self-contained

## Planned Improvements

- Add two-sample inference procedures
- Add paired t-procedures
- Add a compact calculator-screen mode
- Add optional formula abbreviations for faster navigation
- Expand the example problem set
- Improve output formatting for study guides and screenshots

## License

This project is released under the MIT License. See `LICENSE` for details.
