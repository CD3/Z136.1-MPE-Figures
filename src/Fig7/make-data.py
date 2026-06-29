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


exit()
pathlib.Path("data.txt").write_text(
    """# Data for ANSI Z136.1 Figure 7
# alpha = 1.0 mrad
1.000e-13   1.000e-7
1.000e-11   1.000e-7
1.000e-11   2.000e-7
5.000e-06   2.000e-7
1.000e+00   1.800e-3


# alpha = 7.5 mrad
1.000e-13   7.500e-7
1.000e-11   7.500e-7
1.000e-11   1.500e-6
5.000e-06   1.500e-6
6.250e-04   5.336e-5
1.406e-03   6.535e-5
1.000e+00   9.000e-3


# alpha = 25.0 mrad
1.000e-13   8.333e-6
1.000e-11   8.333e-6
1.000e-11   1.667e-5
5.000e-06   1.667e-5
6.250e-04   5.929e-4
1.563e-02   1.326e-3
1.000e+00   3.000e-2


# alpha = 100.0
1.000e-13   1.333e-04
1.000e-11   1.333e-04
1.000e-11   2.667e-04
5.000e-06   2.667e-04
6.250e-04   9.487e-03
2.500e-01   4.243e-02
1.000e+00   1.200e-01
"""
)
