import pathlib

exec(pathlib.Path("../calculations.py").read_text())

with pathlib.Path("data-1.txt").open("w") as fd:
    fd.write("# t [s] MPE [J/cm^2]\n")
    for l in ["1400", "1500", "1800", "2600"]:
        l = D(l)
        fd.write(f"# {l} nm\n")
        for t in [
            "1.0e-13",
            "0.9999e-11",
            "1.0e-11",
            "0.9999e-9",
            "1.0e-9",
            "0.9999e-7",
            "1.0e-7",
            "0.9999e-3",
            "1.0e-3",
            "3.999",
            "4.0",
            "10.0",
            "2.9999e4",
        ]:
            t = D(t)
            val = MPE_FIR(l, t)
            fd.write(f"{t:.1e} {val:.2e}\n")
        fd.write("\n\n")


with pathlib.Path("data-2.txt").open("w") as fd:
    fd.write("# t [s] MPE [J/cm^2]\n")
    fd.write("# 315 to 400 nm\n")
    for t in [
        "1.0e-13",
        "0.999e-11",
        "1.e-11",
        "0.999e-9",
        "1e-9",
        "9.999",
        "10.0",
        "2.9999e4",
    ]:
        t = D(t)
        val = MPE_UV(D("315"), t)
        fd.write(f"{t:.1e} {val:.2e}\n")
