import pathlib
from decimal import Decimal as D

exec(pathlib.Path("../calculations.py").read_text())

with pathlib.Path("data.txt").open("w") as fd:
    fd.write("# Ultriviolet Photochemical MPE\n")
    fd.write("# Wavelength  MPE[J/cm^2]\n")
    for l in ["180", "260", "302.499", "302.501", "315", "399.99"]:
        val = MPE_UV_PHOTO(D(l), D("1e-8"))
        fd.write(f"{D(l):.1f} {val:.3g}\n")
