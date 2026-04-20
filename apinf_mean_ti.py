"""TI-84 AP Stats: one-sample and two-sample mean inference."""

import math


def main():
    while True:
        print("MEAN INF")
        print("1) 1M T TEST")
        print("2) 1M T INT")
        print("3) 2S T TEST")
        print("4) 2S T INT")
        print("5) EXIT")
        ch = input("CHOICE: ").strip()
        print()
        if ch == "1":
            run_1ttest()
        elif ch == "2":
            run_1tint()
        elif ch == "3":
            run_2ttest()
        elif ch == "4":
            run_2tint()
        elif ch == "5":
            print("BYE")
            break
        else:
            print("ENTER 1-5")
            print()


def run_1ttest():
    ctx = txt("CTX: ", "POP")
    xb = num("XBAR: ")
    s = pnum("S: ")
    n = nt("N: ")
    mu0 = num("MU0: ")
    tail = alt()
    a = prob("A: ")
    pop = opint("POP N: ")
    shp = shape(n)
    df = n - 1
    se = s / math.sqrt(n)
    t = (xb - mu0) / se
    pv = t_pv(t, df, tail)
    sec("CHECKS")
    rand1()
    ten(pop, n, "")
    norm_ok(n, shp, "")
    sec("SETUP")
    print("- mu true mean of " + ctx)
    print("- H0: mu = " + fmt(mu0))
    print("- Ha: mu " + tail + " " + fmt(mu0))
    sec("VALS")
    print("- SE = " + fmt(se))
    print("- t = " + fmt(t))
    print("- df = " + str(df))
    print("- ALT = " + tail)
    print("- PV = " + fmt(pv) + " approx")
    print("- use tcdf")
    print("- " + tcdf_txt(t, df, tail))
    conc(test_txt(pv, a, "mean", ctx, tail, mu0))


def run_1tint():
    ctx = txt("CTX: ", "POP")
    xb = num("XBAR: ")
    s = pnum("S: ")
    n = nt("N: ")
    conf = confv()
    pop = opint("POP N: ")
    shp = shape(n)
    df = n - 1
    se = s / math.sqrt(n)
    tc = inv_t((1 + conf) / 2, df)
    me = tc * se
    lo = xb - me
    hi = xb + me
    sec("CHECKS")
    rand1()
    ten(pop, n, "")
    norm_ok(n, shp, "")
    sec("SETUP")
    print("- mu true mean of " + ctx)
    print("- CI: xbar +- t*SE")
    sec("VALS")
    print("- SE = " + fmt(se))
    print("- df = " + str(df))
    print("- t* = " + fmt(tc))
    print("- ME = " + fmt(me))
    print("- INT = " + iv(lo, hi))
    conc(ci_txt(conf, "mean of " + ctx, lo, hi))


def run_2ttest():
    g1 = txt("G1: ", "G1")
    g2 = txt("G2: ", "G2")
    xb1, s1, n1, xb2, s2, n2 = two_means()
    tail = alt()
    a = prob("A: ")
    pop1 = opint("N1POP: ")
    pop2 = opint("N2POP: ")
    shp1 = shape_lab(n1, "G1")
    shp2 = shape_lab(n2, "G2")
    diff = xb1 - xb2
    se = math.sqrt((s1 * s1 / n1) + (s2 * s2 / n2))
    t = diff / se
    df = cons_df(n1, n2)
    pv = t_pv(t, df, tail)
    sec("CHECKS")
    rand2()
    indep()
    ten(pop1, n1, " G1")
    ten(pop2, n2, " G2")
    norm_ok(n1, shp1, " G1")
    norm_ok(n2, shp2, " G2")
    sec("SETUP")
    print("- mu1-mu2 true mean diff")
    print("- H0: mu1-mu2 = 0")
    print("- Ha: mu1-mu2 " + tail + " 0")
    sec("VALS")
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
    print("- use tcdf")
    print("- " + tcdf_txt(t, df, tail))
    conc(test_txt(pv, a, "mean diff", g1 + " - " + g2, tail, 0.0))


def run_2tint():
    g1 = txt("G1: ", "G1")
    g2 = txt("G2: ", "G2")
    xb1, s1, n1, xb2, s2, n2 = two_means()
    conf = confv()
    pop1 = opint("N1POP: ")
    pop2 = opint("N2POP: ")
    shp1 = shape_lab(n1, "G1")
    shp2 = shape_lab(n2, "G2")
    diff = xb1 - xb2
    se = math.sqrt((s1 * s1 / n1) + (s2 * s2 / n2))
    df = cons_df(n1, n2)
    tc = inv_t((1 + conf) / 2, df)
    me = tc * se
    lo = diff - me
    hi = diff + me
    sec("CHECKS")
    rand2()
    indep()
    ten(pop1, n1, " G1")
    ten(pop2, n2, " G2")
    norm_ok(n1, shp1, " G1")
    norm_ok(n2, shp2, " G2")
    sec("SETUP")
    print("- mu1-mu2 true mean diff")
    print("- CI: diff +- t*SE")
    sec("VALS")
    print("- diff = " + fmt(diff))
    print("- SE = " + fmt(se))
    print("- df = " + str(df))
    print("- t* = " + fmt(tc))
    print("- ME = " + fmt(me))
    print("- INT = " + iv(lo, hi))
    conc(ci_txt(conf, "mean diff of " + g1 + " - " + g2, lo, hi))


def sec(s):
    print(s)


def conc(s):
    print("CONC")
    print(s)
    print()


def rand1():
    print("- RAND")


def rand2():
    print("- RAND x2")


def indep():
    print("- INDEP")


def ten(pop, n, suf):
    if pop is None:
        print("- 10%" + suf + ": NEED POP")
    else:
        pf("10%" + suf, n <= 0.10 * pop)


def norm_ok(n, shp, suf):
    if n >= 30:
        pf("NORM" + suf, 1)
    else:
        pf("NORM" + suf, shp)


def pf(lab, ok):
    if ok:
        print("- " + lab + ": OK")
    else:
        print("- " + lab + ": CHK")


def test_txt(pv, a, name, ctx, tail, nullv):
    if pv < a:
        d = "Reject H0."
        e = "Evidence"
        c = "<"
    else:
        d = "Fail to reject H0."
        e = "Not enough evidence"
        c = ">"
    return "PV " + fmt(pv) + " " + c + " A " + fmt(a) + ". " + d + " " + e + " true " + name + " of " + ctx + " is " + rel(tail) + " " + fmt(nullv) + "."


def ci_txt(conf, lab, lo, hi):
    return pct(conf) + " CI: true " + lab + " in " + iv(lo, hi) + "."


def rel(tail):
    if tail == ">":
        return "greater than"
    if tail == "<":
        return "less than"
    return "different from"


def txt(prompt, default):
    s = input(prompt).strip()
    if s == "":
        return default
    return s


def alt():
    print("ALT")
    print("1) >")
    print("2) <")
    print("3) !=")
    s = input("CHOICE: ").strip()
    print()
    if s == "1":
        return ">"
    if s == "2":
        return "<"
    return "!="


def shape(n):
    if n >= 30:
        print("N >= 30")
        return 1
    return yes("OK SHAPE? Y/N: ")


def shape_lab(n, lab):
    if n >= 30:
        print(lab + " N >= 30")
        return 1
    return yes(lab + " OK SHAPE? Y/N: ")


def pint(prompt):
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            v = int(s)
            if v > 0:
                return v
        print("POS INT")


def opint(prompt):
    while True:
        s = input(prompt).strip()
        if s == "":
            return None
        if s.isdigit():
            v = int(s)
            if v > 0:
                return v
        print("POS INT OR ENTER")


def num(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("NUMBER")


def pnum(prompt):
    while True:
        v = num(prompt)
        if v > 0:
            return v
        print("POS NUMBER")


def nt(prompt):
    while True:
        v = pint(prompt)
        if v >= 2:
            return v
        print("N >= 2")


def prob(prompt):
    while True:
        v = num(prompt)
        if 0 < v < 1:
            return v
        if 1 < v < 100:
            return v / 100.0
        print("0-1 OR %")


def confv():
    return prob("CONF: ")


def yes(prompt):
    while True:
        s = input(prompt).strip().lower()
        if s == "y" or s == "yes":
            return 1
        if s == "n" or s == "no":
            return 0
        print("Y OR N")


def two_means():
    xb1 = num("XB1: ")
    s1 = pnum("S1: ")
    n1 = nt("N1: ")
    xb2 = num("XB2: ")
    s2 = pnum("S2: ")
    n2 = nt("N2: ")
    return xb1, s1, n1, xb2, s2, n2


def t_pv(t, df, tail):
    c = t_cdf(t, df)
    if tail == ">":
        return 1 - c
    if tail == "<":
        return c
    m = c
    if 1 - c < m:
        m = 1 - c
    return 2 * m


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
    tot = t_den(a, df) + t_den(b, df)
    i = 1
    while i < steps:
        x = a + i * w
        if i % 2 == 0:
            tot = tot + 2 * t_den(x, df)
        else:
            tot = tot + 4 * t_den(x, df)
        i = i + 1
    return tot * w / 3


def t_den(x, df):
    return t_const(df) * (1 + (x * x) / df) ** (-((df + 1) / 2))


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
        c = c * ((cur + 1) / cur) * math.sqrt(cur / (cur + 2))
        cur = cur + 2
    return c


def cons_df(n1, n2):
    d1 = n1 - 1
    d2 = n2 - 1
    if d1 < d2:
        return d1
    return d2


def tcdf_txt(t, df, tail):
    ts = fmt(t)
    ds = str(df)
    if tail == ">":
        return "tcdf(" + ts + ",1E99," + ds + ")"
    if tail == "<":
        return "tcdf(-1E99," + ts + "," + ds + ")"
    return "2*tcdf(abs(" + ts + "),1E99," + ds + ")"


def fmt(v):
    return "{:.4f}".format(v)


def pct(v):
    return "{:.1f}%".format(v * 100)


def iv(lo, hi):
    return "(" + fmt(lo) + "," + fmt(hi) + ")"


if __name__ == "__main__":
    main()
