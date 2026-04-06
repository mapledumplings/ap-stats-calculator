import math


PROCEDURES = {
    "1": {
        "name": "One-Proportion z-Test",
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
        "values": ["x", "n", "p0", "tail", "alpha", "context"],
        "calc_values": ["p-hat", "SE0", "z", "p-value"],
        "template": (
            "Since p-value = ___ [< or >] alpha = ___, we [reject or fail "
            "to reject] H0. There is [convincing or not convincing] evidence "
            "that the true proportion of [context] is [relation to p0]."
        ),
    },
    "2": {
        "name": "One-Proportion z-Interval",
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
        "values": ["x", "n", "confidence level", "context"],
        "calc_values": ["p-hat", "z*", "SE", "ME", "interval"],
        "template": (
            "We are ___% confident that the true proportion of [context] is "
            "between ___ and ___."
        ),
    },
    "3": {
        "name": "One-Mean t-Test",
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
        "values": ["x-bar", "s", "n", "mu0", "tail", "alpha", "context"],
        "calc_values": ["SE", "t", "df", "p-value"],
        "template": (
            "Since p-value = ___ [< or >] alpha = ___, we [reject or fail "
            "to reject] H0. There is [convincing or not convincing] evidence "
            "that the true mean of [context] is [relation to mu0]."
        ),
    },
    "4": {
        "name": "One-Mean t-Interval",
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
        "values": ["x-bar", "s", "n", "confidence level", "context"],
        "calc_values": ["SE", "t*", "ME", "interval"],
        "template": (
            "We are ___% confident that the true mean of [context] is "
            "between ___ and ___."
        ),
    },
}

MENU_TO_PROCEDURE = {
    "2": "1",
    "3": "2",
    "4": "3",
    "5": "4",
}


def main():
    while True:
        print_title()
        print("1) Choose procedure")
        print("2) One-prop z-test")
        print("3) One-prop z-int")
        print("4) One-mean t-test")
        print("5) One-mean t-int")
        print("6) Exit")
        choice = input("Choice: ").strip()
        print()

        if choice == "1":
            handle_chooser()
        elif choice in MENU_TO_PROCEDURE:
            run_procedure(MENU_TO_PROCEDURE[choice])
        elif choice == "6":
            print("Bye.")
            break
        else:
            print("Enter 1 to 6.\n")


def print_title():
    print("=" * 33)
    print("AP Stats Inference Helper")
    print("=" * 33)


def handle_chooser():
    print("Data type?")
    print("1) Proportion")
    print("2) Mean")
    data_choice = input("Choice: ").strip()
    print()

    print("Goal?")
    print("1) Test a claim")
    print("2) Build an interval")
    goal_choice = input("Choice: ").strip()
    print()

    key = ""
    if data_choice == "1" and goal_choice == "1":
        key = "1"
    elif data_choice == "1" and goal_choice == "2":
        key = "2"
    elif data_choice == "2" and goal_choice == "1":
        key = "3"
    elif data_choice == "2" and goal_choice == "2":
        key = "4"

    if key:
        print("Use:", PROCEDURES[key]["name"])
        print()
        show_procedure_info(key)
        if ask_yes_no("Compute now? (y/n): "):
            print()
            run_calculation(key)
    else:
        print("Pick valid menu options.\n")


def run_procedure(key):
    show_procedure_info(key)
    if ask_yes_no("Compute now? (y/n): "):
        print()
        run_calculation(key)
    else:
        print()


def show_procedure_info(key):
    info = PROCEDURES[key]
    print(info["name"])
    print("-" * len(info["name"]))
    print("Checks:")
    for item in info["checks"]:
        print("-", item)
    print("Formula/setup:")
    for item in info["formula"]:
        print("-", item)
    print("Need:")
    print("-", ", ".join(info["values"]))
    print("Calc:")
    print("-", ", ".join(info["calc_values"]))
    print("Conclusion template:")
    print("-", info["template"])
    print()


def run_calculation(key):
    if key == "1":
        one_prop_z_test()
    elif key == "2":
        one_prop_z_interval()
    elif key == "3":
        one_mean_t_test()
    elif key == "4":
        one_mean_t_interval()


def one_prop_z_test():
    print("One-Proportion z-Test")
    print("---------------------")
    context = get_context()
    x = get_nonnegative_int("Successes x: ")
    n = get_positive_int("Sample size n: ")
    while x > n:
        print("x cannot be larger than n.")
        x = get_nonnegative_int("Successes x: ")
        n = get_positive_int("Sample size n: ")
    p0 = get_probability("Null proportion p0: ")
    tail = get_tail()
    alpha = get_probability("Alpha (ex: 0.05 or 5): ")
    pop_size = get_optional_positive_int("Population size N (Enter if large/unk): ")

    p_hat = x / n
    se0 = math.sqrt(p0 * (1 - p0) / n)
    z_stat = (p_hat - p0) / se0
    cdf = normal_cdf(z_stat)
    p_value = tail_p_value(cdf, tail)

    print()
    print("Checks")
    print_checks(one_prop_test_checks(n, p0, pop_size))
    print()
    print("Setup")
    print(f"- Parameter: p = true proportion of {context}")
    print(f"- H0: p = {fmt(p0)}")
    print(f"- Ha: p {tail} {fmt(p0)}")
    print()
    print("Values")
    print(f"- p-hat = {x} / {n} = {fmt(p_hat)}")
    print(f"- SE0 = sqrt(({fmt(p0)})({fmt(1 - p0)}) / {n}) = {fmt(se0)}")
    print(f"- z = ({fmt(p_hat)} - {fmt(p0)}) / {fmt(se0)} = {fmt(z_stat)}")
    print(f"- p-value = {fmt(p_value)}")
    print()
    print("Conclusion")
    print(test_conclusion(p_value, alpha, "proportion", context, tail, p0))
    print()


def one_prop_z_interval():
    print("One-Proportion z-Interval")
    print("-------------------------")
    context = get_context()
    x = get_nonnegative_int("Successes x: ")
    n = get_positive_int("Sample size n: ")
    while x > n:
        print("x cannot be larger than n.")
        x = get_nonnegative_int("Successes x: ")
        n = get_positive_int("Sample size n: ")
    conf = get_confidence_level()
    pop_size = get_optional_positive_int("Population size N (Enter if large/unk): ")

    p_hat = x / n
    z_star = inverse_normal_cdf((1 + conf) / 2)
    se = math.sqrt(p_hat * (1 - p_hat) / n)
    me = z_star * se
    low = p_hat - me
    high = p_hat + me

    print()
    print("Checks")
    print_checks(one_prop_interval_checks(n, p_hat, pop_size))
    print()
    print("Setup")
    print(f"- Parameter: p = true proportion of {context}")
    print(f"- CI: p-hat +/- z*sqrt(p-hat(1-p-hat)/n)")
    print()
    print("Values")
    print(f"- p-hat = {x} / {n} = {fmt(p_hat)}")
    print(f"- z* = {fmt(z_star)}")
    print(f"- SE = sqrt(({fmt(p_hat)})({fmt(1 - p_hat)}) / {n}) = {fmt(se)}")
    print(f"- ME = {fmt(z_star)} * {fmt(se)} = {fmt(me)}")
    print(f"- Interval = ({fmt(low)}, {fmt(high)})")
    print()
    print("Conclusion")
    print(
        f"We are {fmt_percent(conf)} confident that the true proportion of "
        f"{context} is between {fmt(low)} and {fmt(high)}."
    )
    print()


def one_mean_t_test():
    print("One-Mean t-Test")
    print("---------------")
    context = get_context()
    x_bar = get_float("Sample mean x-bar: ")
    s = get_positive_float("Sample SD s: ")
    n = get_positive_int("Sample size n: ")
    mu0 = get_float("Null mean mu0: ")
    tail = get_tail()
    alpha = get_probability("Alpha (ex: 0.05 or 5): ")
    pop_size = get_optional_positive_int("Population size N (Enter if large/unk): ")
    shape_ok = get_shape_check(n)

    df = n - 1
    se = s / math.sqrt(n)
    t_stat = (x_bar - mu0) / se
    cdf = t_cdf(t_stat, df)
    p_value = tail_p_value(cdf, tail)

    print()
    print("Checks")
    print_checks(one_mean_checks(n, pop_size, shape_ok))
    print()
    print("Setup")
    print(f"- Parameter: mu = true mean of {context}")
    print(f"- H0: mu = {fmt(mu0)}")
    print(f"- Ha: mu {tail} {fmt(mu0)}")
    print()
    print("Values")
    print(f"- SE = {fmt(s)} / sqrt({n}) = {fmt(se)}")
    print(f"- t = ({fmt(x_bar)} - {fmt(mu0)}) / {fmt(se)} = {fmt(t_stat)}")
    print(f"- df = {df}")
    print(f"- p-value = {fmt(p_value)}")
    print()
    print("Conclusion")
    print(test_conclusion(p_value, alpha, "mean", context, tail, mu0))
    print()


def one_mean_t_interval():
    print("One-Mean t-Interval")
    print("-------------------")
    context = get_context()
    x_bar = get_float("Sample mean x-bar: ")
    s = get_positive_float("Sample SD s: ")
    n = get_positive_int("Sample size n: ")
    conf = get_confidence_level()
    pop_size = get_optional_positive_int("Population size N (Enter if large/unk): ")
    shape_ok = get_shape_check(n)

    df = n - 1
    se = s / math.sqrt(n)
    t_star = inverse_t_cdf((1 + conf) / 2, df)
    me = t_star * se
    low = x_bar - me
    high = x_bar + me

    print()
    print("Checks")
    print_checks(one_mean_checks(n, pop_size, shape_ok))
    print()
    print("Setup")
    print(f"- Parameter: mu = true mean of {context}")
    print(f"- CI: x-bar +/- t*(s / sqrt(n))")
    print()
    print("Values")
    print(f"- SE = {fmt(s)} / sqrt({n}) = {fmt(se)}")
    print(f"- t* = {fmt(t_star)}")
    print(f"- ME = {fmt(t_star)} * {fmt(se)} = {fmt(me)}")
    print(f"- Interval = ({fmt(low)}, {fmt(high)})")
    print(f"- df = {df}")
    print()
    print("Conclusion")
    print(
        f"We are {fmt_percent(conf)} confident that the true mean of "
        f"{context} is between {fmt(low)} and {fmt(high)}."
    )
    print()


def one_prop_test_checks(n, p0, pop_size):
    checks = []
    checks.append(("Random", "Ask if the sample/treatment was random."))
    if pop_size:
        checks.append(("10%", pass_fail_text(n <= 0.10 * pop_size)))
    else:
        checks.append(("10%", "Need N if sampling w/o replacement."))
    large_counts = n * p0 >= 10 and n * (1 - p0) >= 10
    checks.append(("Large counts", pass_fail_text(large_counts)))
    return checks


def one_prop_interval_checks(n, p_hat, pop_size):
    checks = []
    checks.append(("Random", "Ask if the sample/treatment was random."))
    if pop_size:
        checks.append(("10%", pass_fail_text(n <= 0.10 * pop_size)))
    else:
        checks.append(("10%", "Need N if sampling w/o replacement."))
    large_counts = n * p_hat >= 10 and n * (1 - p_hat) >= 10
    checks.append(("Large counts", pass_fail_text(large_counts)))
    return checks


def one_mean_checks(n, pop_size, shape_ok):
    checks = []
    checks.append(("Random", "Ask if the sample/treatment was random."))
    if pop_size:
        checks.append(("10%", pass_fail_text(n <= 0.10 * pop_size)))
    else:
        checks.append(("10%", "Need N if sampling w/o replacement."))
    if n >= 30:
        checks.append(("Normal/Large", "Pass (n >= 30)."))
    else:
        checks.append(("Normal/Large", pass_fail_text(shape_ok)))
    return checks


def print_checks(checks):
    for name, result in checks:
        print(f"- {name}: {result}")


def test_conclusion(p_value, alpha, parameter_name, context, tail, null_value):
    decision = "reject H0" if p_value < alpha else "fail to reject H0"
    evidence = "convincing" if p_value < alpha else "not convincing"
    relation = tail_words(tail, null_value)
    return (
        f"Since p-value = {fmt(p_value)} "
        f"{'<' if p_value < alpha else '>'} alpha = {fmt(alpha)}, we "
        f"{decision}. There is {evidence} evidence that the true "
        f"{parameter_name} of {context} is {relation} {fmt(null_value)}."
    )


def tail_words(tail, value):
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


def get_shape_check(n):
    if n >= 30:
        print("n >= 30, so the large sample check is met.")
        return True
    return ask_yes_no("Normal shape/no strong outliers? (y/n): ")


def get_positive_int(prompt):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Enter a positive whole number.")


def get_nonnegative_int(prompt):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit():
            return int(raw)
        print("Enter a whole number.")


def get_optional_positive_int(prompt):
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return None
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Enter a positive whole number or press Enter.")


def get_float(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Enter a number.")


def get_positive_float(prompt):
    while True:
        value = get_float(prompt)
        if value > 0:
            return value
        print("Enter a positive number.")


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


def normal_cdf(z_value):
    return 0.5 * (1 + math.erf(z_value / math.sqrt(2)))


def inverse_normal_cdf(prob):
    low = -10.0
    high = 10.0
    for _ in range(80):
        mid = (low + high) / 2
        if normal_cdf(mid) < prob:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def t_cdf(x_value, df):
    if x_value == 0:
        return 0.5
    area = integrate_t_density(0, abs(x_value), df)
    if x_value > 0:
        return min(0.5 + area, 1.0)
    return max(0.5 - area, 0.0)


def inverse_t_cdf(prob, df):
    low = -20.0
    high = 20.0
    for _ in range(80):
        mid = (low + high) / 2
        if t_cdf(mid, df) < prob:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def integrate_t_density(a_value, b_value, df):
    if a_value == b_value:
        return 0.0
    steps = 600
    if steps % 2 == 1:
        steps += 1
    width = (b_value - a_value) / steps
    total = t_density(a_value, df) + t_density(b_value, df)
    for i in range(1, steps):
        x_value = a_value + i * width
        if i % 2 == 0:
            total += 2 * t_density(x_value, df)
        else:
            total += 4 * t_density(x_value, df)
    return total * width / 3


def t_density(x_value, df):
    top = math.gamma((df + 1) / 2)
    bottom = math.sqrt(df * math.pi) * math.gamma(df / 2)
    power = -((df + 1) / 2)
    return (top / bottom) * (1 + (x_value ** 2) / df) ** power


def tail_p_value(cdf, tail):
    if tail == ">":
        return 1 - cdf
    if tail == "<":
        return cdf
    return 2 * min(cdf, 1 - cdf)


def fmt(value):
    return f"{value:.4f}"


def fmt_percent(value):
    return f"{value * 100:.1f}%"


if __name__ == "__main__":
    main()
