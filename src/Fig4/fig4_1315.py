# fig4_1315.py
# MPE for 1315 nm, Plan D

wavelen = 1315.0

cc = 8.0 + 10.0**(0.04*(wavelen-1250.0))
klambda = 10.0**(0.01 * (1400.0 - wavelen))

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
tau = [ 1.0e-13, 9.9999e-12 ]
for i in range(-11, 1):
    for j in range(1,10):
        t = j * 10.0**i
        tau.append(t)

# Calculate and output the MPE values
fmtstr = '%.1e   %.3e'
for t in tau:
    mpe = mpe1315(t)
    print(fmtstr % (t, mpe))

