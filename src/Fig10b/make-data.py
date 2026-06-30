import pathlib

exec(pathlib.Path("../calculations.py").read_text())

with pathlib.Path("data.txt").open("w") as fd:
    a = D("3")
    fd.write("# t [s]   MPE [W/cm^2]\n")

    # Need to sample time from 0.1 to 30,000 in order to capture the crossover between
    # thermal and photochemical. We want the times to be evenly space on logscale since that is
    # what we will be plotting on.
    # 0.1 = 1e-1, 30,000 = 3e4
    # times: 1e-1, 2e-1, 3e-1,... 1e0, 2e0,...3e4
    durations = []
    for power in [-1, 0, 1, 2, 3, 4]:
        for mantissa in ["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "6", "7", "8"]:
            t = D(f"{mantissa}e{power}")
            if t >= D(
                "30000"
            ):  # actually can't include 30000 since time range is exclusive on top end.
                break
            durations.append(t)

    durations.append(D("2.99999e4"))

    l = D("400")
    fd.write("# 400 to 700 Thermal nm\n")
    for t in durations:
        t = D(t)
        val = MPE_VIS_ES_THERMAL(l, t, a) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    fd.write("# 400 to 450 nm Dual Limit (Lower of Thermal and Photochemical)\n")
    for t in durations:
        t = D(t)
        val = MPE_VIS_ES(l, t, a) / t  # convert to irradiance
        fd.write(f"{t:.3e} {val:.3e}\n")

    fd.write("\n")
    l = D("475")
    fd.write(f"# {l} nm\n")
    for t in durations:
        t = D(t)
        val = MPE_VIS_ES(l, t, a) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("500")
    fd.write(f"# {l} nm\n")
    for t in durations:
        t = D(t)
        val = MPE_VIS_ES(l, t, a) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    # INFRARED
    fd.write("\n")
    l = D("850")
    fd.write(f"# 850 nm\n")
    for t in durations:
        t = D(t)
        val = MPE_NIR_ES(l, t, a) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("1064")
    fd.write(f"# 1064 nm\n")
    for t in durations:
        t = D(t)
        val = MPE_NIR_ES(l, t, a) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("1315")
    fd.write(f"# 1315 nm\n")
    for t in durations:
        t = D(t)
        val = MPE_NIR_ES(l, t, a) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("1399.9999")
    fd.write(f"# 1400 nm\n")
    for t in durations:
        t = D(t)
        val = MPE_NIR_ES(l, t, a) / t  # convert to irradiance
        fd.write(f"{t:.1e} {val:.3e}\n")
