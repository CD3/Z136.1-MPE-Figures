import pathlib

exec(pathlib.Path("../calculations.py").read_text())


with pathlib.Path("data.txt").open("w") as fd:
    a = D("100")
    Omega = D("3.14159") * (a / D("1000")) ** 2 / D("4")

    # Need to sample time from 1e-13 to 1 in order to capture the crossover between
    durations = []
    for power in range(-13, 0):
        for mantissa in [
            x / 2 for x in range(2, 20)
        ]:  # this gives 1.0, 1.5, 2.0, 2.5,...,9.5
            t = D(f"{mantissa}e{power}")
            if t > D("1"):
                break
            durations.append(t)

    # add a duration right below 1e-11 to help with plotting the sharp transision
    durations.append(D("0.9999e-11"))
    durations.sort()  # sort then so gnuplot can draw the lines correctly.

    l = D("400")
    fd.write("# 400 to 700 nm\n")
    for t in durations:
        t = D(t)
        val = MPE_VIS_ES(l, t, a) / Omega  # convert to integrated radiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")

    l = D("1064")
    fd.write("# 1064 nm\n")
    for t in durations:
        t = D(t)
        val = MPE_NIR_ES(l, t, a) / Omega  # convert to integrated radiance
        fd.write(f"{t:.1e} {val:.3e}\n")

    fd.write("\n")

    l = D("1315")
    fd.write("# 1315 nm\n")
    for t in durations:
        t = D(t)
        val = MPE_NIR_ES(l, t, a) / Omega  # convert to integrated radiance
        fd.write(f"{t:.1e} {val:.3e}\n")
exit()
import pathlib

pathlib.Path("data.txt").write_text(
    """# lambda = 400 nm - 700 nm
# t(s)    MPE(J/cm^2/sr)
1.00e-13    0.0169765272631
1.00e-11    0.0169765272631
1.00e-11    0.0339530545263
5.00e-06    0.0339530545263
5.00e-06    0.0323108857459
6.25e-04    1.20790109051
2.50e-01    5.40189789694
1.00e+00    15.2788745368


# lambda = 1064.0
# t(s)    MPE(J/cm^2/sr)
1.00e-13    0.0169765272631
1.00e-11    0.0169765272631
1.00e-11    0.339530545263
1.30e-05    0.339530545263
1.30e-05    0.330787339369
6.25e-04    6.03950545254
2.50e-01    27.0094894847
1.00e+00    76.3943726841


# lambda = 1315.0
# t(s)    MPE(J/cm^2/sr)
1.00e-13    6.89428945266
1.00e-11    6.89428945266
1.00e-11    137.885789053
1.30e-05    134.335110446
3.304e-5    270.415370462
6.25e-04    270.415370462
1.00e-03    270.415370462
1.00e-03   270.362358747
1.15e-03   270.817194458
1.33e-03   271.288346066
1.53e-03   271.776398857
1.76e-03   272.281959110
2.02e-03   272.805654855
2.33e-03   273.348136649
2.68e-03   273.910078387
3.09e-03   274.492178137
3.56e-03   275.095159008
4.09e-03   275.719770050
4.71e-03   276.366787182
5.43e-03   277.037014156
6.25e-03   277.731283557
7.20e-03   278.450457837
8.29e-03   279.195430386
9.54e-03   279.967126640
1.10e-02   280.766505235
1.26e-02   281.594559192
1.46e-02   282.452317158
1.68e-02   283.340844674
1.93e-02   284.261245510
2.22e-02   285.214663028
2.56e-02   286.202281602
2.95e-02   287.225328097
3.39e-02   288.285073386
3.91e-02   289.382833928
4.50e-02   290.519973412
5.18e-02   291.697904439
5.96e-02   292.918090289
6.87e-02   294.182046727
7.91e-02   295.491343897
9.10e-02   296.847608263
1.05e-01   298.252524636
1.21e-01   299.707838264
1.39e-01   301.215357002
1.60e-01   302.776953553
1.84e-01   304.394567801
2.12e-01   306.070209218
2.44e-01   307.805959356
2.81e-01   309.603974441
3.24e-01   311.466488045
3.73e-01   313.395813862
4.29e-01   315.394348586
4.94e-01   317.464574883
5.69e-01   319.609064477
6.55e-01   321.830481347
7.54e-01   324.131585033
8.69e-01   326.515234067
1.00e+00   328.984389520
"""
)
