import pathlib
from decimal import Decimal as D

exec(pathlib.Path("../calculations.py").read_text())

with pathlib.Path(f"data-1.txt").open("w") as fd:
    a = "1.5"
    fd.write("# C_g for photochemical MPEs\n")
    fd.write(f"# alpha = {a} mrad\n")
    fd.write("# gamma (mrad)    C_g\n")
    for g in ["11.0", "110.0"]:
        fd.write(f"{g} {round(C_g(D(a), D(g)), 2)}\n")

with pathlib.Path(f"data-2.txt").open("w") as fd:
    a = "25"
    fd.write("# C_g for photochemical MPEs\n")
    fd.write(f"# alpha = {a} mrad\n")
    fd.write("# gamma (mrad)    C_g\n")
    for g in ["11.0", "25.0", "110.0"]:
        fd.write(f"{g} {round(C_g(D(a), D(g)), 2)}\n")

with pathlib.Path(f"data-3.txt").open("w") as fd:
    a = "50"
    fd.write("# C_g for photochemical MPEs\n")
    fd.write(f"# alpha = {a} mrad\n")
    fd.write("# gamma (mrad)    C_g\n")
    for g in ["11.0", "50.0", "110.0"]:
        fd.write(f"{g} {round(C_g(D(a), D(g)), 2)}\n")

with pathlib.Path(f"data-4.txt").open("w") as fd:
    a = "75"
    fd.write("# C_g for photochemical MPEs\n")
    fd.write(f"# alpha = {a} mrad\n")
    fd.write("# gamma (mrad)    C_g\n")
    for g in ["11.0", "75.0", "110.0"]:
        fd.write(f"{g} {round(C_g(D(a), D(g)), 2)}\n")

with pathlib.Path(f"data-5.txt").open("w") as fd:
    a = "100"
    fd.write("# C_g for photochemical MPEs\n")
    fd.write(f"# alpha = {a} mrad\n")
    fd.write("# gamma (mrad)    C_g\n")
    for g in ["11.0", "100.0", "110.0"]:
        fd.write(f"{g} {round(C_g(D(a), D(g)), 2)}\n")
