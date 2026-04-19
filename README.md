# ap-stats-calculator

`ap-stats-calculator` is a menu-driven Python program for AP Statistics inference. It helps students identify the correct procedure, review the required checks and setup, compute the key values, and write a conclusion in context. The repo now includes both a full desktop version and a compact TI-84 version.

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

## Which File to Use

- `apinf.py` - full desktop version with more explanatory text
- `apinf_ti.py` - compact TI-84 Plus CE Python version with shorter menus and lower memory use

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

## TI-84 Installation and Use

This project is intended for the **TI-84 Plus CE Python** family.

Recommended setup:

1. Update the calculator to the latest CE Bundle / Python App release.
2. Install [TI Connect CE](https://education.ti.com/html/webhelp/EG_TI84PlusCE/EN/Subsystems/EG_TIC_84CE_SW/Content/EG_84_TIConnect/M_IntroTIC-CE/TC_IntroToTIConnect.HTML) on your computer.
3. Connect the calculator to your computer with USB.
4. Send `apinf_ti.py` to the calculator using **Send to Calculators** in TI Connect CE.
5. TI Connect CE will convert the `.py` file to a Python AppVar (`.8xv`) when it sends it to the calculator.
6. Store the program in **RAM**, not Archive, because the Python App runs and edits Python AppVars from RAM.
7. Open the **Python App** on the calculator and run the transferred program.

Important TI notes:

- TI says the Python App may prompt you to update to the latest CE Bundle the first time you open it.
- TI Connect CE applies calculator naming rules when converting `.py` files to Python AppVars.
- Lowercase file names are automatically changed to uppercase on the calculator.
- If a file name does not match TI naming rules, TI Connect CE may rename it automatically.

Why this code is calculator-friendly:

1. Menus are numeric.
2. Print output is shorter than a desktop-only version.
3. Functions are kept small.
4. The two-sample t procedures use a conservative integer `df`, which is easier to support on the calculator.
5. The t-distribution helper avoids `math.gamma`, which makes TI porting safer.
6. The compact TI file is much smaller than the full desktop file.

Useful TI references:

- [Using TI Connect CE to convert and send Python programs](https://education.ti.com/html/webhelp/EG_TI84PlusCE/EN/Subsystems/EG_TIC_84CE_SW/Content/EG_84_TIConnect/M_UsePython/M_UsePython.HTML)
- [Using the Python App on TI-84 Plus CE Python](https://education.ti.com/html/eguides/graphing/84pluscepy/en/content/eg_pythonappprog/m_pyadpapp/m_pyappuse.HTML)
- [TI-84 Plus CE Python getting started page](https://education.ti.com/en/resources/getting-started-on-ti-technology/ti-84-plus-ce-python)

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
- `apinf_ti.py` - compact TI-84 version
- `examples/sample_problems.txt` - sample AP Statistics-style prompts
- `README.md` - project overview and usage
