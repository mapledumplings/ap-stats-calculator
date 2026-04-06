"""AP Statistics inference helper.

This command-line program helps students choose a one-sample or two-sample
inference procedure, review the required checks and formulas, and compute the
key values for the procedures implemented in version 1.
"""

import math


PROCEDURES = {
    "one_prop_test": {
        "name": "One-Proportion z-Test",
        "goal": "test",
        "data_type": "proportion",
        "sample_type": "one",
        "implemented": True,
        "checks": [
            "Random sample or random assignment",
            "10% condition if sampling w/o replacement",
            "Large counts using H0: np0 >= 10 and n(1-p0) >= 10",
        ],
        "formula": [
            "Parameter: p = true proportion in context",
            "H0: p = p0",
            "Ha: p > p0, p < p0, or p != p0",
            "p-hat = x / n",
            "z = (p-hat - p0) / sqrt(p0(1-p0)/n)",
            "p-value from the standard normal model",
        ],
        "required_values": ["x", "n", "p0", "tail", "alpha", "context"],
        "computed_values": ["p-hat", "SE0", "z", "p-value"],
        "conclusion_template": (
            "Since p-value = ___ [< or >] alpha = ___, we [reject or fail to "
            "reject] H0. There is [convincing or not convincing] evidence "
            "that the true proportion of [context] is [relation to p0]."
        ),
    },
    "one_prop_interval": {
        "name": "One-Proportion z-Interval",
        "goal": "interval",
        "data_type": "proportion",
        "sample_type": "one",
        "implemented": True,
        "checks": [
            "Random sample or random assignment",
            "10% condition if sampling w/o replacement",
            "Large counts: n(p-hat) >= 10 and n(1-p-hat) >= 10",
        ],
        "formula": [
            "Parameter: p = true proportion in context",
            "p-hat = x / n",
            "SE = sqrt(p-hat(1-p-hat)/n)",
            "CI: p-hat +/- z*SE",
        ],
        "required_values": ["x", "n", "confidence level", "context"],
        "computed_values": ["p-hat", "z*", "SE", "ME", "interval"],
        "conclusion_template": (
            "We are ___% confident that the true proportion of [context] is "
            "between ___ and ___."
        ),
    },
    "one_mean_test": {
        "name": "One-Mean t-Test",
        "goal": "test",
        "data_type": "mean",
        "sample_type": "one",
        "implemented": True,
        "checks": [
            "Random sample or random assignment",
            "10% condition if sampling w/o replacement",
            "Population is Normal or sample is large enough",
            "No strong skew/outliers for small n",
        ],
        "formula": [
            "Parameter: mu = true mean in context",
            "H0: mu = mu0",
            "Ha: mu > mu0, mu < mu0, or mu != mu0",
            "t = (x-bar - mu0) / (s / sqrt(n))",
            "df = n - 1",
            "p-value from the t model",
        ],
        "required_values": ["x-bar", "s", "n", "mu0", "tail", "alpha", "context"],
        "computed_values": ["SE", "t", "df", "p-value"],
        "conclusion_template": (
            "Since p-value = ___ [< or >] alpha = ___, we [reject or fail to "
            "reject] H0. There is [convincing or not convincing] evidence "
            "that the true mean of [context] is [relation to mu0]."
        ),
    },
    "one_mean_interval": {
        "name": "One-Mean t-Interval",
        "goal": "interval",
        "data_type": "mean",
        "sample_type": "one",
        "implemented": True,
        "checks": [
            "Random sample or random assignment",
            "10% condition if sampling w/o replacement",
            "Population is Normal or sample is large enough",
            "No strong skew/outliers for small n",
        ],
        "formula": [
            "Parameter: mu = true mean in context",
            "SE = s / sqrt(n)",
            "df = n - 1",
            "CI: x-bar +/- t*SE",
        ],
        "required_values": ["x-bar", "s", "n", "confidence level", "context"],
        "computed_values": ["SE", "t*", "ME", "interval"],
        "conclusion_template": (
            "We are ___% confident that the true mean of [context] is between "
            "___ and ___."
        ),
    },
    "two_prop_test": {
        "name": "Two-Proportion z-Test",
        "goal": "test",
        "data_type": "proportion",
        "sample_type": "two",
        "implemented": True,
        "checks": [
            "Random sample or random assignment for each group",
            "Independent groups",
            "10% condition for each sample if sampling w/o replacement",
            "Large counts using pooled p-hat for both groups",
        ],
        "formula": [
            "Parameter: p1 - p2 = true difference in proportions",
            "H0: p1 - p2 = 0",
            "Ha: p1 - p2 > 0, p1 - p2 < 0, or p1 - p2 != 0",
            "p-hat1 = x1 / n1 and p-hat2 = x2 / n2",
            "p-hatc = (x1 + x2) / (n1 + n2)",
            "z = ((p-hat1 - p-hat2) - 0) / sqrt(p-hatc(1-p-hatc)(1/n1+1/n2))",
            "p-value from the standard normal model",
        ],
        "required_values": [
            "x1",
            "n1",
            "x2",
            "n2",
            "tail",
            "alpha",
            "group 1 context",
            "group 2 context",
        ],
        "computed_values": ["p-hat1", "p-hat2", "p-hatc", "SE0", "z", "p-value"],
        "conclusion_template": (
            "Since p-value = ___ [< or >] alpha = ___, we [reject or fail to "
            "reject] H0. There is [convincing or not convincing] evidence "
            "that the true difference in proportions of [group 1 context] and "
            "[group 2 context] is [relation to 0]."
        ),
    },
    "two_prop_interval": {
        "name": "Two-Proportion z-Interval",
        "goal": "interval",
        "data_type": "proportion",
        "sample_type": "two",
        "implemented": True,
        "checks": [
            "Random sample or random assignment for each group",
            "Independent groups",
            "10% condition for each sample if sampling w/o replacement",
            "Large counts in each sample using p-hat1 and p-hat2",
        ],
        "formula": [
            "Parameter: p1 - p2 = true difference in proportions",
            "p-hat1 = x1 / n1 and p-hat2 = x2 / n2",
            "SE = sqrt(p-hat1(1-p-hat1)/n1 + p-hat2(1-p-hat2)/n2)",
            "CI: (p-hat1 - p-hat2) +/- z*SE",
        ],
        "required_values": [
            "x1",
            "n1",
            "x2",
            "n2",
            "confidence level",
            "group 1 context",
            "group 2 context",
        ],
        "computed_values": ["p-hat1", "p-hat2", "z*", "SE", "ME", "interval"],
        "conclusion_template": (
            "We are ___% confident that p1 - p2, the true difference in "
            "proportions of [group 1 context] minus [group 2 context], is "
            "between ___ and ___."
        ),
    },
    "two_mean_test": {
        "name": "Two-Sample t-Test",
        "goal": "test",
        "data_type": "mean",
        "sample_type": "two",
        "implemented": True,
        "checks": [
            "Random sample or random assignment for each group",
            "Independent groups",
            "10% condition for each sample if sampling w/o replacement",
            "Normal/large sample condition for both groups",
            "No strong skew/outliers in either group for small samples",
        ],
        "formula": [
            "Parameter: mu1 - mu2 = true difference in means",
            "H0: mu1 - mu2 = 0",
            "Ha: mu1 - mu2 > 0, mu1 - mu2 < 0, or mu1 - mu2 != 0",
            "t = ((x1-bar - x2-bar) - 0) / sqrt(s1^2/n1 + s2^2/n2)",
            "df from technology or conservative smaller df",
            "p-value from the t model",
        ],
        "required_values": [
            "x1-bar",
            "s1",
            "n1",
            "x2-bar",
            "s2",
            "n2",
            "tail",
            "alpha",
            "group 1 context",
            "group 2 context",
        ],
        "computed_values": ["SE", "t", "df", "p-value"],
        "conclusion_template": (
            "Since p-value = ___ [< or >] alpha = ___, we [reject or fail to "
            "reject] H0. There is [convincing or not convincing] evidence "
            "that the true difference in means of [group 1 context] and "
            "[group 2 context] is [relation to 0]."
        ),
    },
    "two_mean_interval": {
        "name": "Two-Sample t-Interval",
        "goal": "interval",
        "data_type": "mean",
        "sample_type": "two",
        "implemented": True,
        "checks": [
            "Random sample or random assignment for each group",
            "Independent groups",
            "10% condition for each sample if sampling w/o replacement",
            "Normal/large sample condition for both groups",
            "No strong skew/outliers in either group for small samples",
        ],
        "formula": [
            "Parameter: mu1 - mu2 = true difference in means",
            "SE = sqrt(s1^2/n1 + s2^2/n2)",
            "df from technology or conservative smaller df",
            "CI: (x1-bar - x2-bar) +/- t*SE",
        ],
        "required_values": [
            "x1-bar",
            "s1",
            "n1",
            "x2-bar",
            "s2",
            "n2",
            "confidence level",
            "group 1 context",
            "group 2 context",
        ],
        "computed_values": ["SE", "t*", "ME", "interval", "df"],
        "conclusion_template": (
            "We are ___% confident that mu1 - mu2, the true difference in "
            "means of [group 1 context] minus [group 2 context], is between "
            "___ and ___."
        ),
    },
    "paired_mean_test": {
        "name": "Paired t-Test",
        "goal": "test",
        "data_type": "mean",
        "sample_type": "paired",
        "implemented": True,
        "checks": [
            "Random sample or random assignment",
            "10% condition if sampling w/o replacement",
            "Analyze the differences d = value1 - value2",
            "Normal/large sample condition for the differences",
            "No strong skew/outliers in the differences for small n",
        ],
        "formula": [
            "Parameter: mu_d = true mean difference",
            "H0: mu_d = 0",
            "Ha: mu_d > 0, mu_d < 0, or mu_d != 0",
            "t = (d-bar - 0) / (s_d / sqrt(n))",
            "df = n - 1",
            "p-value from the t model",
        ],
        "required_values": ["d-bar", "s_d", "n", "tail", "alpha", "difference context"],
        "computed_values": ["SE", "t", "df", "p-value"],
        "conclusion_template": (
            "Since p-value = ___ [< or >] alpha = ___, we [reject or fail to "
            "reject] H0. There is [convincing or not convincing] evidence "
            "that the true mean difference for [difference context] is "
            "[relation to 0]."
        ),
    },
    "paired_mean_interval": {
        "name": "Paired t-Interval",
        "goal": "interval",
        "data_type": "mean",
        "sample_type": "paired",
        "implemented": True,
        "checks": [
            "Random sample or random assignment",
            "10% condition if sampling w/o replacement",
            "Analyze the differences d = value1 - value2",
            "Normal/large sample condition for the differences",
            "No strong skew/outliers in the differences for small n",
        ],
        "formula": [
            "Parameter: mu_d = true mean difference",
            "SE = s_d / sqrt(n)",
            "df = n - 1",
            "CI: d-bar +/- t*SE",
        ],
        "required_values": ["d-bar", "s_d", "n", "confidence level", "difference context"],
        "computed_values": ["SE", "t*", "ME", "interval", "df"],
        "conclusion_template": (
            "We are ___% confident that mu_d, the true mean difference for "
            "[difference context], is between ___ and ___."
        ),
    },
}

DIRECT_MENU_TO_PROCEDURE = {
    "2": "one_prop_test",
    "3": "one_prop_interval",
    "4": "one_mean_test",
    "5": "one_mean_interval",
}


def main():
    """Run the main menu loop."""
    while True:
        print_header()
        print("1) Decision tree")
        print("2) One-prop z-test")
        print("3) One-prop z-int")
        print("4) One-mean t-test")
        print("5) One-mean t-int")
        print("6) Exit")
        choice = input("Choice: ").strip()
        print()

        if choice == "1":
            choose_by_decision_tree()
        elif choice in DIRECT_MENU_TO_PROCEDURE:
            open_procedure(DIRECT_MENU_TO_PROCEDURE[choice])
        elif choice == "6":
            print("Bye.")
            break
        else:
            print("Enter 1 to 6.\n")


def print_header():
    print("=" * 33)
    print("AP Stats Inference Helper")
    print("=" * 33)


def choose_by_decision_tree():
    goal = choose_goal()
    data_type = choose_data_type()
    sample_type = choose_sample_type()
    procedure_id = find_procedure(goal, data_type, sample_type)

    if procedure_id:
        open_procedure(procedure_id)
    else:
        print_no_match_message(data_type, sample_type)


def choose_goal():
    print("Goal?")
    print("1) Confidence interval")
    print("2) Hypothesis test")
    choice = input("Choice: ").strip()
    print()
    if choice == "1":
        return "interval"
    if choice == "2":
        return "test"
    print("Using hypothesis test by default.")
    print()
    return "test"


def choose_data_type():
    print("Data type?")
    print("1) Categorical / proportion")
    print("2) Quantitative / mean")
    choice = input("Choice: ").strip()
    print()
    if choice == "1":
        return "proportion"
    if choice == "2":
        return "mean"
    print("Using quantitative / mean by default.")
    print()
    return "mean"


def choose_sample_type():
    print("Sample structure?")
    print("1) One sample")
    print("2) Two independent samples")
    print("3) Paired data")
    choice = input("Choice: ").strip()
    print()
    if choice == "1":
        return "one"
    if choice == "2":
        return "two"
    if choice == "3":
        return "paired"
    print("Using one sample by default.")
    print()
    return "one"


def find_procedure(goal, data_type, sample_type):
    for procedure_id, procedure in PROCEDURES.items():
        if (
            procedure["goal"] == goal
            and procedure["data_type"] == data_type
            and procedure["sample_type"] == sample_type
        ):
            return procedure_id
    return ""


def open_procedure(procedure_id):
    procedure = PROCEDURES[procedure_id]
    print("Use:", procedure["name"])
    print()
    display_procedure_summary(procedure_id)
    if procedure["implemented"]:
        if ask_yes_no("Compute now? (y/n): "):
            print()
            run_procedure_computation(procedure_id)
        else:
            print()
    else:
        print("Computation for this procedure is not in v1.")
        print()


def print_no_match_message(data_type, sample_type):
    if data_type == "proportion" and sample_type == "paired":
        print("No z/t procedure is listed here for paired categorical data.")
        print("This calculator currently focuses on proportion z and mean t methods.")
        print()
    else:
        print("No matching procedure was found for that choice.")
        print()


def display_procedure_summary(procedure_id):
    procedure = PROCEDURES[procedure_id]
    print(procedure["name"])
    print("-" * len(procedure["name"]))
    print("Status:")
    if procedure["implemented"]:
        print("- Implemented")
    else:
        print("- Guide only for now")
    print("Checks:")
    for item in procedure["checks"]:
        print("-", item)
    print("Formula/setup:")
    for item in procedure["formula"]:
        print("-", item)
    print("Need:")
    print("-", ", ".join(procedure["required_values"]))
    print("Calc:")
    print("-", ", ".join(procedure["computed_values"]))
    print("Conclusion template:")
    print("-", procedure["conclusion_template"])
    print()


def run_procedure_computation(procedure_id):
    if procedure_id == "one_prop_test":
        run_one_proportion_z_test()
    elif procedure_id == "one_prop_interval":
        run_one_proportion_z_interval()
    elif procedure_id == "one_mean_test":
        run_one_mean_t_test()
    elif procedure_id == "one_mean_interval":
        run_one_mean_t_interval()
    elif procedure_id == "two_prop_test":
        run_two_proportion_z_test()
    elif procedure_id == "two_prop_interval":
        run_two_proportion_z_interval()
    elif procedure_id == "two_mean_test":
        run_two_sample_t_test()
    elif procedure_id == "two_mean_interval":
        run_two_sample_t_interval()
    elif procedure_id == "paired_mean_test":
        run_paired_t_test()
    elif procedure_id == "paired_mean_interval":
        run_paired_t_interval()


def run_one_proportion_z_test():
    print("One-Proportion z-Test")
    print("---------------------")
    context = get_context()
    successes, sample_size = get_successes_and_sample_size()
    null_proportion = get_probability("Null proportion p0: ")
    tail = get_tail()
    alpha = get_probability("Alpha (ex: 0.05 or 5): ")
    population_size = get_optional_positive_int(
        "Population size N (Enter if large/unk): "
    )

    sample_proportion = successes / sample_size
    standard_error_null = math.sqrt(
        null_proportion * (1 - null_proportion) / sample_size
    )
    z_statistic = (sample_proportion - null_proportion) / standard_error_null
    cumulative_probability = normal_cdf(z_statistic)
    p_value = tail_p_value(cumulative_probability, tail)

    print()
    print("Checks")
    print_checks(
        get_one_proportion_test_checks(sample_size, null_proportion, population_size)
    )
    print()
    print("Setup")
    print(f"- Parameter: p = true proportion of {context}")
    print(f"- H0: p = {format_number(null_proportion)}")
    print(f"- Ha: p {tail} {format_number(null_proportion)}")
    print()
    print("Values")
    print(
        f"- p-hat = {successes} / {sample_size} = "
        f"{format_number(sample_proportion)}"
    )
    print(
        f"- SE0 = sqrt(({format_number(null_proportion)})"
        f"({format_number(1 - null_proportion)}) / {sample_size}) = "
        f"{format_number(standard_error_null)}"
    )
    print(
        f"- z = ({format_number(sample_proportion)} - "
        f"{format_number(null_proportion)}) / "
        f"{format_number(standard_error_null)} = {format_number(z_statistic)}"
    )
    print(f"- p-value = {format_number(p_value)}")
    print()
    print("Conclusion")
    print(test_conclusion(p_value, alpha, "proportion", context, tail, null_proportion))
    print()


def run_one_proportion_z_interval():
    print("One-Proportion z-Interval")
    print("-------------------------")
    context = get_context()
    successes, sample_size = get_successes_and_sample_size()
    confidence_level = get_confidence_level()
    population_size = get_optional_positive_int(
        "Population size N (Enter if large/unk): "
    )

    sample_proportion = successes / sample_size
    z_critical = inverse_normal_cdf((1 + confidence_level) / 2)
    standard_error = math.sqrt(
        sample_proportion * (1 - sample_proportion) / sample_size
    )
    margin_of_error = z_critical * standard_error
    lower_bound = sample_proportion - margin_of_error
    upper_bound = sample_proportion + margin_of_error

    print()
    print("Checks")
    print_checks(
        get_one_proportion_interval_checks(
            sample_size, sample_proportion, population_size
        )
    )
    print()
    print("Setup")
    print(f"- Parameter: p = true proportion of {context}")
    print("- CI: p-hat +/- z*sqrt(p-hat(1-p-hat)/n)")
    print()
    print("Values")
    print(
        f"- p-hat = {successes} / {sample_size} = "
        f"{format_number(sample_proportion)}"
    )
    print(f"- z* = {format_number(z_critical)}")
    print(
        f"- SE = sqrt(({format_number(sample_proportion)})"
        f"({format_number(1 - sample_proportion)}) / {sample_size}) = "
        f"{format_number(standard_error)}"
    )
    print(
        f"- ME = {format_number(z_critical)} * {format_number(standard_error)} = "
        f"{format_number(margin_of_error)}"
    )
    print(
        f"- Interval = ({format_number(lower_bound)}, "
        f"{format_number(upper_bound)})"
    )
    print()
    print("Conclusion")
    print(
        f"We are {format_percent(confidence_level)} confident that the true "
        f"proportion of {context} is between {format_number(lower_bound)} "
        f"and {format_number(upper_bound)}."
    )
    print()


def run_one_mean_t_test():
    print("One-Mean t-Test")
    print("---------------")
    context = get_context()
    sample_mean = get_float("Sample mean x-bar: ")
    sample_sd = get_positive_float("Sample SD s: ")
    sample_size = get_positive_int("Sample size n: ")
    null_mean = get_float("Null mean mu0: ")
    tail = get_tail()
    alpha = get_probability("Alpha (ex: 0.05 or 5): ")
    population_size = get_optional_positive_int(
        "Population size N (Enter if large/unk): "
    )
    shape_is_ok = get_shape_check(sample_size)

    degrees_freedom = sample_size - 1
    standard_error = sample_sd / math.sqrt(sample_size)
    t_statistic = (sample_mean - null_mean) / standard_error
    cumulative_probability = t_cdf(t_statistic, degrees_freedom)
    p_value = tail_p_value(cumulative_probability, tail)

    print()
    print("Checks")
    print_checks(get_one_mean_checks(sample_size, population_size, shape_is_ok))
    print()
    print("Setup")
    print(f"- Parameter: mu = true mean of {context}")
    print(f"- H0: mu = {format_number(null_mean)}")
    print(f"- Ha: mu {tail} {format_number(null_mean)}")
    print()
    print("Values")
    print(
        f"- SE = {format_number(sample_sd)} / sqrt({sample_size}) = "
        f"{format_number(standard_error)}"
    )
    print(
        f"- t = ({format_number(sample_mean)} - {format_number(null_mean)}) / "
        f"{format_number(standard_error)} = {format_number(t_statistic)}"
    )
    print(f"- df = {degrees_freedom}")
    print(f"- p-value = {format_number(p_value)}")
    print()
    print("Conclusion")
    print(test_conclusion(p_value, alpha, "mean", context, tail, null_mean))
    print()


def run_one_mean_t_interval():
    print("One-Mean t-Interval")
    print("-------------------")
    context = get_context()
    sample_mean = get_float("Sample mean x-bar: ")
    sample_sd = get_positive_float("Sample SD s: ")
    sample_size = get_positive_int("Sample size n: ")
    confidence_level = get_confidence_level()
    population_size = get_optional_positive_int(
        "Population size N (Enter if large/unk): "
    )
    shape_is_ok = get_shape_check(sample_size)

    degrees_freedom = sample_size - 1
    standard_error = sample_sd / math.sqrt(sample_size)
    t_critical = inverse_t_cdf((1 + confidence_level) / 2, degrees_freedom)
    margin_of_error = t_critical * standard_error
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error

    print()
    print("Checks")
    print_checks(get_one_mean_checks(sample_size, population_size, shape_is_ok))
    print()
    print("Setup")
    print(f"- Parameter: mu = true mean of {context}")
    print("- CI: x-bar +/- t*(s / sqrt(n))")
    print()
    print("Values")
    print(
        f"- SE = {format_number(sample_sd)} / sqrt({sample_size}) = "
        f"{format_number(standard_error)}"
    )
    print(f"- t* = {format_number(t_critical)}")
    print(
        f"- ME = {format_number(t_critical)} * {format_number(standard_error)} = "
        f"{format_number(margin_of_error)}"
    )
    print(
        f"- Interval = ({format_number(lower_bound)}, "
        f"{format_number(upper_bound)})"
    )
    print(f"- df = {degrees_freedom}")
    print()
    print("Conclusion")
    print(
        f"We are {format_percent(confidence_level)} confident that the true "
        f"mean of {context} is between {format_number(lower_bound)} and "
        f"{format_number(upper_bound)}."
    )
    print()


def run_two_proportion_z_test():
    print("Two-Proportion z-Test")
    print("---------------------")
    group_1, group_2 = get_two_group_contexts()
    successes_1, sample_size_1, successes_2, sample_size_2 = get_two_group_counts()
    tail = get_tail()
    alpha = get_probability("Alpha (ex: 0.05 or 5): ")
    population_size_1 = get_optional_positive_int("Population size N1 (Enter if large/unk): ")
    population_size_2 = get_optional_positive_int("Population size N2 (Enter if large/unk): ")

    sample_proportion_1 = successes_1 / sample_size_1
    sample_proportion_2 = successes_2 / sample_size_2
    pooled_proportion = (successes_1 + successes_2) / (sample_size_1 + sample_size_2)
    standard_error_null = math.sqrt(
        pooled_proportion
        * (1 - pooled_proportion)
        * ((1 / sample_size_1) + (1 / sample_size_2))
    )
    z_statistic = (sample_proportion_1 - sample_proportion_2) / standard_error_null
    p_value = tail_p_value(normal_cdf(z_statistic), tail)

    print()
    print("Checks")
    print_checks(
        get_two_proportion_test_checks(
            sample_size_1,
            sample_size_2,
            pooled_proportion,
            population_size_1,
            population_size_2,
        )
    )
    print()
    print("Setup")
    print(f"- Parameter: p1 - p2 = true proportion of {group_1} minus {group_2}")
    print("- H0: p1 - p2 = 0")
    print(f"- Ha: p1 - p2 {tail} 0")
    print("- Normal approximation used for the z test.")
    print()
    print("Values")
    print(f"- p-hat1 = {successes_1} / {sample_size_1} = {format_number(sample_proportion_1)}")
    print(f"- p-hat2 = {successes_2} / {sample_size_2} = {format_number(sample_proportion_2)}")
    print(
        f"- p-hatc = ({successes_1} + {successes_2}) / "
        f"({sample_size_1} + {sample_size_2}) = {format_number(pooled_proportion)}"
    )
    print(
        f"- SE0 = sqrt(({format_number(pooled_proportion)})"
        f"({format_number(1 - pooled_proportion)})"
        f"(1/{sample_size_1} + 1/{sample_size_2})) = "
        f"{format_number(standard_error_null)}"
    )
    print(
        f"- z = ({format_number(sample_proportion_1)} - "
        f"{format_number(sample_proportion_2)}) / "
        f"{format_number(standard_error_null)} = {format_number(z_statistic)}"
    )
    print(f"- p-value = {format_number(p_value)}")
    print()
    print("Conclusion")
    print(
        test_conclusion(
            p_value,
            alpha,
            "difference in proportions",
            f"{group_1} minus {group_2}",
            tail,
            0.0,
        )
    )
    print()


def run_two_proportion_z_interval():
    print("Two-Proportion z-Interval")
    print("-------------------------")
    group_1, group_2 = get_two_group_contexts()
    successes_1, sample_size_1, successes_2, sample_size_2 = get_two_group_counts()
    confidence_level = get_confidence_level()
    population_size_1 = get_optional_positive_int("Population size N1 (Enter if large/unk): ")
    population_size_2 = get_optional_positive_int("Population size N2 (Enter if large/unk): ")

    sample_proportion_1 = successes_1 / sample_size_1
    sample_proportion_2 = successes_2 / sample_size_2
    difference = sample_proportion_1 - sample_proportion_2
    z_critical = inverse_normal_cdf((1 + confidence_level) / 2)
    standard_error = math.sqrt(
        (sample_proportion_1 * (1 - sample_proportion_1) / sample_size_1)
        + (sample_proportion_2 * (1 - sample_proportion_2) / sample_size_2)
    )
    margin_of_error = z_critical * standard_error
    lower_bound = difference - margin_of_error
    upper_bound = difference + margin_of_error

    print()
    print("Checks")
    print_checks(
        get_two_proportion_interval_checks(
            sample_size_1,
            sample_size_2,
            sample_proportion_1,
            sample_proportion_2,
            population_size_1,
            population_size_2,
        )
    )
    print()
    print("Setup")
    print(f"- Parameter: p1 - p2 = true proportion of {group_1} minus {group_2}")
    print("- CI: (p-hat1 - p-hat2) +/- z*SE")
    print("- Normal approximation used for the z interval.")
    print()
    print("Values")
    print(f"- p-hat1 = {successes_1} / {sample_size_1} = {format_number(sample_proportion_1)}")
    print(f"- p-hat2 = {successes_2} / {sample_size_2} = {format_number(sample_proportion_2)}")
    print(f"- p-hat1 - p-hat2 = {format_number(difference)}")
    print(f"- z* = {format_number(z_critical)}")
    print(
        f"- SE = sqrt(({format_number(sample_proportion_1)})"
        f"({format_number(1 - sample_proportion_1)})/{sample_size_1} + "
        f"({format_number(sample_proportion_2)})"
        f"({format_number(1 - sample_proportion_2)})/{sample_size_2}) = "
        f"{format_number(standard_error)}"
    )
    print(
        f"- ME = {format_number(z_critical)} * {format_number(standard_error)} = "
        f"{format_number(margin_of_error)}"
    )
    print(
        f"- Interval = ({format_number(lower_bound)}, "
        f"{format_number(upper_bound)})"
    )
    print()
    print("Conclusion")
    print(
        f"We are {format_percent(confidence_level)} confident that p1 - p2, "
        f"the true difference in proportions of {group_1} minus {group_2}, "
        f"is between {format_number(lower_bound)} and {format_number(upper_bound)}."
    )
    print()


def run_two_sample_t_test():
    print("Two-Sample t-Test")
    print("-----------------")
    group_1, group_2 = get_two_group_contexts()
    mean_1, sd_1, sample_size_1, mean_2, sd_2, sample_size_2 = get_two_sample_mean_inputs()
    tail = get_tail()
    alpha = get_probability("Alpha (ex: 0.05 or 5): ")
    population_size_1 = get_optional_positive_int("Population size N1 (Enter if large/unk): ")
    population_size_2 = get_optional_positive_int("Population size N2 (Enter if large/unk): ")
    shape_1_ok = get_shape_check_with_label(sample_size_1, "Group 1")
    shape_2_ok = get_shape_check_with_label(sample_size_2, "Group 2")

    difference = mean_1 - mean_2
    standard_error = math.sqrt((sd_1 ** 2 / sample_size_1) + (sd_2 ** 2 / sample_size_2))
    t_statistic = difference / standard_error
    degrees_freedom = welch_degrees_freedom(sd_1, sample_size_1, sd_2, sample_size_2)
    p_value = tail_p_value(t_cdf(t_statistic, degrees_freedom), tail)

    print()
    print("Checks")
    print_checks(
        get_two_mean_checks(
            sample_size_1,
            sample_size_2,
            population_size_1,
            population_size_2,
            shape_1_ok,
            shape_2_ok,
        )
    )
    print()
    print("Setup")
    print(f"- Parameter: mu1 - mu2 = true mean of {group_1} minus {group_2}")
    print("- H0: mu1 - mu2 = 0")
    print(f"- Ha: mu1 - mu2 {tail} 0")
    print()
    print("Values")
    print(f"- x1-bar = {format_number(mean_1)}")
    print(f"- s1 = {format_number(sd_1)}")
    print(f"- n1 = {sample_size_1}")
    print(f"- x2-bar = {format_number(mean_2)}")
    print(f"- s2 = {format_number(sd_2)}")
    print(f"- n2 = {sample_size_2}")
    print(f"- x1-bar - x2-bar = {format_number(difference)}")
    print(
        f"- SE = sqrt({format_number(sd_1 ** 2)}/{sample_size_1} + "
        f"{format_number(sd_2 ** 2)}/{sample_size_2}) = "
        f"{format_number(standard_error)}"
    )
    print(
        f"- t = {format_number(difference)} / {format_number(standard_error)} = "
        f"{format_number(t_statistic)}"
    )
    print(f"- df (Welch approx) = {format_number(degrees_freedom)}")
    print_t_test_pvalue_details(p_value, t_statistic, degrees_freedom, tail, "2-SampTTest")
    print("Conclusion")
    print(
        test_conclusion(
            p_value,
            alpha,
            "difference in means",
            f"{group_1} minus {group_2}",
            tail,
            0.0,
        )
    )
    print()


def run_two_sample_t_interval():
    print("Two-Sample t-Interval")
    print("---------------------")
    group_1, group_2 = get_two_group_contexts()
    mean_1, sd_1, sample_size_1, mean_2, sd_2, sample_size_2 = get_two_sample_mean_inputs()
    confidence_level = get_confidence_level()
    population_size_1 = get_optional_positive_int("Population size N1 (Enter if large/unk): ")
    population_size_2 = get_optional_positive_int("Population size N2 (Enter if large/unk): ")
    shape_1_ok = get_shape_check_with_label(sample_size_1, "Group 1")
    shape_2_ok = get_shape_check_with_label(sample_size_2, "Group 2")

    difference = mean_1 - mean_2
    standard_error = math.sqrt((sd_1 ** 2 / sample_size_1) + (sd_2 ** 2 / sample_size_2))
    degrees_freedom = welch_degrees_freedom(sd_1, sample_size_1, sd_2, sample_size_2)
    t_critical = inverse_t_cdf((1 + confidence_level) / 2, degrees_freedom)
    margin_of_error = t_critical * standard_error
    lower_bound = difference - margin_of_error
    upper_bound = difference + margin_of_error

    print()
    print("Checks")
    print_checks(
        get_two_mean_checks(
            sample_size_1,
            sample_size_2,
            population_size_1,
            population_size_2,
            shape_1_ok,
            shape_2_ok,
        )
    )
    print()
    print("Setup")
    print(f"- Parameter: mu1 - mu2 = true mean of {group_1} minus {group_2}")
    print("- CI: (x1-bar - x2-bar) +/- t*SE")
    print()
    print("Values")
    print(f"- x1-bar - x2-bar = {format_number(difference)}")
    print(
        f"- SE = sqrt({format_number(sd_1 ** 2)}/{sample_size_1} + "
        f"{format_number(sd_2 ** 2)}/{sample_size_2}) = "
        f"{format_number(standard_error)}"
    )
    print(f"- df (Welch approx) = {format_number(degrees_freedom)}")
    print(f"- t* = {format_number(t_critical)}")
    print(
        f"- ME = {format_number(t_critical)} * {format_number(standard_error)} = "
        f"{format_number(margin_of_error)}"
    )
    print(
        f"- Interval = ({format_number(lower_bound)}, "
        f"{format_number(upper_bound)})"
    )
    print()
    print("Conclusion")
    print(
        f"We are {format_percent(confidence_level)} confident that mu1 - mu2, "
        f"the true difference in means of {group_1} minus {group_2}, "
        f"is between {format_number(lower_bound)} and {format_number(upper_bound)}."
    )
    print()


def run_paired_t_test():
    print("Paired t-Test")
    print("-------------")
    difference_context = get_context_with_prompt("Difference context: ")
    mean_difference = get_float("Mean diff d-bar: ")
    sd_difference = get_positive_float("SD of diffs s_d: ")
    sample_size = get_sample_size_for_t("Pairs n: ")
    tail = get_tail()
    alpha = get_probability("Alpha (ex: 0.05 or 5): ")
    population_size = get_optional_positive_int("Population size N (Enter if large/unk): ")
    shape_is_ok = get_shape_check(sample_size)

    degrees_freedom = sample_size - 1
    standard_error = sd_difference / math.sqrt(sample_size)
    t_statistic = mean_difference / standard_error
    p_value = tail_p_value(t_cdf(t_statistic, degrees_freedom), tail)

    print()
    print("Checks")
    print_checks(get_paired_mean_checks(sample_size, population_size, shape_is_ok))
    print()
    print("Setup")
    print(f"- Parameter: mu_d = true mean difference for {difference_context}")
    print("- H0: mu_d = 0")
    print(f"- Ha: mu_d {tail} 0")
    print()
    print("Values")
    print(f"- d-bar = {format_number(mean_difference)}")
    print(f"- s_d = {format_number(sd_difference)}")
    print(
        f"- SE = {format_number(sd_difference)} / sqrt({sample_size}) = "
        f"{format_number(standard_error)}"
    )
    print(
        f"- t = {format_number(mean_difference)} / {format_number(standard_error)} = "
        f"{format_number(t_statistic)}"
    )
    print(f"- df = {degrees_freedom}")
    print_t_test_pvalue_details(p_value, t_statistic, degrees_freedom, tail, "T-Test")
    print("Conclusion")
    print(
        test_conclusion(
            p_value,
            alpha,
            "mean difference",
            difference_context,
            tail,
            0.0,
        )
    )
    print()


def run_paired_t_interval():
    print("Paired t-Interval")
    print("-----------------")
    difference_context = get_context_with_prompt("Difference context: ")
    mean_difference = get_float("Mean diff d-bar: ")
    sd_difference = get_positive_float("SD of diffs s_d: ")
    sample_size = get_sample_size_for_t("Pairs n: ")
    confidence_level = get_confidence_level()
    population_size = get_optional_positive_int("Population size N (Enter if large/unk): ")
    shape_is_ok = get_shape_check(sample_size)

    degrees_freedom = sample_size - 1
    standard_error = sd_difference / math.sqrt(sample_size)
    t_critical = inverse_t_cdf((1 + confidence_level) / 2, degrees_freedom)
    margin_of_error = t_critical * standard_error
    lower_bound = mean_difference - margin_of_error
    upper_bound = mean_difference + margin_of_error

    print()
    print("Checks")
    print_checks(get_paired_mean_checks(sample_size, population_size, shape_is_ok))
    print()
    print("Setup")
    print(f"- Parameter: mu_d = true mean difference for {difference_context}")
    print("- CI: d-bar +/- t*SE")
    print()
    print("Values")
    print(f"- d-bar = {format_number(mean_difference)}")
    print(f"- s_d = {format_number(sd_difference)}")
    print(
        f"- SE = {format_number(sd_difference)} / sqrt({sample_size}) = "
        f"{format_number(standard_error)}"
    )
    print(f"- df = {degrees_freedom}")
    print(f"- t* = {format_number(t_critical)}")
    print(
        f"- ME = {format_number(t_critical)} * {format_number(standard_error)} = "
        f"{format_number(margin_of_error)}"
    )
    print(
        f"- Interval = ({format_number(lower_bound)}, "
        f"{format_number(upper_bound)})"
    )
    print()
    print("Conclusion")
    print(
        f"We are {format_percent(confidence_level)} confident that mu_d, the "
        f"true mean difference for {difference_context}, is between "
        f"{format_number(lower_bound)} and {format_number(upper_bound)}."
    )
    print()


def get_one_proportion_test_checks(sample_size, null_proportion, population_size):
    checks = [("Random", "Ask if the sample/treatment was random.")]
    if population_size:
        checks.append(("10%", pass_fail_text(sample_size <= 0.10 * population_size)))
    else:
        checks.append(("10%", "Need N if sampling w/o replacement."))

    large_counts_pass = (
        sample_size * null_proportion >= 10
        and sample_size * (1 - null_proportion) >= 10
    )
    checks.append(("Large counts", pass_fail_text(large_counts_pass)))
    return checks


def get_one_proportion_interval_checks(
    sample_size, sample_proportion, population_size
):
    checks = [("Random", "Ask if the sample/treatment was random.")]
    if population_size:
        checks.append(("10%", pass_fail_text(sample_size <= 0.10 * population_size)))
    else:
        checks.append(("10%", "Need N if sampling w/o replacement."))

    large_counts_pass = (
        sample_size * sample_proportion >= 10
        and sample_size * (1 - sample_proportion) >= 10
    )
    checks.append(("Large counts", pass_fail_text(large_counts_pass)))
    return checks


def get_one_mean_checks(sample_size, population_size, shape_is_ok):
    checks = [("Random", "Ask if the sample/treatment was random.")]
    if population_size:
        checks.append(("10%", pass_fail_text(sample_size <= 0.10 * population_size)))
    else:
        checks.append(("10%", "Need N if sampling w/o replacement."))

    if sample_size >= 30:
        checks.append(("Normal/Large", "Pass (n >= 30)."))
    else:
        checks.append(("Normal/Large", pass_fail_text(shape_is_ok)))
    return checks


def get_two_proportion_test_checks(
    sample_size_1,
    sample_size_2,
    pooled_proportion,
    population_size_1,
    population_size_2,
):
    checks = [("Random", "Ask if both groups were sampled/assigned randomly.")]
    checks.append(("Independent", "Groups should be independent."))
    checks.extend(get_two_sample_ten_percent_checks(population_size_1, population_size_2, sample_size_1, sample_size_2))
    large_counts_pass = (
        sample_size_1 * pooled_proportion >= 10
        and sample_size_1 * (1 - pooled_proportion) >= 10
        and sample_size_2 * pooled_proportion >= 10
        and sample_size_2 * (1 - pooled_proportion) >= 10
    )
    checks.append(("Large counts", pass_fail_text(large_counts_pass)))
    return checks


def get_two_proportion_interval_checks(
    sample_size_1,
    sample_size_2,
    sample_proportion_1,
    sample_proportion_2,
    population_size_1,
    population_size_2,
):
    checks = [("Random", "Ask if both groups were sampled/assigned randomly.")]
    checks.append(("Independent", "Groups should be independent."))
    checks.extend(get_two_sample_ten_percent_checks(population_size_1, population_size_2, sample_size_1, sample_size_2))
    large_counts_pass = (
        sample_size_1 * sample_proportion_1 >= 10
        and sample_size_1 * (1 - sample_proportion_1) >= 10
        and sample_size_2 * sample_proportion_2 >= 10
        and sample_size_2 * (1 - sample_proportion_2) >= 10
    )
    checks.append(("Large counts", pass_fail_text(large_counts_pass)))
    return checks


def get_two_mean_checks(
    sample_size_1,
    sample_size_2,
    population_size_1,
    population_size_2,
    shape_1_ok,
    shape_2_ok,
):
    checks = [("Random", "Ask if both groups were sampled/assigned randomly.")]
    checks.append(("Independent", "Groups should be independent."))
    checks.extend(get_two_sample_ten_percent_checks(population_size_1, population_size_2, sample_size_1, sample_size_2))
    checks.append(("Normal/Large G1", pass_fail_text(sample_size_1 >= 30 or shape_1_ok)))
    checks.append(("Normal/Large G2", pass_fail_text(sample_size_2 >= 30 or shape_2_ok)))
    return checks


def get_paired_mean_checks(sample_size, population_size, shape_is_ok):
    checks = [("Random", "Ask if the sample/treatment was random.")]
    if population_size:
        checks.append(("10%", pass_fail_text(sample_size <= 0.10 * population_size)))
    else:
        checks.append(("10%", "Need N if sampling w/o replacement."))
    checks.append(("Paired data", "Use differences from matched pairs."))
    checks.append(("Normal/Large", pass_fail_text(sample_size >= 30 or shape_is_ok)))
    return checks


def get_two_sample_ten_percent_checks(
    population_size_1,
    population_size_2,
    sample_size_1,
    sample_size_2,
):
    checks = []
    if population_size_1:
        checks.append(("10% G1", pass_fail_text(sample_size_1 <= 0.10 * population_size_1)))
    else:
        checks.append(("10% G1", "Need N1 if sampling w/o replacement."))
    if population_size_2:
        checks.append(("10% G2", pass_fail_text(sample_size_2 <= 0.10 * population_size_2)))
    else:
        checks.append(("10% G2", "Need N2 if sampling w/o replacement."))
    return checks


def print_checks(checks):
    for check_name, result in checks:
        print(f"- {check_name}: {result}")


def test_conclusion(p_value, alpha, parameter_name, context, tail, null_value):
    decision = "reject H0" if p_value < alpha else "fail to reject H0"
    evidence = "convincing" if p_value < alpha else "not convincing"
    relation = tail_words(tail)
    comparison = "<" if p_value < alpha else ">"
    return (
        f"Since p-value = {format_number(p_value)} {comparison} alpha = "
        f"{format_number(alpha)}, we {decision}. There is {evidence} evidence "
        f"that the true {parameter_name} of {context} is {relation} "
        f"{format_number(null_value)}."
    )


def tail_words(tail):
    if tail == ">":
        return "greater than"
    if tail == "<":
        return "less than"
    return "different from"


def get_context():
    text = input("Context: ").strip()
    if text:
        return text
    return "the population of interest"


def get_context_with_prompt(prompt):
    text = input(prompt).strip()
    if text:
        return text
    return "the population of interest"


def get_two_group_contexts():
    group_1 = get_context_with_prompt("Group 1 context: ")
    group_2 = get_context_with_prompt("Group 2 context: ")
    return group_1, group_2


def get_successes_and_sample_size():
    successes = get_nonnegative_int("Successes x: ")
    sample_size = get_positive_int("Sample size n: ")
    while successes > sample_size:
        print("x cannot be larger than n.")
        successes = get_nonnegative_int("Successes x: ")
        sample_size = get_positive_int("Sample size n: ")
    return successes, sample_size


def get_two_group_counts():
    successes_1 = get_nonnegative_int("Group 1 successes x1: ")
    sample_size_1 = get_positive_int("Group 1 size n1: ")
    while successes_1 > sample_size_1:
        print("x1 cannot be larger than n1.")
        successes_1 = get_nonnegative_int("Group 1 successes x1: ")
        sample_size_1 = get_positive_int("Group 1 size n1: ")

    successes_2 = get_nonnegative_int("Group 2 successes x2: ")
    sample_size_2 = get_positive_int("Group 2 size n2: ")
    while successes_2 > sample_size_2:
        print("x2 cannot be larger than n2.")
        successes_2 = get_nonnegative_int("Group 2 successes x2: ")
        sample_size_2 = get_positive_int("Group 2 size n2: ")

    return successes_1, sample_size_1, successes_2, sample_size_2


def get_two_sample_mean_inputs():
    mean_1 = get_float("Group 1 mean x1-bar: ")
    sd_1 = get_positive_float("Group 1 SD s1: ")
    sample_size_1 = get_sample_size_for_t("Group 1 size n1: ")
    mean_2 = get_float("Group 2 mean x2-bar: ")
    sd_2 = get_positive_float("Group 2 SD s2: ")
    sample_size_2 = get_sample_size_for_t("Group 2 size n2: ")
    return mean_1, sd_1, sample_size_1, mean_2, sd_2, sample_size_2


def get_tail():
    print("Alt hypothesis?")
    print("1) >")
    print("2) <")
    print("3) !=")
    choice = input("Choice: ").strip()
    print()
    if choice == "1":
        return ">"
    if choice == "2":
        return "<"
    if choice == "3":
        return "!="
    print("Using two-sided by default.")
    print()
    return "!="


def get_shape_check(sample_size):
    if sample_size >= 30:
        print("n >= 30, so the large sample check is met.")
        return True
    return ask_yes_no("Normal shape/no strong outliers? (y/n): ")


def get_shape_check_with_label(sample_size, label):
    if sample_size >= 30:
        print(f"{label}: n >= 30, so the large sample check is met.")
        return True
    return ask_yes_no(f"{label} Normal shape/no strong outliers? (y/n): ")


def get_positive_int(prompt):
    while True:
        raw_text = input(prompt).strip()
        if raw_text.isdigit() and int(raw_text) > 0:
            return int(raw_text)
        print("Enter a positive whole number.")


def get_nonnegative_int(prompt):
    while True:
        raw_text = input(prompt).strip()
        if raw_text.isdigit():
            return int(raw_text)
        print("Enter a whole number.")


def get_optional_positive_int(prompt):
    while True:
        raw_text = input(prompt).strip()
        if raw_text == "":
            return None
        if raw_text.isdigit() and int(raw_text) > 0:
            return int(raw_text)
        print("Enter a positive whole number or press Enter.")


def get_float(prompt):
    while True:
        raw_text = input(prompt).strip()
        try:
            return float(raw_text)
        except ValueError:
            print("Enter a number.")


def get_positive_float(prompt):
    while True:
        value = get_float(prompt)
        if value > 0:
            return value
        print("Enter a positive number.")


def get_sample_size_for_t(prompt):
    while True:
        value = get_positive_int(prompt)
        if value >= 2:
            return value
        print("Enter a whole number at least 2.")


def get_probability(prompt):
    while True:
        value = get_float(prompt)
        if 0 < value < 1:
            return value
        if 1 < value < 100:
            return value / 100
        print("Enter a value between 0 and 1, or a percent like 5.")


def get_confidence_level():
    while True:
        value = get_float("Confidence level (ex: 0.95 or 95): ")
        if 0 < value < 1:
            return value
        if 1 < value < 100:
            return value / 100
        print("Enter a value between 0 and 1, or a percent like 95.")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Enter y or n.")


def pass_fail_text(passed):
    return "Pass." if passed else "Fail or check again."


def print_t_test_pvalue_details(
    p_value,
    t_statistic,
    degrees_freedom,
    tail,
    calculator_test_name,
):
    print(f"- p-value (numerical t approx) = {format_number(p_value)}")
    print("- Exact t-model p-values are not built in to plain math code.")
    print(
        f"- Calculator: use {calculator_test_name} or tcdf with "
        f"t = {format_number(t_statistic)} and df ~= {format_number(degrees_freedom)}."
    )
    print(f"- tcdf form: {tcdf_instruction(t_statistic, degrees_freedom, tail)}")


def normal_cdf(z_value):
    return 0.5 * (1 + math.erf(z_value / math.sqrt(2)))


def inverse_normal_cdf(probability):
    # Binary search gives a practical z* estimate without external libraries.
    low = -10.0
    high = 10.0
    for _ in range(80):
        mid = (low + high) / 2
        if normal_cdf(mid) < probability:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def t_cdf(x_value, degrees_freedom):
    if x_value == 0:
        return 0.5
    area = integrate_t_density(0, abs(x_value), degrees_freedom)
    if x_value > 0:
        return min(0.5 + area, 1.0)
    return max(0.5 - area, 0.0)


def inverse_t_cdf(probability, degrees_freedom):
    # Binary search again keeps the implementation simple for calculator porting.
    low = -20.0
    high = 20.0
    for _ in range(80):
        mid = (low + high) / 2
        if t_cdf(mid, degrees_freedom) < probability:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def integrate_t_density(start, end, degrees_freedom):
    if start == end:
        return 0.0

    steps = 600
    if steps % 2 == 1:
        steps += 1

    width = (end - start) / steps
    total = t_density(start, degrees_freedom) + t_density(end, degrees_freedom)

    # Simpson's Rule approximates the area under the t density curve.
    for step in range(1, steps):
        x_value = start + step * width
        if step % 2 == 0:
            total += 2 * t_density(x_value, degrees_freedom)
        else:
            total += 4 * t_density(x_value, degrees_freedom)
    return total * width / 3


def t_density(x_value, degrees_freedom):
    numerator = math.gamma((degrees_freedom + 1) / 2)
    denominator = (
        math.sqrt(degrees_freedom * math.pi) * math.gamma(degrees_freedom / 2)
    )
    exponent = -((degrees_freedom + 1) / 2)
    return (numerator / denominator) * (
        1 + (x_value ** 2) / degrees_freedom
    ) ** exponent


def welch_degrees_freedom(sd_1, sample_size_1, sd_2, sample_size_2):
    part_1 = (sd_1 ** 2) / sample_size_1
    part_2 = (sd_2 ** 2) / sample_size_2
    numerator = (part_1 + part_2) ** 2
    denominator = ((part_1 ** 2) / (sample_size_1 - 1)) + ((part_2 ** 2) / (sample_size_2 - 1))
    return numerator / denominator


def tail_p_value(cumulative_probability, tail):
    if tail == ">":
        return 1 - cumulative_probability
    if tail == "<":
        return cumulative_probability
    return 2 * min(cumulative_probability, 1 - cumulative_probability)


def format_number(value):
    return f"{value:.4f}"


def format_percent(value):
    return f"{value * 100:.1f}%"


def tcdf_instruction(t_statistic, degrees_freedom, tail):
    t_text = format_number(t_statistic)
    df_text = format_number(degrees_freedom)
    if tail == ">":
        return f"tcdf({t_text}, 1E99, {df_text})"
    if tail == "<":
        return f"tcdf(-1E99, {t_text}, {df_text})"
    return f"2*tcdf(abs({t_text}), 1E99, {df_text})"


if __name__ == "__main__":
    main()
