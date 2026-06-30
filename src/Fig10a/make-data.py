import pathlib

exec(pathlib.Path("../calculations.py").read_text())

# NOTE: In 2007 there were dual limits for the point source visible MPEs.
#       These were removed in 2014 but the figure still references
#       thermal vs photochemical in both 2014 and 2022 versions.

with pathlib.Path("data.txt").open("w") as fd:
    fd.write("# t [s]   MPE [W/cm^2]\n")
    l = D("400")
    fd.write("# 400 to 450 nm\n")
    for t in ["1.0e-1", "2.5e-1", "1.0e1", "1.0e2", "2.99999e4"]:
        t = D(t)
        val = MPE_VIS_PS(l, t) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("475")
    fd.write(f"# {l} nm\n")
    for t in ["1.0e-1", "2.5e-1", "1.0e1", "1.0e2", "2.99999e4"]:
        t = D(t)
        val = MPE_VIS_PS(l, t) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("490")
    fd.write(f"# {l} nm\n")
    for t in ["1.0e-1", "2.5e-1", "1.0e1", "1.0e2", "2.99999e4"]:
        t = D(t)
        val = MPE_VIS_PS(l, t) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("500")
    fd.write(f"# 500 to 700 nm\n")
    for t in ["1.0e-1", "2.5e-1", "1.0e1", "1.0e2", "2.99999e4"]:
        t = D(t)
        val = MPE_VIS_PS(l, t) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("850")
    fd.write(f"# 850 nm\n")
    for t in ["1.0e-1", "2.5e-1", "1.0e1", "1.0e2", "2.99999e4"]:
        t = D(t)
        val = MPE_NIR_PS(l, t) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("1064")
    fd.write(f"# 1064 nm\n")
    for t in ["1.0e-1", "2.5e-1", "1.0e1", "1.0e2", "2.99999e4"]:
        t = D(t)
        val = MPE_NIR_PS(l, t) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("1315")
    fd.write(f"# 1315 nm\n")
    for t in ["1.0e-1", "2.5e-1", "1.0e1", "1.0e2", "2.99999e4"]:
        t = D(t)
        val = MPE_NIR_PS(l, t) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("1399.9999")
    fd.write(f"# 1400 nm\n")
    for t in ["1.0e-1", "2.5e-1", "1.0e1", "1.0e2", "2.99999e4"]:
        t = D(t)
        val = MPE_NIR_PS(l, t) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")
