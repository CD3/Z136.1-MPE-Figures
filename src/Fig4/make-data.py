# generate datafiles for figure 4.
# values for 400-1064 and 1400 orignally computed by Brian Lund
# code to compute values for 1315 and 1390 originally written by Brian Lund
import pathlib

with pathlib.Path("data.txt").open("w") as fd:
    ########################################
    ##  400 - 1064                        ##
    ########################################
    fd.write(
        """# Plan E
# MPE for 400 to 700 nm
1.0e-13   1.000e-07
1.0e-11   1.000e-07
1.0e-11   2.000e-07
5.0e-06   2.000e-07
1.0e+01   1.012e-02


# MPE for 850 nm
1.0e-13   1.000e-07
1.0e-11   1.000e-07
1.0e-11   3.991e-07
5.0e-06   3.991e-07
1.0e+01   1.995e-02


# MPE for 1064 nm
1.0e-13   1.000e-07
1.0e-11   1.000e-07
1.0e-11   2.000e-06
1.3e-05   2.000e-06
1.0e+01   5.000e-02
"""
    )

    ########################################
    ##   1315                             ##
    ########################################
    # MPE for 1315 nm, Plan D
    wavelen = 1315.0

    cc = 8.0 + 10.0 ** (0.04 * (wavelen - 1250.0))
    klambda = 10.0 ** (0.01 * (1400.0 - wavelen))

    def mpe1315(t):
        if t < 1.0e-11:
            return 1.0e-7 * cc
        if t < 1.3e-5:
            mret = 2.0e-6 * cc
            mcorn = 0.3 * klambda
            return min(mret, mcorn)
        if t < 1.0e-3:
            mret = 9.0e-3 * cc * t**0.75
            mcorn = 0.3 * klambda
            return min(mret, mcorn)
        if t < 4.0:
            mret = 9.0e-3 * cc * t**0.75
            mcorn = 0.3 * klambda + 0.56 * t**0.25 - 0.1
            return min(mret, mcorn)
        if t < 10.0:
            mret = 9.0e-3 * cc * t**0.75
            mcorn = 0.3 * klambda + 0.7
            return min(mret, mcorn)
        # t >= 10.0
        mret = 5.0e-3 * cc * t
        mcorn = 0.3 * klambda + 0.1 * t - 0.3
        return min(mret, mcorn)

    # set up pulse durations for MPE calculations
    tau = [1.0e-13, 9.9999e-12]
    for i in range(-11, 1):
        for j in range(1, 10):
            t = j * 10.0**i
            tau.append(t)

    # Calculate and output the MPE values
    fd.write("\n\n# MPE for 1315 nm\n")
    fmtstr = "%.1e   %.3e\n"
    for t in tau:
        mpe = mpe1315(t)
        fd.write(fmtstr % (t, mpe))

    ########################################
    ##  1390                              ##
    ########################################

    # MPE for 1315 nm, Plan D

    wavelen = 1390.0

    cc = 8.0 + 10.0 ** (0.04 * (wavelen - 1250.0))
    klambda = 10.0 ** (0.01 * (1400.0 - wavelen))

    def mpe1390(t):
        if t < 1.0e-11:
            return 1.0e-7 * cc
        if t < 1.3e-5:
            mret = 2.0e-6 * cc
            mcorn = 0.3 * klambda
            return min(mret, mcorn)
        if t < 1.0e-3:
            mret = 9.0e-3 * cc * t**0.75
            mcorn = 0.3 * klambda
            return min(mret, mcorn)
        if t < 4.0:
            mret = 9.0e-3 * cc * t**0.75
            mcorn = 0.3 * klambda + 0.56 * t**0.25 - 0.1
            return min(mret, mcorn)
        if t < 10.0:
            mret = 9.0e-3 * cc * t**0.75
            mcorn = 0.3 * klambda + 0.7
            return min(mret, mcorn)
        # t >= 10.0
        mret = 5.0e-3 * cc * t
        mcorn = 0.3 * klambda + 0.1 * t - 0.3
        return min(mret, mcorn)

    # set up pulse durations for MPE calculations
    tau = [1.0e-13, 9.9999e-12]
    for i in range(-11, 1):
        for j in range(1, 10):
            t = j * 10.0**i
            tau.append(t)

    # Calculate and output the MPE values
    fd.write("\n\n# MPE for 1390 nm\n")
    fmtstr = "%.1e   %.3e\n"
    for t in tau:
        mpe = mpe1390(t)
        fd.write(fmtstr % (t, mpe))

    fd.write("""

# MPE for 1400 nm
1.0e-09   3.000e-01
1.0e-03   2.996e-01
4.0e+00   1.000e+00
1.0e+01   1.000e+00
""")
