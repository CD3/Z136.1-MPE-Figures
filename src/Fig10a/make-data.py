import pathlib

exec(pathlib.Path("../calculations.py").read_text())

# NOTE: In 2007 there were dual limits for the point source visible MPEs.
#       These were removed in 2014 but the figure still references
#       thermal vs photochemical in both 2014 and 2022 versions.

with pathlib.Path("data.txt").open("w") as fd:
    fd.write("# t [s]   MPE [W/cm^2]\n")

    # We want to create a graph of MPE vs. exposure duration
    # from 0.1 s to 30,000 s# for visible and near infrared
    # wavelengths. Note that we can't (technically) calculate the
    # MPE for 30,000 s because it's "not defined" (time ranges
    # in the standard are exclusive on the right side).

    # Exposure druations need to be chosen to capture any changes
    # in slope.
    durations = []
    for power in range(-1, 5):
        for mantissa in [
            "1",
            "1.25",
            "1.5",
            "2",
            "2.25",
            "2.5",
            "3",
            "3.5",
            "4",
            "4.5",
            "5",
            "6",
            "7",
            "8",
            "9",
        ]:
            t = D(f"{mantissa}e{power}")
            if t >= D("30000"):
                break
            durations.append(t)
    durations.append("29999.9999")

    wavelengths = ["400", "475", "490", "500"]
    for l in wavelengths:
        fd.write(f"# {l} nm\n")
        l = D(l)
        for t in durations:
            t = D(t)
            val = MPE_VIS_PS(l, t) / t  # convert to irradiance
            fd.write(f"{t:.1e} {val:.3e}\n")
        fd.write("\n")

    wavelengths = ["850", "1064", "1315", "1399.9999"]
    for l in wavelengths:
        fd.write(f"# {l} nm\n")
        l = D(l)
        for t in durations:
            t = D(t)
            val = MPE_NIR_PS(l, t) / t  # convert to irradiance
            fd.write(f"{t:.1e} {val:.3e}\n")
        fd.write("\n")
