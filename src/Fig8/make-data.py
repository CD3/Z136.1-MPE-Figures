import pathlib
from decimal import Decimal as D

exec(pathlib.Path("../calculations.py").read_text())

with pathlib.Path("data.txt").open("w") as fd:
    fd.write("# Correction factors Ca, Cb, and Cc\n")
    fd.write("# wavelength (nm)    value\n")
    fd.write("# Ca\n")
    for l in ["400.0", "700.0", "1050.0", "1400.0"]:
        fd.write(f"{l} {round(C_A(D(l)), 1)}\n")
    fd.write("\n\n# Cb\n")
    for l in ["400.0", "450.0", "600.0"]:
        fd.write(f"{l} {round(C_B(D(l)), 1)}\n")

    fd.write("\n\n# Cc\n")
    for l in [
        "1050.0",
        "1150.0",
        "1200.0",
        "1210.0",
        "1220.0",
        "1230.0",
        "1240.0",
        "1250.0",
        "1260.0",
        "1270.0",
        "1280.0",
        "1290.0",
        "1300.0",
        "1310.0",
        "1320.0",
        "1330.0",
        "1340.0",
        "1350.0",
        "1360.0",
        "1370.0",
        "1380.0",
        "1390.0",
        "1400.0",
    ]:
        fd.write(f"{l} {round(C_C(D(l)), 3)}\n")
