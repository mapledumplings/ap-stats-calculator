"""TI-84 AP Stats: proportion inference."""

import math


def main():
    while True:
        print("PROP INF")
        print("1) 1P Z TEST")
        print("2) 1P Z INT")
        print("3) 2P Z TEST")
        print("4) 2P Z INT")
        print("5) EXIT")
        ch = input("CHOICE: ").strip()
        print()
        if ch == "1":
            run_1ztest()
        elif ch == "2":
            run_1zint()
        elif ch == "3":
            run_2ztest()
        elif ch == "4":
            run_2zint()
        elif ch == "5":
            print("BYE")
            break
        else:
            print("ENTER 1-5")
            print()


def run_1ztest():
    ctx = txt("CTX: ", "POP")
    x = nnint("X: ")
    n = pint("N: ")
    while x > n:
        print("X > N")
        x = nnint("X: ")
        n = pint("N: ")
    p0 = prob("P0: ")
    tail = alt()
    a = prob("A: ")
    pop = opint("POP N: ")
    ph = x / n
    se0 = math.sqrt(p0 * (1 - p0) / n)
    z = (ph - p0) / se0
    pv = z_pv(z, tail)
    sec("CHECKS")
    rand1()
    ten(pop, n, "")
    pf("LARGE", n * p0 >= 10 and n * (1 - p0) >= 10)
    sec("SETUP")
    print("- p true prop of " + ctx)
    print("- H0: p = " + fmt(p0))
    print("- Ha: p " + tail + " " + fmt(p0))
    print("- norm approx")
    sec("VALS")
    print("- ph = " + fmt(ph))
    print("- SE0 = " + fmt(se0))
    print("- z = " + fmt(z))
    print("- ALT = " + tail)
    print("- PV = " + fmt(pv))
    conc(test_txt(pv, a, "prop", ctx, tail, p0))


def run_1zint():
    ctx = txt("CTX: ", "POP")
    x = nnint("X: ")
    n = pint("N: ")
    while x > n:
        print("X > N")
        x = nnint("X: ")
        n = pint("N: ")
    conf = confv()
    pop = opint("POP N: ")
    ph = x / n
    zc = inv_norm((1 + conf) / 2)
    se = math.sqrt(ph * (1 - ph) / n)
    me = zc * se
    lo = ph - me
    hi = ph + me
    sec("CHECKS")
    rand1()
    ten(pop, n, "")
    pf("LARGE", n * ph >= 10 and n * (1 - ph) >= 10)
    sec("SETUP")
    print("- p true prop of " + ctx)
    print("- CI: ph +- z*SE")
    print("- norm approx")
    sec("VALS")
    print("- ph = " + fmt(ph))
    print("- z* = " + fmt(zc))
    print("- SE = " + fmt(se))
    print("- ME = " + fmt(me))
    print("- INT = " + iv(lo, hi))
    conc(ci_txt(conf, "prop of " + ctx, lo, hi))


def run_2ztest():
    g1 = txt("G1: ", "G1")
    g2 = txt("G2: ", "G2")
    x1, n1, x2, n2 = two_counts()
    tail = alt()
    a = prob("A: ")
    pop1 = opint("N1POP: ")
    pop2 = opint("N2POP: ")
    ph1 = x1 / n1
    ph2 = x2 / n2
    phc = (x1 + x2) / (n1 + n2)
    se0 = math.sqrt(phc * (1 - phc) * ((1 / n1) + (1 / n2)))
    z = (ph1 - ph2) / se0
    pv = z_pv(z, tail)
    sec("CHECKS")
    rand2()
    indep()
    ten(pop1, n1, " G1")
    ten(pop2, n2, " G2")
    ok = 1
    if n1 * phc < 10 or n1 * (1 - phc) < 10:
        ok = 0
    if n2 * phc < 10 or n2 * (1 - phc) < 10:
        ok = 0
    pf("POOL CTS", ok)
    sec("SETUP")
    print("- p1-p2 true prop diff")
    print("- H0: p1-p2 = 0")
    print("- Ha: p1-p2 " + tail + " 0")
    print("- norm approx")
    sec("VALS")
    print("- ph1 = " + fmt(ph1))
    print("- ph2 = " + fmt(ph2))
    print("- phc = " + fmt(phc))
    print("- SE0 = " + fmt(se0))
    print("- z = " + fmt(z))
    print("- ALT = " + tail)
    print("- PV = " + fmt(pv))
    conc(test_txt(pv, a, "prop diff", g1 + " - " + g2, tail, 0.0))


def run_2zint():
    g1 = txt("G1: ", "G1")
    g2 = txt("G2: ", "G2")
    x1, n1, x2, n2 = two_counts()
    conf = confv()
    pop1 = opint("N1POP: ")
    pop2 = opint("N2POP: ")
    ph1 = x1 / n1
    ph2 = x2 / n2
    diff = ph1 - ph2
    zc = inv_norm((1 + conf) / 2)
    se = math.sqrt(ph1 * (1 - ph1) / n1 + ph2 * (1 - ph2) / n2)
    me = zc * se
    lo = diff - me
    hi = diff + me
    sec("CHECKS")
    rand2()
    indep()
    ten(pop1, n1, " G1")
    ten(pop2, n2, " G2")
    ok = 1
    if n1 * ph1 < 10 or n1 * (1 - ph1) < 10:
        ok = 0
    if n2 * ph2 < 10 or n2 * (1 - ph2) < 10:
        ok = 0
    pf("LARGE", ok)
    sec("SETUP")
    print("- p1-p2 true prop diff")
    print("- CI: diff +- z*SE")
    print("- norm approx")
    sec("VALS")
    print("- ph1 = " + fmt(ph1))
    print("- ph2 = " + fmt(ph2))
    print("- diff = " + fmt(diff))
    print("- z* = " + fmt(zc))
    print("- SE = " + fmt(se))
    print("- ME = " + fmt(me))
    print("- INT = " + iv(lo, hi))
    conc(ci_txt(conf, "prop diff of " + g1 + " - " + g2, lo, hi))


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


def two_counts():
    x1 = nnint("X1: ")
    n1 = pint("N1: ")
    while x1 > n1:
        print("X1 > N1")
        x1 = nnint("X1: ")
        n1 = pint("N1: ")
    x2 = nnint("X2: ")
    n2 = pint("N2: ")
    while x2 > n2:
        print("X2 > N2")
        x2 = nnint("X2: ")
        n2 = pint("N2: ")
    return x1, n1, x2, n2


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


def pint(prompt):
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            v = int(s)
            if v > 0:
                return v
        print("POS INT")


def nnint(prompt):
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            return int(s)
        print("WHOLE #")


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


def z_pv(z, tail):
    c = norm_cdf(z)
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


def fmt(v):
    return "{:.4f}".format(v)


def pct(v):
    return "{:.1f}%".format(v * 100)


def iv(lo, hi):
    return "(" + fmt(lo) + "," + fmt(hi) + ")"


if __name__ == "__main__":
    main()
