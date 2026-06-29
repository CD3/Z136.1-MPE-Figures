# generate datafiles for figure 4.
# values for 400-1064 and 1400 orignally computed by Brian Lund
# code to compute values for 1315 and 1390 originally written by Brian Lund
import pathlib

exec(pathlib.Path("../calculations.py").read_text())

with pathlib.Path("data.txt").open("w") as fd:
    ########################################
    ##  400 - 700 nm                      ##
    ########################################
    l = D("532")
    fd.write("# MPE for 400 to 700 nm\n")
    for t in ["1.001e-13", "1.0e-11", "1.0001e-11", "5.0e-6", "1.0e+01"]:
        t = D(t)
        val = MPE_VIS_PS(l, t)
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    ########################################
    ##  850 nm                            ##
    ########################################
    l = D("850")
    fd.write(f"# MPE for {l} nm\n")
    for t in ["1.001e-13", "0.9999e-11", "1.0e-11", "4.9999e-6", "1.0e+01"]:
        t = D(t)
        val = MPE_NIR_PS(l, t)
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    ########################################
    ##  1064 nm                           ##
    ########################################
    l = D("1064")
    fd.write(f"# MPE for {l} nm\n")
    for t in ["1.001e-13", "0.9999e-11", "1.0e-11", "4.9999e-6", "1.0e+01"]:
        t = D(t)
        val = MPE_NIR_PS(l, t)
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    ########################################
    ##   1315                             ##
    ########################################

    l = D("1315")
    fd.write(f"# MPE for {l} nm\n")
    # set up pulse durations for MPE calculations
    durations = [1.0e-13, 9.9999e-12]
    for i in range(-11, 1):
        for j in range(1, 10):
            t = round_to_sigfigs(D(j * 10.0**i), 2)
            durations.append(t)
    for t in durations:
        val = MPE_NIR_PS(l, t)
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    ########################################
    ##  1390                              ##
    ########################################
    l = D("1390")
    fd.write(f"# MPE for {l} nm\n")
    # set up pulse durations for MPE calculations
    durations = [1.0e-13, 9.9999e-12]
    for i in range(-11, 1):
        for j in range(1, 10):
            t = round_to_sigfigs(D(j * 10.0**i), 2)
            durations.append(t)
    for t in durations:
        val = MPE_NIR_PS(l, t)
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")
    ########################################
    ##  1400                              ##
    ########################################
    l = D("1400")
    fd.write(f"# MPE for {l:.0f} nm\n")
    # set up pulse durations for MPE calculations
    durations = ["1.0e-9", "1.0e-3", "4.0", "1.0e1"]
    for t in durations:
        t = D(t)
        val = MPE_NIR_PS(l, t)
        fd.write(f"{t:.1e} {val:.3e}\n")
