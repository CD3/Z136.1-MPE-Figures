import math

# use decimal module so we don't have to deal with floating point rounding
from decimal import Decimal as D

#
# Functions for calculating various parameter, correction factors, and MPEs.
# Adapted by CD Clark III from scripts originally written by Brian Lund.
#

# PARAMETERS

alpha_min = 1.5


def alpha_max(t):
    if t < 6.25e-4:
        result = 5.0
    elif t < 0.25:
        result = 200.0 * math.sqrt(t)
    else:
        result = 100.0
    return result


def T_1(l):
    return D(10) * 10 ** (D("0.02") * (l - D(450)))


def T_2(a):
    if a <= D("1.5"):
        return D("10")
    if a <= D("100"):
        return D("10") * 10 ** ((a - D("1.5")) / D("98.5"))

    return D("100")


# CORRECTION FACTORS


def C_A(l):
    if l <= D("700"):
        return 1
    if l <= D("1050"):
        return 10 ** (D("0.002") * (l - D("700")))

    return D("5")


def C_B(l):
    if l <= D("450"):
        return D("1")

    return 10 ** (D("0.02") * (l - D("450")))


def C_C(l):
    if l <= D("1150"):
        return D("1")
    if l <= D("1200"):
        return 10 ** (D("0.018") * (l - D("1150.0")))

    return D("8.0") + 10 ** (D("0.04") * (l - D("1250")))


def C_E(alpha, t):
    amax = alpha_max(t)
    if alpha < alpha_min:
        result = 1.0
    elif alpha < alpha_min:
        result = alpha / amax
    else:
        result = (alpha * alpha) / (amax * alpha_min)
    return result


def gamma(t):
    if t <= D("100"):
        return D("11")
    if t <= D("10000"):
        return D("1.1") * t ** D("0.5")

    return D("110")


def C_g(alpha, g):
    if alpha <= g:
        return D("1.0")
    return (alpha / g) ** 2


def K_lambda(l):
    return 10 ** (D("0.01") * (D("1400.0") - l))


# MPEs


def mpe_ret(wavelength, t, alpha=1):
    if t < 1.0e-11:
        result = (1.0e-7) * C_C(wavelength) * C_E(alpha, t)
    elif t < 1.3e-5:
        result = (2.0e-6) * C_C(wavelength) * C_E(alpha, t)
    else:
        result = (0.009) * C_C(wavelength) * C_E(alpha, t) * t**0.75
    return result


def mpe_cornea(wavelength, t):
    if t < 1.0e-11:
        result = 1.0e20
    elif t < 1.0e-3:
        result = 0.3 * K_lambda(wavelength)
    elif t < 4:
        result = 0.3 * K_lambda(wavelength) + 0.56 * t**0.75 - 0.1
    return result


# def main():
#     alpha = 100
#     wavelength = 1315
#     dur = [1.0e-13, 1.0e-11, 1.3e-5, 6.25e-4, 1.0e-3, 0.25, 1.0]
#     amax = [alpha_max(x) for x in dur]
#     Ce = [C_E(alpha, x) for x in dur]
#     MPEret = [mpe_ret(wavelength, alpha, x) for x in dur]
#     MPEcor = [mpe_cornea(wavelength, x) for x in dur]
#     MPE = [min(x, y) for x, y in zip(MPEret, MPEcor)]
#     lblstr = "  t(s)        C_E      MPE(ret)    MPE(cor)    MPE"
#     fmtstr = "{0:8.2e}   {1:8.2e}    {2:8.2e}    {3:8.2e}    {4:8.2e}"
#     print(lblstr)
#     for i in range(len(dur)):
#         print(fmtstr.format(dur[i], Ce[i], MPEret[i], MPEcor[i], MPE[i]))


# if __name__ == "__main__":
#     main()

# # fig4_1315.py
# # MPE for 1315 nm, Plan D

# wavelen = 1390.0

# cc = 8.0 + 10.0 ** (0.04 * (wavelen - 1250.0))
# klambda = 10.0 ** (0.01 * (1400.0 - wavelen))


# def mpe1390(t):
#     if t < 1.0e-11:
#         return 1.0e-7 * cc
#     if t < 1.3e-5:
#         mret = 2.0e-6 * cc
#         mcorn = 0.3 * klambda
#         return min(mret, mcorn)
#     if t < 1.0e-3:
#         mret = 9.0e-3 * cc * t**0.75
#         mcorn = 0.3 * klambda
#         return min(mret, mcorn)
#     if t < 4.0:
#         mret = 9.0e-3 * cc * t**0.75
#         mcorn = 0.3 * klambda + 0.56 * t**0.25 - 0.1
#         return min(mret, mcorn)
#     if t < 10.0:
#         mret = 9.0e-3 * cc * t**0.75
#         mcorn = 0.3 * klambda + 0.7
#         return min(mret, mcorn)
#     # t >= 10.0
#     mret = 5.0e-3 * cc * t
#     mcorn = 0.3 * klambda + 0.1 * t - 0.3
#     return min(mret, mcorn)


# # set up pulse durations for MPE calculations
# tau = [1.0e-13, 9.9999e-12]
# for i in range(-11, 1):
#     for j in range(1, 10):
#         t = j * 10.0**i
#         tau.append(t)

# # Calculate and output the MPE values
# fmtstr = "%.1e   %.3e"
# for t in tau:
#     mpe = mpe1390(t)
#     print(fmtstr % (t, mpe))

# # fig4_1315.py
# # MPE for 1315 nm, Plan D

# wavelen = 1315.0

# cc = 8.0 + 10.0 ** (0.04 * (wavelen - 1250.0))
# klambda = 10.0 ** (0.01 * (1400.0 - wavelen))


# def mpe1315(t):
#     if t < 1.0e-11:
#         return 1.0e-7 * cc
#     if t < 1.3e-5:
#         mret = 2.0e-6 * cc
#         mcorn = 0.3 * klambda
#         return min(mret, mcorn)
#     if t < 1.0e-3:
#         mret = 9.0e-3 * cc * t**0.75
#         mcorn = 0.3 * klambda
#         return min(mret, mcorn)
#     if t < 4.0:
#         mret = 9.0e-3 * cc * t**0.75
#         mcorn = 0.3 * klambda + 0.56 * t**0.25 - 0.1
#         return min(mret, mcorn)
#     if t < 10.0:
#         mret = 9.0e-3 * cc * t**0.75
#         mcorn = 0.3 * klambda + 0.7
#         return min(mret, mcorn)
#     # t >= 10.0
#     mret = 5.0e-3 * cc * t
#     mcorn = 0.3 * klambda + 0.1 * t - 0.3
#     return min(mret, mcorn)


# # set up pulse durations for MPE calculations
# tau = [1.0e-13, 9.9999e-12]
# for i in range(-11, 1):
#     for j in range(1, 10):
#         t = j * 10.0**i
#         tau.append(t)

# # Calculate and output the MPE values
# fmtstr = "%.1e   %.3e"
# for t in tau:
#     mpe = mpe1315(t)
#     print(fmtstr % (t, mpe))
