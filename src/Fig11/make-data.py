import pathlib
from decimal import Decimal as D

exec(pathlib.Path("../calculations.py").read_text())


with pathlib.Path("data-1.txt").open("w") as fd:
    fd.write("# alpha <= 5 mrad\n")
    a = D("4")
    a_max = D("50")
    for n in ["1.0", "1.0e+6"]:
        val = round(C_P(a, a_max, D(n)), 1)
        fd.write(f"{n} {val}\n")
with pathlib.Path("data-2.txt").open("w") as fd:
    fd.write("# 5 mrad < alpha <= alpha_max\n")
    a = D("10")
    a_max = D("50")
    for n in ["1.0", "40.0", "1.0e+6"]:
        val = round(C_P(a, a_max, D(n)), 1)
        fd.write(f"{n} {val}\n")

with pathlib.Path("data-3.txt").open("w") as fd:
    fd.write("# alpha > alpha_max\n")
    a = D("60")
    a_max = D("50")
    for n in ["1.0", "625.0", "1.0e+6"]:
        val = round(C_P(a, a_max, D(n)), 1)
        fd.write(f"{n} {val}\n")
