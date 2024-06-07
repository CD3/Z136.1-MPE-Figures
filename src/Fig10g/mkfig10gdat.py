# mkfig10gdat.py
# Create a data file for Z136.1 figure 10g
import math

alpha_min = 1.5

# Wavelength dependent factor C_C
def C_c(wavelength) :
    if wavelength < 1150:
        result = 1.0
    elif wavelength < 1200 :
        exponent = 0.018 * (wavelength - 1150.0)
        result = 10**exponent
    elif wavelength < 1400.0 :
        exponent = 0.04 * (wavelength - 1250)
        result = 8.0 + 10.0**exponent
    else :
        result = 1
    return result

def K_lambda(wavelength) :
    exponent = 0.01 * (1400.0 - wavelength)
    return 10.0**exponent

def alpha_max(t) :
    if t < 6.25e-4 :
        result = 5
    elif t < 0.25 :
        result = 200.0 * math.sqrt(t)
    else :
        result = 100.0
    return result

def C_e(alpha, t) :
    amax = alpha_max(t)
    if alpha < alpha_min :
        result = 1.0
    elif alpha < alpha_min:
        result = alpha / amax
    else :
        result = (alpha * alpha) / (amax * alpha_min)
    return result

def mpe_ret(wavelength, alpha, t) :
    if t < 1.0e-11:
        result = (1.0e-7) * C_c(wavelength) * C_e(alpha, t)
    elif t < 1.3e-5:
        result = (2.0e-6) * C_c(wavelength) * C_e(alpha, t)
    else :
        result = (0.009) * C_c(wavelength) * C_e(alpha, t) * t**0.75
    return result

def mpe_cornea(wavelength, t):
    if t < 1.0e-11:
        result = 1.0e20
    elif t < 1.0e-3:
        result = 0.3 * K_lambda(wavelength)
    elif t < 4:
        result = 0.3 * K_lambda(wavelength) + 0.56*t**0.75-0.1
    return result

def main():
    alpha = 100
    wavelength = 1315
    dur = [1.0e-13, 1.0e-11, 1.3e-5, 6.25e-4, 1.0e-3, 0.25, 1.0]
    amax = [alpha_max(x) for x in dur]
    Ce = [C_e(alpha, x) for x in dur]
    MPEret = [mpe_ret(wavelength, alpha, x) for x in dur]
    MPEcor = [mpe_cornea(wavelength, x) for x in dur]
    MPE = [min(x,y) for x,y in zip(MPEret,MPEcor)]
    lblstr = "  t(s)        C_E      MPE(ret)    MPE(cor)    MPE"
    fmtstr = "{0:8.2e}   {1:8.2e}    {2:8.2e}    {3:8.2e}    {4:8.2e}"
    print(lblstr)
    for i in range(len(dur)):
        print(fmtstr.format(dur[i], Ce[i], MPEret[i], MPEcor[i], MPE[i]))


if __name__ == "__main__":
    main()

