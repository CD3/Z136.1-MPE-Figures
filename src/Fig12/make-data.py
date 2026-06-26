import pathlib
from decimal import Decimal as D

exec(pathlib.Path("../calculations.py").read_text())

with pathlib.Path("data.txt").open("w") as fd:
    fd.write("# alpha_max\n")
    fd.write("# t (s)    a_max (mrad)\n")
    for t in ["1.0e-13", "6.25e-4", "0.25", "3.0e+4"]:
        a = round(alpha_max(D(t)), 1)
        fd.write(f"{t} {a}\n")
