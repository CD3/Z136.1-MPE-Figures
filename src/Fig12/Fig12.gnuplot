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
set style line 10 linetype 1 linewidth 1 linecolor rgb "#d0d0d0"
set style line 11 linetype 1 linewidth 1 linecolor rgb "#f0f0f0"

set mytics 5
set mxtics 5
set xtics 1.0e-13, 10.0
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 10,linestyle 11

set xlabel 'Exposure Duration (s)'
set ylabel '{/Symbol a}_{max} (mrad)'

set format x '10^{%L}'
set format y '10^{%L}'

#plot 'alpha_max.dat' notitle with lines linestyle 1
plot 'data.txt' notitle with lines linestyle 1
