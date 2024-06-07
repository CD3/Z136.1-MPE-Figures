# Fig12_alpha_max.plt
# Plot of alpha_max vs exposure duration
# For ANSI Z136.1, make plot 5.5in x 3.25 in
#
# Author: Brian J. Lund

set xrange [1.0e-13:1.0e+5]
set yrange [1.0:1000.0]
set logscale xy

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"

set mytics 5
set mxtics 5
set xtics 1.0e-13, 10.0
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 2, linestyle 3

set xlabel 'Exposure Duration (s)'
set ylabel '{/Symbol a}_{max} (mrad)'

set format x '10^{%L}'
set format y '10^{%L}'

#plot 'alpha_max.dat' notitle with lines linestyle 1
plot '-' notitle with lines linestyle 1
# alpha_max
# t (s)    a_max (mrad)
1.0e-13       5.0
6.25e-4       5.0
0.25        100.0
3.0e+4      100.0
e


