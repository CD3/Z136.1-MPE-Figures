# Fig10g_MPE.plt
# MPE for visible and near infrared for sources subtending an angle
# of alpha_max(t).  MPE given as Integrated Radiance (J/cm^2/sr)
# For ANSI Z136.1, make plot 5in x 3.25 in
#
# Author: Brian J. Lund

set xrange [1.0e-13:1.0]
set yrange [0.01:1.0e+3]
set logscale xy

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"

set mxtics 5
set mytics 5
set xtics 1.0e-13, 10.0
set ytics 0.01, 10.0
set grid xtics ytics mxtics mytics
set grid linestyle 2, linestyle 3

set xlabel 'Exposure Duration (s)'
set ylabel 'Integrated Radiance (J/cm^2/sr)'

set format x '10^{%L}'
set format y '10^{%L}'

set label 1 '400 - 700 nm' at first 1.0e-8, first 6.0e-2 center front
set label 2 '1064 nm' at first 1.0e-8, first 0.6 center front
set label 3 '1315 nm' at first 1.0e-8, first 230.0 center front

plot 'figure10g.dat' notitle with lines linestyle 1

