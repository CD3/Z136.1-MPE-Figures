import pathlib

pathlib.Path("data-1.txt").write_text(
    """
# C_g for photochemical MPEs
# alpha = 1.5 mrad to 11 mrad
# gamma (mrad)    C_g
11.0              1.0
110.0             1.0
"""
)

pathlib.Path("data-2.txt").write_text("""
# C_g for photochemical MPEs
# alpha = 25 mrad
# gamma (mrad)    C_g
11.0              5.17
25.0              1.0
110.0             1.0
""")

pathlib.Path("data-3.txt").write_text("""
# C_g for photochemical MPEs
# alpha = 50 mrad
# gamma (mrad)    C_g
11.0              20.66
50.0              1.0
110.0             1.0
""")

pathlib.Path("data-4.txt").write_text("""
# C_g for photochemical MPEs
# alpha = 75 mrad
# gamma (mrad)    C_g
11.0              46.49
75.0              1.0
110.0             1.0
""")

pathlib.Path("data-5.txt").write_text("""
# C_g for photochemical MPEs
# alpha = 100 mrad
# gamma (mrad)    C_g
11.0              82.64
100.0             1.0
110.0             1.0
""")
