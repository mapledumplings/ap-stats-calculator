# ap-stats-calculator

`ap-stats-calculator` is a menu-driven Python program for AP Statistics inference. It helps students identify the correct procedure, review the required checks and setup, compute the key values, and write a conclusion in context.

## Supported Procedures

The current version supports:

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

The decision tree also distinguishes paired categorical data, which is not part of the current z/t procedure set in this project.

## Demo Menu Flow

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
Choice: 2

Use: Two-Proportion z-Test
```

## Example Outputs

Example z-test output:

```text
Setup
- Parameter: p = true proportion of students who get at least 8 hours of sleep
- H0: p = 0.6000
- Ha: p != 0.6000

Values
- p-hat = 102 / 150 = 0.6800
- SE0 = sqrt((0.6000)(0.4000) / 150) = 0.0400
- z = (0.6800 - 0.6000) / 0.0400 = 2.0000
- Alt = !=
- p-value = 0.0455 (normal)

Conclusion
Since p-value = 0.0455 < alpha = 0.0500, we reject H0.
```

Example t-test output:

```text
Values
- d-bar = 4.5000
- s_d = 6.2000
- SE = 6.2000 / sqrt(18) = 1.4614
- t = 4.5000 / 1.4614 = 3.0793
- df = 17
- Alt = >
- p-value = 0.0034 (numerical t approx)
- Plain math code has no exact t CDF.
- This uses numerical integration.
- An exact t routine can be added later.
```

## How to Run Locally

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

```bash
python apinf.py
```

## How to Port to a Calculator

This project was written to be portable to a TI-84 Python calculator later.

Suggested porting steps:

1. Keep the numeric menus and short prompts.
2. Move long explanation text into shorter calculator-friendly labels.
3. Keep the math helper functions separate from the menu/display code.
4. Replace longer README-style wording with abbreviations for calculator screens.
5. Test one procedure at a time after moving it to the calculator.

The top of `apinf.py` also includes TI-84 porting notes for future refactoring.

## How to Upload to GitHub

If the project is local and not pushed yet:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

If the repository already exists on GitHub, the usual flow is:

```bash
git add .
git commit -m "Update AP Stats calculator"
git push
```

## Future Work

- Add a compact calculator-screen mode
- Add direct raw-data entry for paired differences
- Add support for more AP Statistics inference families
- Add shorter text labels for calculator ports
- Expand the sample problem set
- Improve output formatting for study guides

## Resume-Ready Project Description

Built a Python command-line AP Statistics inference calculator that selects appropriate one-sample and two-sample procedures, computes test statistics and intervals, and generates context-based statistical conclusions using only the standard library.

## Project Files

- `apinf.py` - main application
- `examples/sample_problems.txt` - sample AP Statistics-style prompts
- `README.md` - project overview and usage
