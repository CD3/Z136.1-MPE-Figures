import math
from decimal import Decimal as D

#
# Functions for calculating various parameter, correction factors, and MPEs.
# Adapted by CD Clark III from scripts originally written by Brian Lund.
#
# Note that all of these functions work with decimal.Deminal types instead of
# floats so that we do not have to deal with floating point rounding issues.
# This does mean that we need manually convert literals to decimal.Decimal, which is
# why you will see D("6.25e-4") and D("1") for example.


def round_to_sigfigs(v: D, n: int):
    """
    Round a Decimal number to the given number of significant figures.
    """
    fmtstr = "{:." + str(n - 1) + "e}"
    return D(fmtstr.format(v))


# PARAMETERS

alpha_min = D("1.5")


def alpha_max(t: D) -> D:
    if t < D("6.25e-4"):
        return D("5.0")

    if t < D("0.25"):
        return D("200.0") * t ** D("0.5")

    return D("100.0")


def T_1(l: D) -> D:
    return D(10) * 10 ** (D("0.02") * (l - D(450)))


def T_2(a: D) -> D:
    if a < D("1.5"):
        return D("10")
    if a < D("100"):
        return D("10") * 10 ** ((a - D("1.5")) / D("98.5"))

    return D("100")


# CORRECTION FACTORS


def C_A(l: D) -> D:
    if l <= D("700"):
        return 1
    if l <= D("1050"):
        return 10 ** (D("0.002") * (l - D("700")))

    return D("5")


def C_B(l: D) -> D:
    if l <= D("450"):
        return D("1")

    return 10 ** (D("0.02") * (l - D("450")))


def C_C(l: D) -> D:
    if l <= D("1150"):
        return D("1")
    if l <= D("1200"):
        return 10 ** (D("0.018") * (l - D("1150.0")))

    return D("8.0") + 10 ** (D("0.04") * (l - D("1250")))


def C_E(a: D, t: D) -> D:
    amax = alpha_max(t)
    if a < alpha_min:
        return D("1.0")
    if a < amax:
        return a / alpha_min

    return (a * a) / (amax * alpha_min)


def gamma(t: D) -> D:
    if t <= D("100"):
        return D("11")
    if t <= D("10000"):
        return D("1.1") * t ** D("0.5")

    return D("110")


def C_g(a: D, g: D) -> D:
    if a <= g:
        return D("1.0")
    return (a / g) ** 2


def K_lambda(l: D) -> D:
    return 10 ** (D("0.01") * (D("1400.0") - l))


def C_P(a: D, a_max: D, n: D) -> D:
    if a <= D("5"):
        return D("1.0")

    if a <= a_max:
        if n <= D("40"):
            return n ** D("-0.25")
        else:
            return D("0.4")

    if a <= D("100"):
        if n <= D("625"):
            return n ** D("-0.25")
        else:
            return D("0.2")

    return D("1.0")


# MPEs
# NOTE: Wavelength and duration ranges are INCLUSIVE on the LEFT and EXCLUSIVE on the RIGHT
#       So when checking to see if a wavelength or duration is inside a range we would do
#       t >= lower_bound and t < upper_bound
#
#       In practice, we can just check the upper bounds after checking the first lower bound
#
#       if t < lower_bound_1:
#          return None
#       if t < upper_bound_1:
#          return compute_mpe_for_lower_bound_1_to_upper_bound_1
#       if t < upper_bound_2:
#          return compute_mpe_for_upper_bound_1_to_upper_bound_2
#       ...


def MPE_UV_THERM(l: D, t: D) -> D:
    if l < D("180") or l >= D("400"):
        return None
    if t < D("1e-13") or t >= D("30000"):
        return None

    if t < D("1e-11"):
        return D("3e-4")

    if t < D("1e-9"):
        return D("1e-3")

    if t < D("10"):
        return D("0.56") * t ** D("0.25")

    return None


def MPE_UV_PHOTO(l: D, t: D) -> D:
    if l < D("180") or l >= D("400"):
        return None
    if t < D("1e-9") or t >= D("30000"):
        return None

    if l < D("260"):
        return D("0.003") * 10 ** (D("0.033") * (D("260") - l))
    if l < D("302.5"):
        return D("3e-3")
    if l < D("315"):
        return 10 ** (D("0.2") * (l - D("295"))) * D("1e-4")
    if l < D("400"):
        if t < D("10"):
            return None
        return D("1.0")


def MPE_UV(l: D, t: D) -> D:
    mpe_t = MPE_UV_THERM(l, t)
    mpe_p = MPE_UV_PHOTO(l, t)

    if mpe_t is None:
        return mpe_p
    if mpe_p is None:
        return mpe_t

    return min(mpe_t, mpe_p)


def MPE_VIS_PS(l: D, t: D) -> D:
    if l < D("400") or l >= D("700"):
        return None
    if t < D("1e-13") or t >= D("30000"):
        return None

    # MPE is the same for all wavelengths from 10**-13 to 10 s
    if t < D("1e-11"):
        return D("1.0e-7")
    if t < D("5e-6"):
        return D("2.0e-7")
    if t < D("10"):
        return D("1.8") * t ** D("0.75") * D("1e-3")

    if l < D("450"):
        if t < D("100"):
            return D("1.0e-2")

        return C_B(l) * D("1e-4") * t  # convert to radient exposure

    if l < D("500"):
        if t < T_1(l):
            return D("1.0e-3") * t
        if t < D("100"):
            return C_B(l) * D("1e-2")

        return C_B(l) * D("1e-4") * t  # convert to radient exposure

    if l < D("700"):
        return D("1e-3") * t  # convert to radient exposure


def MPE_NIR_PS_RETINA(l: D, t: D) -> D:
    if l < D("700") or l >= D("1400"):
        return None
    if t < D("1e-13") or t >= D("30000"):
        return None

    if l < D("1050"):
        if t < D("1e-11"):
            return D("1.0e-7")
        if t < D("5e-6"):
            return D("2.0") * C_A(l) * D("1e-7")
        if t < D("10"):
            return D("1.8") * C_A(l) * t ** D("0.75") * D("1e-3")
        if t < D("30000"):
            #      W / cm^2             convert to J/cm^2
            return C_A(l) * D("1e-3") * t

    if l < D("1200") or l < D("1400"):  # retinal MPEs are same from 1050 - 1400
        if t < D("1e-11"):
            return C_C(l) * D("1e-7")
        if t < D("13e-6"):
            return D("2.0") * C_C(l) * D("1e-6")
        if t < D("10"):
            return D("9.0") * C_C(l) * t ** D("0.75") * D("1e-3")
        if t < D("30000"):
            return D("5.0") * C_C(l) * D("1e-3") * t


def MPE_NIR_PS_CORNEA(l: D, t: D) -> D:
    if l < D("1200") or l >= D("1400"):
        return None
    if t < D("1e-11") or t >= D("30000"):
        return None

    if t < D("1e-3"):
        return D("0.3") * K_lambda(l)
    if t < D("4"):
        return D("0.3") * K_lambda(l) + D("0.56") * t ** D("0.25") - D("0.1")
    if t < D("10"):
        return D("0.3") * K_lambda(l) + D("0.7")
    if t < D("30000"):
        return (D("0.03") * K_lambda(l) + D("0.07")) * t


def MPE_NIR_PS(l: D, t: D) -> D:
    mpe_r = MPE_NIR_PS_RETINA(l, t)
    mpe_c = MPE_NIR_PS_CORNEA(l, t)
    if mpe_c is None and mpe_r is None:
        return None
    if mpe_c is None:
        return mpe_r
    if mpe_r is None:
        return mpe_c
    # FIXME: we need to compare MPE:Q
    return min(mpe_r, mpe_c)


def MPE_FIR(l: D, t: D) -> D:
    if l < D("1400") or l >= D("1000000"):
        return None
    if t < D("1e-13") or t >= D("30000"):
        return None

    if l < D("1500"):
        if t < D("1e-11"):
            return D("0.03")
        if t < D("1e-9"):
            return D("0.1")
        if t < D("1e-3"):
            return D("0.3")
        if t < D("4"):
            return D("0.56") * t ** D("0.25") + D("0.2")
        if t < D("10"):
            return D("1.0")

        return D("0.1") * t

    if l < D("1800"):
        if t < D("1e-11"):
            return D("0.1")
        if t < D("1e-9"):
            return D("0.3")
        if t < D("10"):
            return D("1.0")

        return D("0.1") * t
    if l < D("2600"):
        if t < D("1e-11"):
            return D("0.01")
        if t < D("1e-9"):
            return D("0.03")
        if t < D("1e-3"):
            return D("0.1")
        if t < D("10"):
            return D("0.56") * t ** D("0.25")

        return D("0.1") * t

    if l < D("1000000"):
        if t < D("1e-11"):
            return D("1e-3")
        if t < D("1e-9"):
            return D("3e-3")
        if t < D("1e-7"):
            return D("1e-2")
        if t < D("10"):
            return D("0.56") * t ** D("0.25")

        return D("0.1") * t


def MPE_VIS_ES_THERMAL(l: D, t: D, a: D) -> D:
    if a <= D("1.5"):
        return MPE_VIS_PS(l, t)
    if l < D("400") or l >= D("700"):
        return None
    if t < D("1e-13") or t >= D("30000"):
        return None

    if t < D("1e-11"):
        return C_E(a, t) * D("1e-7")
    if t <= D("5e-6"):
        return D("2.0") * C_E(a, t) * D("1e-7")
    # if t < D("0.7"):
    if t < T_2(a):
        return D("1.8") * C_E(a, t) * t ** D("0.75") * D("1e-3")

    return D("1.8") * C_E(a, t) * T_2(a) ** D("-0.25") * D("1e-3") * t


def MPE_VIS_ES_PHOTO(l: D, t: D, a: D) -> D:
    if l < D("400") or l >= D("600"):
        return None
    if t < D("0.7") or t >= D("30000"):
        return None

    if t < D("100"):
        return C_B(l) * C_g(a, gamma(t)) * D("1e-2")

    return C_B(l) * C_g(a, gamma(t)) * D("1e-4") * t


def MPE_VIS_ES(l: D, t: D, a: D) -> D:
    if a <= D("1.5"):
        return MPE_VIS_PS(l, t)

    mpe_t = MPE_VIS_ES_THERMAL(l, t, a)
    mpe_p = MPE_VIS_ES_PHOTO(l, t, a)
    if mpe_t is None and mpe_p is None:
        return None
    if mpe_t is None:
        return mpe_p
    if mpe_p is None:
        return mpe_t

    return min(mpe_t, mpe_p)


def MPE_NIR_ES_RETINA(l: D, t: D, a: D) -> D:
    if l < D("700") or l >= D("1400"):
        return None
    if t < D("1e-13") or t >= D("30000"):
        return None

    if l < D("1050"):
        if t < D("1e-11"):
            return C_E(a, t) * D("1e-7")
        if t < D("5e-6"):
            return D("2.0") * C_A(l) * C_E(a, t) * D("1e-7")
        if t < T_2(a):
            return D("1.8") * C_A(l) * C_E(a, t) * t ** D("0.75") * D("1e-3")
        if t < D("30000"):
            return D("1.8") * C_A(l) * C_E(a, t) * T_2(a) ** D("-0.25") * D("1e-3") * t
    if l < D("1200") or l < D("1400"):  # Retina MPE is same from 1050 - 1400 nm
        if t < D("1e-11"):
            return C_C(l) * C_E(a, t) * D("1e-7")
        if t < D("13e-6"):
            return D("2.0") * C_C(l) * C_E(a, t) * D("1e-6")
        if t < T_2(a):
            return D("9.0") * C_C(l) * C_E(a, t) * t ** D("0.75") * D("1e-3")
        if t < D("30000"):
            return D("9.0") * C_C(l) * C_E(a, t) * T_2(a) ** D("-0.25") * D("1e-3") * t


def MPE_NIR_ES_CORNEA(l: D, t: D, a: D) -> D:
    if l < D("1200") or l >= D("1400"):
        return None
    if t < D("1e-11") or t >= D("30000"):
        return None

    if t < D("13e-6") or t < D("1e-3"):
        return D("0.3") * K_lambda(l)
    if t < D("4"):
        return D("0.3") * K_lambda(l) + D("0.56") * t ** D("0.25") - D("0.1")
    if t < D("10"):
        return D("0.3") * K_lambda(l) + D("0.7")
    if t < D("30000"):
        return (D("0.03") * K_lambda(l) + D("0.07")) * t


def MPE_NIR_ES(l: D, t: D, a: D) -> D:
    mpe_r = MPE_NIR_ES_RETINA(l, t, a)
    mpe_c = MPE_NIR_ES_CORNEA(l, t, a)
    if mpe_c is None and mpe_r is None:
        return None
    if mpe_c is None:
        return mpe_r
    if mpe_r is None:
        return mpe_c
    # FIXME: we need to compare MPE:Q
    return min(mpe_r, mpe_c)


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
