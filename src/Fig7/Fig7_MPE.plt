# Fig7_MPE.plt
# Plot MPE in visible for extended source
# For ANSI Z135.1, make plot 5in x 3.25in
#
# Author: Brian J. Lund

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"

set xrange [1.0e-13:1]
set yrange [1.0e-8:1]
set logscale xy

set mytics 5
set mxtics 5
set xtics 1.0e-13, 10
set ytics 1.0e-8, 10
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 2, linestyle 3

set xlabel 'Exposure Duration (s)'
set ylabel 'Radiant Exposure (J/cm^2)'

set format x ' 10^{%L}'
set format y ' 10^{%L}'

set label 1 '{/Symbol a \243 a}_{min}' at first 3e-8, first 3.5e-7 center
set label 2 '{/Symbol a} = 7.5 mrad' at first 3e-8, first 3.0e-6 center
set label 3 '{/Symbol a} = 25 mrad' at first 3e-8, first 3.0e-5 center
set label 4 '{/Symbol a} = 100 mrad' at first 3e-8, first 5.0e-4 center

plot 'figure7.dat' notitle with lines linestyle 1


unset label 1
unset label 2
unset label 3
unset label 4
