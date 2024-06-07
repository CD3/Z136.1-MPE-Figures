# Fig8_C.plt
# Correction factors Ca, Cb, Cc
# For ANSI Z136.1, make plot 4in x 8in
#
# Author: Brian J. Lund

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"

set multiplot layout 3,1

# Ca
set xrange [400.0:1400.0]
set yrange [0.9:11.0]
set logscale y
unset logscale x

set mytics 10 
set mxtics 5
set xtics 400, 100
set ytics 1,10
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 2, linestyle 3

set xlabel 'Wavelength (nm)'
set ylabel '{/=12 C_A}'

set format y '{%.0f}'
set format x '{%.0f}'

plot 'C_factor.dat' index 0 notitle with lines linestyle 1

# Cb
set xrange [400:600]
set yrange [0.7:1400]
set xtics 400,50
set ytics 1,10
set mytics 5

set ylabel '{/=12 C_B}'

set format y '10^{%L}'
set format x '{%.0f}'

plot 'C_factor.dat' index 1 notitle with lines linestyle 1

set xrange [1050:1400]
set yrange [0.44:2.2e+6]
set xtics 1050,50
set ytics 1,10

set ylabel '{/=12 C_C}'

set format x '{%.0f}'

plot 'C_factor.dat' index 2 notitle with lines linestyle 1

unset multiplot
