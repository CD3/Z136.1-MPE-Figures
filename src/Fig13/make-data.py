import pathlib
from decimal import Decimal as D

exec(pathlib.Path("../calculations.py").read_text())

with pathlib.Path("data.txt").open("w") as fd:
    fd.write("# Wavelength (nm)    Klambda\n")
    for l in ["1200.0", "1400.0"]:
        fd.write(f"{l} {round(K_lambda(D(l)), 1)}\n")
