import pathlib
from decimal import Decimal as D

exec(pathlib.Path("../calculations.py").read_text())

with pathlib.Path("data.txt").open("w") as fd:
    fd.write("# Cone limiting angle for photochemical MPEs\n")
    fd.write("# t(s)      gamma (mrad)\n")
    for t in ["0.7", "100.0", "10000.0", "30000.0"]:
        fd.write(f"{t} {round(gamma(D(t)), 1)}\n")

    pass
