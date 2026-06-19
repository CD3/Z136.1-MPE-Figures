# Fig5_UV_MPE.plt
# Plot UV Photochemical MPE for Skin and Ocular Exposure
# For ANSI Z136.1, make plot 4in x 3in
#
# Author: Brian J. Lund

set xrange [180:400]
set yrange [1e-3:10]
set logscale y
unset logscale x

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"

set xtics 200,50,400
set ytics 1.0e-3,10
set mytics 10
set mxtics 5
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 2, linestyle 3

#set xlabel '{/=20 Wavelength (nm)}'
#set ylabel '{/=20 Radiant Exposure (J/cm^2)}'
set xlabel 'Wavelength (nm)'
set ylabel 'Radiant Exposure (J/cm^2)'

set format x '{%.0f}'
set format y '10^{%L}'

plot '-' notitle with lines linestyle 1
# Ultriviolet Photochemical MPE
# # Wavelenght      MP (J/cm^2)
180                 1.31
260                 3.0e-3
302.5               3.0e-3
302.5               3.2e-3
315                 1.0
400                 1.0
e

