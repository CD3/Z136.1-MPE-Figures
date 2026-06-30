import pathlib

exec(pathlib.Path("../calculations.py").read_text())

with pathlib.Path("data.txt").open("w") as fd:
    fd.write("# Data for ANSI Z136.1 Figure 7\n")

    l = D("532")
    for a in ["1.0", "7.5", "25.0", "100.0"]:
        a = D(a)
        fd.write(f"# alpha = {a} mrad\n")
        for t in [
            "1.001e-13",
            "0.999e-11",
            "1.000e-11",
            "4.999e-6",
            "6.25e-4",
            "1.406e-03",
            "1.563e-02",
            "2.0e-1",  #
            "2.5e-1",
            "1.000",
        ]:
            t = D(t)
            val = MPE_VIS_ES_THERMAL(l, t, a)
            fd.write(f"{t:.1e} {val:.3e}\n")
        fd.write("\n\n")
