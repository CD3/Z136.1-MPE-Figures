import pathlib

pathlib.Path("data-1.txt").write_text(
    """# alpha < 5 mrad
1.0   1.0
1.0e+6 1.0 
"""
)

pathlib.Path("data-2.txt").write_text(
    """# 5 mrad < alpha < alpha_max
1.0   1.0
40.0  0.4
1.0e+6 0.4
"""
)

pathlib.Path("data-3.txt").write_text(
    """# alpha > alpha_max
1.0   1.0
625.0  0.2
1.0e+6 0.2
"""
)
