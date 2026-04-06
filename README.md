# ap-stats-calculator

`ap-stats-calculator` is a small command-line Python project that supports common AP Statistics inference procedures. It is designed to help students choose the correct method, review the required conditions, and complete the setup, calculations, and conclusion expected on free-response work.

## Why This Project Matters

AP Statistics students often know the formulas but still struggle with procedure selection, condition checks, and writing complete statistical conclusions. This project focuses on that full workflow, combining method selection with computation and short response templates in a format that can later be adapted for a TI-84 Python calculator.

## Features

- Menu-based command-line interface
- Three-step decision tree based on goal, data type, and sample structure
- Built-in checks and conditions for each supported method
- Formula and setup reminders for full-credit written work
- Computation of test statistics, p-values, critical values, and intervals
- Numerical t-model p-value approximation with calculator guidance for t-tests
- Short conclusion templates written in context
- Beginner-friendly Python with no external dependencies beyond `math`

## Current Procedures

Version 1 includes:

- One-proportion z-test
- One-proportion z-interval
- One-mean t-test
- One-mean t-interval
- Two-proportion z-test
- Two-proportion z-interval
- Two-sample t-test
- Two-sample t-interval
- Paired t-test
- Paired t-interval

The decision tree also distinguishes paired categorical data, which is not part
of the current z/t procedure set in this project.

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
1) Decision tree
2) One-prop z-test
3) One-prop z-int
4) One-mean t-test
5) One-mean t-int
6) Exit
Choice: 1

Goal?
1) Confidence interval
2) Hypothesis test
Choice: 2

Data type?
1) Categorical / proportion
2) Quantitative / mean
Choice: 1

Sample structure?
1) One sample
2) Two independent samples
3) Paired data
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
- t-test p-values are approximated numerically and paired with calculator instructions

## Planned Improvements

- Add a compact calculator-screen mode
- Add direct raw-data entry for paired differences
- Add support for more AP Statistics inference families
- Add optional formula abbreviations for faster navigation
- Expand the example problem set
- Improve output formatting for study guides and screenshots

## License

This project is released under the MIT License. See `LICENSE` for details.
