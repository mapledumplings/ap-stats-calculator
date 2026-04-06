# ap-stats-calculator

`ap-stats-calculator` is a small command-line Python project for AP Statistics inference.

Version 1 supports:

- one-proportion z-test
- one-proportion z-interval
- one-mean t-test
- one-mean t-interval

The program helps a student:

- choose the right one-sample inference procedure
- see the checks/conditions to verify
- see the formula/setup used for full credit
- identify the values to calculate
- compute the statistic, p-value, or interval
- write a short conclusion in context

## Files

- `apinf.py` - main menu-based program
- `examples/sample_problems.txt` - short practice prompts
- `README.md` - project overview and usage

## Why this version is simple

The code is intentionally beginner-friendly:

- only uses the `math` module
- uses plain functions instead of classes
- keeps prompts short
- keeps logic grouped by procedure
- is written so it could later be adapted to a TI-84 Python calculator

## How to run

Make sure Python 3 is installed, then run:

```bash
python apinf.py
```

## Main menu

When the program starts, you can:

1. choose a procedure from a short decision menu
2. open a specific procedure directly
3. compute values for that procedure
4. exit

## What each procedure includes

Each implemented procedure shows:

- method name
- required checks/conditions
- formula/setup
- needed input values
- computed values
- conclusion template

## Supported computations

### One-proportion z-test

Inputs:

- context
- number of successes `x`
- sample size `n`
- null proportion `p0`
- alternative hypothesis direction
- significance level `alpha`

Outputs:

- sample proportion `p-hat`
- standard error under `H0`
- z statistic
- p-value
- contextual conclusion

### One-proportion z-interval

Inputs:

- context
- number of successes `x`
- sample size `n`
- confidence level

Outputs:

- sample proportion `p-hat`
- critical value `z*`
- standard error
- margin of error
- confidence interval
- contextual conclusion

### One-mean t-test

Inputs:

- context
- sample mean `x-bar`
- sample standard deviation `s`
- sample size `n`
- null mean `mu0`
- alternative hypothesis direction
- significance level `alpha`

Outputs:

- standard error
- t statistic
- degrees of freedom
- p-value
- contextual conclusion

### One-mean t-interval

Inputs:

- context
- sample mean `x-bar`
- sample standard deviation `s`
- sample size `n`
- confidence level

Outputs:

- standard error
- critical value `t*`
- margin of error
- confidence interval
- degrees of freedom
- contextual conclusion

## Notes on conditions

The program lists the AP Stats checks you should discuss, including:

- randomization
- the 10% condition
- large counts for proportion procedures
- Normal/large sample conditions for mean procedures

Some of these checks still depend on the problem context. For example, the program can remind you to check whether a sample was random, but it cannot decide that from numbers alone.

## Example workflow

1. Run `python apinf.py`
2. Pick `1` to choose a procedure
3. Pick `Proportion` or `Mean`
4. Pick `Test` or `Interval`
5. Read the displayed checks and formula
6. Choose to compute
7. Enter the sample values
8. Use the printed conclusion as a model for your write-up

## Porting ideas for a calculator later

This project was written with future TI-84 adaptation in mind:

- short prompts
- simple loops
- no external packages
- clear procedure-specific functions
- limited formatting

Possible later changes:

- replace long text blocks with abbreviated screens
- split computations into smaller calculator-friendly functions
- store common prompts in shorter labels
- add a numeric menu for tails and confidence levels

## License

This repository includes an MIT License in `LICENSE`.
