import pathlib

exec(pathlib.Path("../calculations.py").read_text())


with pathlib.Path("data.txt").open("w") as fd:
    a = D("110")
    Omega = D("3.14159") * (a / D("1000")) ** 2 / D("4")
    fd.write("# t [s]   MPE [W/cm^2]\n")
    # Not sure this figure even makes sense now, the MPEs are not given as an integrted radiance/radiance
    # anymore. Cg used for the visible makes the MPE act _sort_ of like before, but in the NIR
    # saying that the MPE is given as some radiance for all alpha >= 100 mrad is incorrect.

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
        val = MPE_VIS_ES_THERMAL(l, t, a) / t / Omega  # convert to radiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")

    fd.write("# 400 to 450 nm Dual Limit (Lower of Thermal and Photochemical)\n")
    for t in durations:
        t = D(t)
        val = MPE_VIS_ES(l, t, a) / t / Omega  # convert to radiance
        fd.write(f"{t:.3e} {val:.3e}\n")

    fd.write("\n")
    l = D("475")
    fd.write(f"# {l} nm\n")
    for t in durations:
        t = D(t)
        val = MPE_VIS_ES(l, t, a) / t / Omega  # convert to radiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("500")
    fd.write(f"# {l} nm\n")
    for t in durations:
        t = D(t)
        val = MPE_VIS_ES(l, t, a) / t / Omega  # convert to radiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("532")
    fd.write(f"# {l} nm\n")
    for t in durations:
        t = D(t)
        val = MPE_VIS_ES(l, t, a) / t / Omega  # convert to radiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("550")
    fd.write(f"# {l} nm\n")
    for t in durations:
        t = D(t)
        val = MPE_VIS_ES(l, t, a) / t / Omega  # convert to radiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    # INFRARED
    fd.write("\n")
    l = D("850")
    fd.write(f"# 850 nm\n")
    for t in durations:
        t = D(t)
        val = MPE_NIR_ES(l, t, a) / t / Omega  # convert to radiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("1064")
    fd.write(f"# 1064 nm\n")
    for t in durations:
        t = D(t)
        val = MPE_NIR_ES(l, t, a) / t / Omega  # convert to radiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("1315")
    fd.write(f"# 1315 nm\n")
    for t in durations:
        t = D(t)
        val = MPE_NIR_ES(l, t, a) / t / Omega  # convert to radiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    l = D("1399.9999")
    fd.write(f"# 1400 nm\n")
    for t in durations:
        t = D(t)
        val = MPE_NIR_ES(l, t, a) / t / Omega  # convert to radiance
        fd.write(f"{t:.1e} {val:.3e}\n")
exit()
import pathlib

pathlib.Path("data-therm.txt").write_text(
    """# lambda=550.0
# t(s)    MPE (W/cm^2/sr)
1.000000e-01    4.295971e+01
2.500000e-01    2.160759e+01
1.000000e+02    4.831604e+00
3.000000e+04    4.831604e+00


# lambda=850.0
# t(s)    MPE (W/cm^2/sr)
1.000000e-01    8.571590e+01
2.500000e-01    4.311281e+01
1.000000e+02    9.640318e+00
3.000000e+04    9.640318e+00


# lambda=1064.0
# t(s)    MPE (W/cm^2/sr)
1.000000e-01    2.147986e+02
2.500000e-01    1.080380e+02
1.000000e+02    2.415802e+01
3.000000e+04    2.415802e+01


"""
)
pathlib.Path("data-photo.txt").write_text(
    """# lambda=425.0
# t(s)    MPE (W/cm^2/sr)
1.224273e+01    8.168115e+00
1.000000e+04    1.000000e-02
3.000000e+04    1.000000e-02


# lambda=475.0
# t(s)    MPE (W/cm^2/sr)
5.682571e+01    5.564872e+00
1.000000e+04    3.162278e-02
3.000000e+04    3.162278e-02


# lambda=500.0
# t(s)    MPE (W/cm^2/sr)
2.069706e+02    4.831604e+00
1.000000e+04    1.000000e-01
3.000000e+04    1.000000e-01


# lambda=532.0
# t(s)    MPE (W/cm^2/sr)
9.034594e+02    4.831604e+00
1.000000e+04    4.365158e-01
3.000000e+04    4.365158e-01


# lambda=550.0
# t(s)    MPE (W/cm^2/sr)
2.069706e+03    4.831604e+00
1.000000e+04    1.000000e+00
3.000000e+04    1.000000e+00


"""
)


pathlib.Path("data-cornea.txt").write_text(
    """# lambda=1315.0
# t(s)    MPE (W/cm^2/sr)
1.000e-01  2.461e+03
1.446e-01  1.724e+03
2.091e-01  1.209e+03
3.024e-01  8.487e+02
4.373e-01  5.965e+02
6.325e-01  4.198e+02
9.146e-01  2.959e+02
1.323e+00  2.088e+02
1.913e+00  1.476e+02
2.766e+00  1.045e+02
4.000e+00  7.429e+01
1.000e+01  2.971e+01
1.263e+02  2.971e+01
3.000e+04  2.971e+01


# lambda=1400.0
# t(s)    MPE (W/cm^2/sr)
1.000000e-01    1.639013e+03
1.500000e-01    7.759779e+02
2.000000e-01    4.571683e+02
2.500000e-01    3.035300e+02
3.000000e-01    2.607791e+02
4.000000e-01    2.054218e+02
6.000000e-01    1.470300e+02
8.000000e-01    1.161219e+02
1.000000e+00    9.676621e+01
2.000000e+00    5.512847e+01
3.000000e+00    3.976758e+01
4.000000e+00    3.183099e+01
5.000000e+00    2.546479e+01
6.000000e+00    2.122066e+01
7.000000e+00    1.818914e+01
8.000000e+00    1.591549e+01
9.000000e+00    1.414711e+01
1.000000e+01    1.273240e+01
2.000000e+01    1.273240e+01
3.000000e+01    1.273240e+01
4.000000e+01    1.273240e+01
5.000000e+01    1.273240e+01
6.000000e+01    1.273240e+01
7.000000e+01    1.273240e+01
8.000000e+01    1.273240e+01
9.000000e+01    1.273240e+01
1.000000e+02    1.273240e+01
2.000000e+02    1.273240e+01
3.000000e+02    1.273240e+01
4.000000e+02    1.273240e+01
5.000000e+02    1.273240e+01
6.000000e+02    1.273240e+01
7.000000e+02    1.273240e+01
8.000000e+02    1.273240e+01
9.000000e+02    1.273240e+01
1.000000e+03    1.273240e+01
2.000000e+03    1.273240e+01
3.000000e+03    1.273240e+01
4.000000e+03    1.273240e+01
5.000000e+03    1.273240e+01
6.000000e+03    1.273240e+01
7.000000e+03    1.273240e+01
8.000000e+03    1.273240e+01
9.000000e+03    1.273240e+01
1.000000e+04    1.273240e+01
2.000000e+04    1.273240e+01
3.000000e+04    1.273240e+01


"""
)
