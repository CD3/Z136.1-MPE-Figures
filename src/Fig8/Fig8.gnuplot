# Fig8_C.plt
# Correction factors Ca, Cb, Cc
# For ANSI Z136.1, make plot 4in x 8in
#
# Author: Brian J. Lund

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"

set multiplot layout 2,2

# Ca
set xrange [400.0:1400.0]
set yrange [0.9:11.0]
set logscale y
unset logscale x

set mxtics 5
set xtics 400, 100
# can't get gnuplot to produce the tics correctly on this,
# so we are manuualy adding the. the `set ytics` command
# can take a tuple where each element contains a tic value and level.
# 1 0 means tic at 1 with level 0 (major)
# 1 1 means tic at 1 with level 1 (minor)
set ytics ( 1 0, 10 0, 2 1, 3 1, 4 1, 5 1, 6 1, 7 1, 8 1, 9 1)
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 2, linestyle 3

set xlabel 'Wavelength (nm)'
set ylabel '{/=12 C_A}'

set format y '{%.0f}'
set format x '{%.0f}'

plot 'data.txt' index 0 notitle with lines linestyle 1

# Cb
set xrange [400:600]
set yrange [0.7:1400]
set xtics 400,50
set ytics 1,10
set mytics 5

set ylabel '{/=12 C_B}'

set format y '10^{%L}'
set format x '{%.0f}'

plot 'data.txt' index 1 notitle with lines linestyle 1

set xrange [1050:1400]
set yrange [0.44:2.2e+6]
set xtics 1050,50
set ytics 1,10

set ylabel '{/=12 C_C}'

set format x '{%.0f}'

plot 'data.txt' index 2 notitle with lines linestyle 1


set xrange [1300:1400]
set yrange [1e-3:2]
set xtics 1200,20
set ytics ( 0.01 0, 0.1 0, 1 0, 0.003 1, 0.03 1, 0.3 1)

set ylabel '{/=12 C_D}'

set format x '{%.0f}'

set key bottom left
unset key
set label 1 '1 x 10^{-13}  s' at first 1380, first 0.5e-2
set label 2 '1 x 10^{-12}  s' at first 1380, first 3e-2
set label 3 '5 x 10^{-12}  s' at first 1380, first 15e-2
set label 4 '1 x 10^{-11}  s' at first 1380, first 80e-2
plot 'data.txt' index 3 u 1:2 with lines linestyle 1 title "1e-13 s" ,\
     '' index 3 u 1:3 with lines linestyle 1 title "1e-12 s" ,\
     '' index 3 u 1:4 with lines linestyle 1 title "5e-12 s", \
     '' index 3 u 1:5 with lines linestyle 1 title "1e-11 s"

unset multiplot
