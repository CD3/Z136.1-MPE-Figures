import pathlib

pathlib.Path("data.txt").write_text(
    """# alpha_max
# t (s)    a_max (mrad)
1.0e-13       5.0
6.25e-4       5.0
0.25        100.0
3.0e+4      100.0
"""
)
