import pathlib

pathlib.Path("data.txt").write_text(
    """# Wavelength (nm)    Klambda
1200.0               100.0
1400.0                 1.0
"""
)
