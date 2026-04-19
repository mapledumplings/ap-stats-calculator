"""Compact TI-84 Plus CE Python version of the AP Stats calculator.

TI notes:
- Send this file to the calculator instead of the full desktop file.
- Keep it in RAM.
- Menus are numeric and text is shortened on purpose.
- Two-sample t uses conservative df = min(n1-1, n2-1).
- t p-values use numerical integration, not an exact built-in t CDF.
"""

import math


def main():
    while True:
        title()
        print("1) TREE")
        print("2) EXIT")
        ch = input("CHOICE: ").strip()
        print()
        if ch == "1":
            proc = choose_proc()
            if proc == "":
                print("NO MATCH")
                print()
            elif proc == "PAIR_PROP":
                print("PAIRED CATEGORICAL")
                print("NOT IN THIS APP")
                print()
            else:
                open_proc(proc)
        elif ch == "2":
            print("BYE")
            break
        else:
            print("ENTER 1 OR 2")
            print()


def title():
    print("====================")
    print("AP STATS TI HELPER")
    print("====================")


def choose_proc():
    goal = choose_goal()
    dtype = choose_dtype()
    stype = choose_stype()
    if dtype == "P" and stype == "P":
        return "PAIR_PROP"
    if goal == "T" and dtype == "P" and stype == "1":
        return "1PZTEST"
    if goal == "I" and dtype == "P" and stype == "1":
        return "1PZINT"
    if goal == "T" and dtype == "M" and stype == "1":
        return "1TTEST"
    if goal == "I" and dtype == "M" and stype == "1":
        return "1TINT"
    if goal == "T" and dtype == "P" and stype == "2":
        return "2PZTEST"
    if goal == "I" and dtype == "P" and stype == "2":
        return "2PZINT"
    if goal == "T" and dtype == "M" and stype == "2":
        return "2TTEST"
    if goal == "I" and dtype == "M" and stype == "2":
        return "2TINT"
    if goal == "T" and dtype == "M" and stype == "P":
        return "PTTEST"
    if goal == "I" and dtype == "M" and stype == "P":
        return "PTINT"
    return ""


def choose_goal():
    print("GOAL?")
    print("1) INT")
    print("2) TEST")
    ch = input("CHOICE: ").strip()
    print()
    if ch == "1":
        return "I"
    return "T"


def choose_dtype():
    print("TYPE?")
    print("1) PROP")
    print("2) MEAN")
    ch = input("CHOICE: ").strip()
    print()
    if ch == "1":
        return "P"
    return "M"


def choose_stype():
    print("DATA?")
    print("1) ONE")
    print("2) TWO IND")
    print("3) PAIRED")
    ch = input("CHOICE: ").strip()
    print()
    if ch == "1":
        return "1"
    if ch == "2":
        return "2"
    return "P"


def open_proc(proc):
    print(proc_name(proc))
    print()
    show_info(proc)
    if ask_yes_no("COMPUTE? Y/N: "):
        print()
        run_proc(proc)
    else:
        print()


def proc_name(proc):
    if proc == "1PZTEST":
        return "1-PROP Z TEST"
    if proc == "1PZINT":
        return "1-PROP Z INT"
    if proc == "1TTEST":
        return "1-MEAN T TEST"
    if proc == "1TINT":
        return "1-MEAN T INT"
    if proc == "2PZTEST":
        return "2-PROP Z TEST"
    if proc == "2PZINT":
        return "2-PROP Z INT"
    if proc == "2TTEST":
        return "2-SAMP T TEST"
    if proc == "2TINT":
        return "2-SAMP T INT"
    if proc == "PTTEST":
        return "PAIRED T TEST"
    return "PAIRED T INT"


def show_info(proc):
    print("CHECKS")
    if proc == "1PZTEST":
        show_lines(["RAND", "10%", "LARGE CTS H0"])
        print("FORM")
        show_lines(["p", "H0:p=p0", "z=(ph-p0)/SE0"])
    elif proc == "1PZINT":
        show_lines(["RAND", "10%", "LARGE CTS"])
        print("FORM")
        show_lines(["p", "CI: ph +- z*SE"])
    elif proc == "1TTEST":
        show_lines(["RAND", "10%", "NORMAL/LARGE"])
        print("FORM")
        show_lines(["mu", "H0:mu=mu0", "t=(xb-mu0)/SE"])
    elif proc == "1TINT":
        show_lines(["RAND", "10%", "NORMAL/LARGE"])
        print("FORM")
        show_lines(["mu", "CI: xb +- t*SE"])
    elif proc == "2PZTEST":
        show_lines(["RAND BOTH", "INDEP", "10% BOTH", "POOL CTS"])
        print("FORM")
        show_lines(["p1-p2", "H0:p1-p2=0", "z=(ph1-ph2)/SE0"])
    elif proc == "2PZINT":
        show_lines(["RAND BOTH", "INDEP", "10% BOTH", "LARGE CTS"])
        print("FORM")
        show_lines(["p1-p2", "CI: (ph1-ph2)+-z*SE"])
    elif proc == "2TTEST":
        show_lines(["RAND BOTH", "INDEP", "10% BOTH", "NORMAL/LARGE"])
        print("FORM")
        show_lines(["mu1-mu2", "H0:mu1-mu2=0", "t=(xb1-xb2)/SE"])
    elif proc == "2TINT":
        show_lines(["RAND BOTH", "INDEP", "10% BOTH", "NORMAL/LARGE"])
        print("FORM")
        show_lines(["mu1-mu2", "CI: (xb1-xb2)+-t*SE"])
    elif proc == "PTTEST":
        show_lines(["RAND", "10%", "USE DIFFS", "NORMAL/LARGE"])
        print("FORM")
        show_lines(["mu_d", "H0:mu_d=0", "t=dbar/SE"])
    elif proc == "PTINT":
        show_lines(["RAND", "10%", "USE DIFFS", "NORMAL/LARGE"])
        print("FORM")
        show_lines(["mu_d", "CI: dbar +- t*SE"])
    print()


def show_lines(items):
    i = 0
    while i < len(items):
        print("- " + items[i])
        i = i + 1


def run_proc(proc):
    if proc == "1PZTEST":
        run_1pztest()
    elif proc == "1PZINT":
        run_1pzint()
    elif proc == "1TTEST":
        run_1ttest()
    elif proc == "1TINT":
        run_1tint()
    elif proc == "2PZTEST":
        run_2pztest()
    elif proc == "2PZINT":
        run_2pzint()
    elif proc == "2TTEST":
        run_2ttest()
    elif proc == "2TINT":
        run_2tint()
    elif proc == "PTTEST":
        run_pttest()
    elif proc == "PTINT":
        run_ptint()


def run_1pztest():
    ctx = get_text("CTX: ", "POP")
    x = get_nonneg_int("X: ")
    n = get_pos_int("N: ")
    while x > n:
        print("X > N")
        x = get_nonneg_int("X: ")
        n = get_pos_int("N: ")
    p0 = get_prob("P0: ")
    tail = get_tail()
    alpha = get_prob("A: ")
    pop = get_opt_pos_int("POP N: ")
    ph = x / n
    se0 = math.sqrt(p0 * (1 - p0) / n)
    z = (ph - p0) / se0
    pv = z_pv(z, tail)
    print()
    print("CHECKS")
    show_checks_1p_test(n, p0, pop)
    print("SETUP")
    print("- p = true prop of " + ctx)
    print("- H0: p = " + fmt(p0))
    print("- Ha: p " + tail + " " + fmt(p0))
    print("VALS")
    print("- ph = " + fmt(ph))
    print("- SE0 = " + fmt(se0))
    print("- z = " + fmt(z))
    print("- ALT = " + tail)
    print("- PV = " + fmt(pv))
    print_conc(test_conc(pv, alpha, "proportion", ctx, tail, 0, p0))


def run_1pzint():
    ctx = get_text("CTX: ", "POP")
    x = get_nonneg_int("X: ")
    n = get_pos_int("N: ")
    while x > n:
        print("X > N")
        x = get_nonneg_int("X: ")
        n = get_pos_int("N: ")
    conf = get_conf()
    pop = get_opt_pos_int("POP N: ")
    ph = x / n
    zc = inv_norm((1 + conf) / 2)
    se = math.sqrt(ph * (1 - ph) / n)
    me = zc * se
    lo = ph - me
    hi = ph + me
    print()
    print("CHECKS")
    show_checks_1p_int(n, ph, pop)
    print("SETUP")
    print("- p = true prop of " + ctx)
    print("- CI: ph +- z*SE")
    print("VALS")
    print("- ph = " + fmt(ph))
    print("- z* = " + fmt(zc))
    print("- SE = " + fmt(se))
    print("- ME = " + fmt(me))
    print("- INT = (" + fmt(lo) + ", " + fmt(hi) + ")")
    print_conc("We are " + pct(conf) + " conf true prop of " + ctx + " is between " + fmt(lo) + " and " + fmt(hi) + ".")


def run_1ttest():
    ctx = get_text("CTX: ", "POP")
    xb = get_num("XBAR: ")
    s = get_pos_num("S: ")
    n = get_n_t("N: ")
    mu0 = get_num("MU0: ")
    tail = get_tail()
    alpha = get_prob("A: ")
    pop = get_opt_pos_int("POP N: ")
    shape = get_shape(n)
    df = n - 1
    se = s / math.sqrt(n)
    t = (xb - mu0) / se
    pv = t_pv(t, df, tail)
    print()
    print("CHECKS")
    show_checks_1m(n, pop, shape)
    print("SETUP")
    print("- mu = true mean of " + ctx)
    print("- H0: mu = " + fmt(mu0))
    print("- Ha: mu " + tail + " " + fmt(mu0))
    print("VALS")
    print("- SE = " + fmt(se))
    print("- t = " + fmt(t))
    print("- df = " + str(df))
    print("- ALT = " + tail)
    print("- PV = " + fmt(pv) + " approx")
    print("- use tcdf for calc")
    print("- " + tcdf_text(t, df, tail))
    print_conc(test_conc(pv, alpha, "mean", ctx, tail, 0, mu0))


def run_1tint():
    ctx = get_text("CTX: ", "POP")
    xb = get_num("XBAR: ")
    s = get_pos_num("S: ")
    n = get_n_t("N: ")
    conf = get_conf()
    pop = get_opt_pos_int("POP N: ")
    shape = get_shape(n)
    df = n - 1
    se = s / math.sqrt(n)
    tc = inv_t((1 + conf) / 2, df)
    me = tc * se
    lo = xb - me
    hi = xb + me
    print()
    print("CHECKS")
    show_checks_1m(n, pop, shape)
    print("SETUP")
    print("- mu = true mean of " + ctx)
    print("- CI: xbar +- t*SE")
    print("VALS")
    print("- SE = " + fmt(se))
    print("- df = " + str(df))
    print("- t* = " + fmt(tc))
    print("- ME = " + fmt(me))
    print("- INT = (" + fmt(lo) + ", " + fmt(hi) + ")")
    print_conc("We are " + pct(conf) + " conf true mean of " + ctx + " is between " + fmt(lo) + " and " + fmt(hi) + ".")


def run_2pztest():
    g1 = get_text("G1: ", "G1")
    g2 = get_text("G2: ", "G2")
    x1, n1, x2, n2 = get_2counts()
    tail = get_tail()
    alpha = get_prob("A: ")
    pop1 = get_opt_pos_int("N1POP: ")
    pop2 = get_opt_pos_int("N2POP: ")
    ph1 = x1 / n1
    ph2 = x2 / n2
    phc = (x1 + x2) / (n1 + n2)
    se0 = math.sqrt(phc * (1 - phc) * ((1 / n1) + (1 / n2)))
    z = (ph1 - ph2) / se0
    pv = z_pv(z, tail)
    print()
    print("CHECKS")
    show_checks_2p_test(n1, n2, phc, pop1, pop2)
    print("SETUP")
    print("- p1-p2 true prop diff")
    print("- H0: p1-p2 = 0")
    print("- Ha: p1-p2 " + tail + " 0")
    print("- normal approx")
    print("VALS")
    print("- ph1 = " + fmt(ph1))
    print("- ph2 = " + fmt(ph2))
    print("- phc = " + fmt(phc))
    print("- SE0 = " + fmt(se0))
    print("- z = " + fmt(z))
    print("- ALT = " + tail)
    print("- PV = " + fmt(pv))
    print_conc(test_conc(pv, alpha, "prop diff", g1 + " minus " + g2, tail, 1, 0.0))


def run_2pzint():
    g1 = get_text("G1: ", "G1")
    g2 = get_text("G2: ", "G2")
    x1, n1, x2, n2 = get_2counts()
    conf = get_conf()
    pop1 = get_opt_pos_int("N1POP: ")
    pop2 = get_opt_pos_int("N2POP: ")
    ph1 = x1 / n1
    ph2 = x2 / n2
    diff = ph1 - ph2
    zc = inv_norm((1 + conf) / 2)
    se = math.sqrt(ph1 * (1 - ph1) / n1 + ph2 * (1 - ph2) / n2)
    me = zc * se
    lo = diff - me
    hi = diff + me
    print()
    print("CHECKS")
    show_checks_2p_int(n1, n2, ph1, ph2, pop1, pop2)
    print("SETUP")
    print("- p1-p2 true prop diff")
    print("- CI: diff +- z*SE")
    print("- normal approx")
    print("VALS")
    print("- ph1 = " + fmt(ph1))
    print("- ph2 = " + fmt(ph2))
    print("- diff = " + fmt(diff))
    print("- z* = " + fmt(zc))
    print("- SE = " + fmt(se))
    print("- ME = " + fmt(me))
    print("- INT = (" + fmt(lo) + ", " + fmt(hi) + ")")
    print_conc("We are " + pct(conf) + " conf true prop diff of " + g1 + " minus " + g2 + " is between " + fmt(lo) + " and " + fmt(hi) + ".")


def run_2ttest():
    g1 = get_text("G1: ", "G1")
    g2 = get_text("G2: ", "G2")
    xb1, s1, n1, xb2, s2, n2 = get_2means()
    tail = get_tail()
    alpha = get_prob("A: ")
    pop1 = get_opt_pos_int("N1POP: ")
    pop2 = get_opt_pos_int("N2POP: ")
    sh1 = get_shape_lab(n1, "G1")
    sh2 = get_shape_lab(n2, "G2")
    diff = xb1 - xb2
    se = math.sqrt((s1 * s1 / n1) + (s2 * s2 / n2))
    t = diff / se
    df = cons_df(n1, n2)
    pv = t_pv(t, df, tail)
    print()
    print("CHECKS")
    show_checks_2m(n1, n2, pop1, pop2, sh1, sh2)
    print("SETUP")
    print("- mu1-mu2 true mean diff")
    print("- H0: mu1-mu2 = 0")
    print("- Ha: mu1-mu2 " + tail + " 0")
    print("VALS")
    print("- xb1 = " + fmt(xb1))
    print("- s1 = " + fmt(s1))
    print("- n1 = " + str(n1))
    print("- xb2 = " + fmt(xb2))
    print("- s2 = " + fmt(s2))
    print("- n2 = " + str(n2))
    print("- diff = " + fmt(diff))
    print("- SE = " + fmt(se))
    print("- t = " + fmt(t))
    print("- df = " + str(df))
    print("- ALT = " + tail)
    print("- PV = " + fmt(pv) + " approx")
    print("- use 2-SampTTest/tcdf")
    print("- " + tcdf_text(t, df, tail))
    print_conc(test_conc(pv, alpha, "mean diff", g1 + " minus " + g2, tail, 1, 0.0))


def run_2tint():
    g1 = get_text("G1: ", "G1")
    g2 = get_text("G2: ", "G2")
    xb1, s1, n1, xb2, s2, n2 = get_2means()
    conf = get_conf()
    pop1 = get_opt_pos_int("N1POP: ")
    pop2 = get_opt_pos_int("N2POP: ")
    sh1 = get_shape_lab(n1, "G1")
    sh2 = get_shape_lab(n2, "G2")
    diff = xb1 - xb2
    se = math.sqrt((s1 * s1 / n1) + (s2 * s2 / n2))
    df = cons_df(n1, n2)
    tc = inv_t((1 + conf) / 2, df)
    me = tc * se
    lo = diff - me
    hi = diff + me
    print()
    print("CHECKS")
    show_checks_2m(n1, n2, pop1, pop2, sh1, sh2)
    print("SETUP")
    print("- mu1-mu2 true mean diff")
    print("- CI: diff +- t*SE")
    print("VALS")
    print("- diff = " + fmt(diff))
    print("- SE = " + fmt(se))
    print("- df = " + str(df))
    print("- t* = " + fmt(tc))
    print("- ME = " + fmt(me))
    print("- INT = (" + fmt(lo) + ", " + fmt(hi) + ")")
    print_conc("We are " + pct(conf) + " conf true mean diff of " + g1 + " minus " + g2 + " is between " + fmt(lo) + " and " + fmt(hi) + ".")


def run_pttest():
    ctx = get_text("DIFF CTX: ", "DIFF")
    dbar = get_num("DBAR: ")
    sd = get_pos_num("SD: ")
    n = get_n_t("N: ")
    tail = get_tail()
    alpha = get_prob("A: ")
    pop = get_opt_pos_int("POP N: ")
    shape = get_shape(n)
    df = n - 1
    se = sd / math.sqrt(n)
    t = dbar / se
    pv = t_pv(t, df, tail)
    print()
    print("CHECKS")
    show_checks_pm(n, pop, shape)
    print("SETUP")
    print("- mu_d true mean diff")
    print("- H0: mu_d = 0")
    print("- Ha: mu_d " + tail + " 0")
    print("VALS")
    print("- dbar = " + fmt(dbar))
    print("- s_d = " + fmt(sd))
    print("- SE = " + fmt(se))
    print("- t = " + fmt(t))
    print("- df = " + str(df))
    print("- ALT = " + tail)
    print("- PV = " + fmt(pv) + " approx")
    print("- use T-Test/tcdf")
    print("- " + tcdf_text(t, df, tail))
    print_conc(test_conc(pv, alpha, "mean diff", ctx, tail, 0, 0.0))


def run_ptint():
    ctx = get_text("DIFF CTX: ", "DIFF")
    dbar = get_num("DBAR: ")
    sd = get_pos_num("SD: ")
    n = get_n_t("N: ")
    conf = get_conf()
    pop = get_opt_pos_int("POP N: ")
    shape = get_shape(n)
    df = n - 1
    se = sd / math.sqrt(n)
    tc = inv_t((1 + conf) / 2, df)
    me = tc * se
    lo = dbar - me
    hi = dbar + me
    print()
    print("CHECKS")
    show_checks_pm(n, pop, shape)
    print("SETUP")
    print("- mu_d true mean diff")
    print("- CI: dbar +- t*SE")
    print("VALS")
    print("- dbar = " + fmt(dbar))
    print("- s_d = " + fmt(sd))
    print("- SE = " + fmt(se))
    print("- df = " + str(df))
    print("- t* = " + fmt(tc))
    print("- ME = " + fmt(me))
    print("- INT = (" + fmt(lo) + ", " + fmt(hi) + ")")
    print_conc("We are " + pct(conf) + " conf true mean diff for " + ctx + " is between " + fmt(lo) + " and " + fmt(hi) + ".")


def show_checks_1p_test(n, p0, pop):
    check_rand()
    check_10(pop, n, "")
    ok = n * p0 >= 10 and n * (1 - p0) >= 10
    show_pf("LARGE", ok)


def show_checks_1p_int(n, ph, pop):
    check_rand()
    check_10(pop, n, "")
    ok = n * ph >= 10 and n * (1 - ph) >= 10
    show_pf("LARGE", ok)


def show_checks_1m(n, pop, shape):
    check_rand()
    check_10(pop, n, "")
    if n >= 30:
        show_pf("NORM/LARGE", 1)
    else:
        show_pf("NORM/LARGE", shape)


def show_checks_2p_test(n1, n2, phc, pop1, pop2):
    print("- RAND BOTH")
    print("- INDEP")
    check_10(pop1, n1, " G1")
    check_10(pop2, n2, " G2")
    ok = 1
    if n1 * phc < 10 or n1 * (1 - phc) < 10:
        ok = 0
    if n2 * phc < 10 or n2 * (1 - phc) < 10:
        ok = 0
    show_pf("POOL CTS", ok)


def show_checks_2p_int(n1, n2, ph1, ph2, pop1, pop2):
    print("- RAND BOTH")
    print("- INDEP")
    check_10(pop1, n1, " G1")
    check_10(pop2, n2, " G2")
    ok = 1
    if n1 * ph1 < 10 or n1 * (1 - ph1) < 10:
        ok = 0
    if n2 * ph2 < 10 or n2 * (1 - ph2) < 10:
        ok = 0
    show_pf("LARGE", ok)


def show_checks_2m(n1, n2, pop1, pop2, sh1, sh2):
    print("- RAND BOTH")
    print("- INDEP")
    check_10(pop1, n1, " G1")
    check_10(pop2, n2, " G2")
    if n1 >= 30:
        show_pf("NORM G1", 1)
    else:
        show_pf("NORM G1", sh1)
    if n2 >= 30:
        show_pf("NORM G2", 1)
    else:
        show_pf("NORM G2", sh2)


def show_checks_pm(n, pop, shape):
    check_rand()
    check_10(pop, n, "")
    print("- USE DIFFS")
    if n >= 30:
        show_pf("NORM/LARGE", 1)
    else:
        show_pf("NORM/LARGE", shape)


def check_rand():
    print("- RAND")


def check_10(pop, n, suf):
    lab = "10%" + suf
    if pop is None:
        print("- " + lab + ": NEED POP")
    else:
        show_pf(lab, n <= 0.10 * pop)


def show_pf(label, ok):
    if ok:
        print("- " + label + ": PASS")
    else:
        print("- " + label + ": FAIL/CHECK")


def test_conc(pv, alpha, pname, ctx, tail, is_diff, nullv):
    if pv < alpha:
        d = "reject H0"
        e = "convincing"
        c = "<"
    else:
        d = "fail to reject H0"
        e = "not convincing"
        c = ">"
    rel = tail_word(tail)
    txt = "Since p-value = " + fmt(pv) + " " + c
    txt = txt + " alpha = " + fmt(alpha) + ", we " + d + ". "
    txt = txt + "There is " + e + " evidence that the true "
    txt = txt + pname + " of " + ctx + " is " + rel + " "
    txt = txt + fmt(nullv) + "."
    return txt


def tail_word(tail):
    if tail == ">":
        return "greater than"
    if tail == "<":
        return "less than"
    return "different from"


def print_conc(text):
    print("CONC")
    print(text)
    print()


def get_text(prompt, default):
    t = input(prompt).strip()
    if t == "":
        return default
    return t


def get_2counts():
    x1 = get_nonneg_int("X1: ")
    n1 = get_pos_int("N1: ")
    while x1 > n1:
        print("X1 > N1")
        x1 = get_nonneg_int("X1: ")
        n1 = get_pos_int("N1: ")
    x2 = get_nonneg_int("X2: ")
    n2 = get_pos_int("N2: ")
    while x2 > n2:
        print("X2 > N2")
        x2 = get_nonneg_int("X2: ")
        n2 = get_pos_int("N2: ")
    return x1, n1, x2, n2


def get_2means():
    xb1 = get_num("XB1: ")
    s1 = get_pos_num("S1: ")
    n1 = get_n_t("N1: ")
    xb2 = get_num("XB2: ")
    s2 = get_pos_num("S2: ")
    n2 = get_n_t("N2: ")
    return xb1, s1, n1, xb2, s2, n2


def get_tail():
    print("ALT?")
    print("1) >")
    print("2) <")
    print("3) !=")
    ch = input("CHOICE: ").strip()
    print()
    if ch == "1":
        return ">"
    if ch == "2":
        return "<"
    return "!="


def get_shape(n):
    if n >= 30:
        print("N >= 30")
        return 1
    return ask_yes_no("OK SHAPE? Y/N: ")


def get_shape_lab(n, lab):
    if n >= 30:
        print(lab + " N >= 30")
        return 1
    return ask_yes_no(lab + " OK SHAPE? Y/N: ")


def get_pos_int(prompt):
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            v = int(s)
            if v > 0:
                return v
        print("POS INT")


def get_nonneg_int(prompt):
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            return int(s)
        print("WHOLE #")


def get_opt_pos_int(prompt):
    while True:
        s = input(prompt).strip()
        if s == "":
            return None
        if s.isdigit():
            v = int(s)
            if v > 0:
                return v
        print("POS INT OR ENTER")


def get_num(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("NUMBER")


def get_pos_num(prompt):
    while True:
        v = get_num(prompt)
        if v > 0:
            return v
        print("POS NUMBER")


def get_n_t(prompt):
    while True:
        v = get_pos_int(prompt)
        if v >= 2:
            return v
        print("N >= 2")


def get_prob(prompt):
    while True:
        v = get_num(prompt)
        if 0 < v < 1:
            return v
        if 1 < v < 100:
            return v / 100.0
        print("0-1 OR %")


def get_conf():
    while True:
        v = get_num("CONF: ")
        if 0 < v < 1:
            return v
        if 1 < v < 100:
            return v / 100.0
        print("0-1 OR %")


def ask_yes_no(prompt):
    while True:
        s = input(prompt).strip().lower()
        if s == "y" or s == "yes":
            return 1
        if s == "n" or s == "no":
            return 0
        print("Y OR N")


def z_pv(z, tail):
    c = norm_cdf(z)
    return tail_pv(c, tail)


def t_pv(t, df, tail):
    c = t_cdf(t, df)
    return tail_pv(c, tail)


def tail_pv(c, tail):
    if tail == ">":
        return 1 - c
    if tail == "<":
        return c
    m = c
    if 1 - c < m:
        m = 1 - c
    return 2 * m


def norm_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def inv_norm(p):
    lo = -10.0
    hi = 10.0
    i = 0
    while i < 50:
        mid = (lo + hi) / 2
        if norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
        i = i + 1
    return (lo + hi) / 2


def t_cdf(x, df):
    if x == 0:
        return 0.5
    area = t_area(0, abs(x), df)
    if x > 0:
        v = 0.5 + area
        if v > 1:
            return 1.0
        return v
    v = 0.5 - area
    if v < 0:
        return 0.0
    return v


def inv_t(p, df):
    lo = -20.0
    hi = 20.0
    i = 0
    while i < 40:
        mid = (lo + hi) / 2
        if t_cdf(mid, df) < p:
            lo = mid
        else:
            hi = mid
        i = i + 1
    return (lo + hi) / 2


def t_area(a, b, df):
    if a == b:
        return 0.0
    steps = 120
    if steps % 2 == 1:
        steps = steps + 1
    w = (b - a) / steps
    total = t_den(a, df) + t_den(b, df)
    i = 1
    while i < steps:
        x = a + i * w
        if i % 2 == 0:
            total = total + 2 * t_den(x, df)
        else:
            total = total + 4 * t_den(x, df)
        i = i + 1
    return total * w / 3


def t_den(x, df):
    c = t_const(df)
    p = -((df + 1) / 2)
    return c * (1 + (x * x) / df) ** p


def t_const(df):
    df = int(df)
    if df <= 0:
        return 0.0
    if df == 1:
        return 1 / math.pi
    if df == 2:
        return 1 / (2 * math.sqrt(2))
    if df % 2 == 1:
        c = 1 / math.pi
        cur = 1
    else:
        c = 1 / (2 * math.sqrt(2))
        cur = 2
    while cur < df:
        r = ((cur + 1) / cur) * math.sqrt(cur / (cur + 2))
        c = c * r
        cur = cur + 2
    return c


def cons_df(n1, n2):
    d1 = n1 - 1
    d2 = n2 - 1
    if d1 < d2:
        return d1
    return d2


def tcdf_text(t, df, tail):
    ts = fmt(t)
    ds = fmt(df)
    if tail == ">":
        return "tcdf(" + ts + ",1E99," + ds + ")"
    if tail == "<":
        return "tcdf(-1E99," + ts + "," + ds + ")"
    return "2*tcdf(abs(" + ts + "),1E99," + ds + ")"


def fmt(v):
    return "{:.4f}".format(v)


def pct(v):
    return "{:.1f}%".format(v * 100)


if __name__ == "__main__":
    main()
