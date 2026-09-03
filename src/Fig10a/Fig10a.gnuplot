# Fig10a_MPE.plt
# Plot point source MPE for visible and near ir lasers
# For ANSI Z136.1, make plot 5in x 3.25in
#
# Author: Brian J. Lund

set xrange [0.1:1.0e+5]
set yrange [1.0e-5:10.0]
set logscale xy

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 2 linewidth 2 linecolor rgb "black"
set style line 3 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 4 linetype 1 linewidth 1 linecolor rgb "dark-gray"

set mytics 5
set mxtics 5
set xtics 0.1, 10.0
set ytics 1.0e-5, 10.0
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 3, linestyle 4

set xlabel 'Exposure Duration (s)'
set ylabel 'Irradiance (W/cm^2)'

set format x '10^{%L}'
set format y '10^{%L}'

set label 1 '500 - 700 nm' at first 1000.0, first 1.4e-3 center front
set label 2 '490 nm' at first 1000.0, first 8.2e-4 center front
set label 3 '475 nm' at first 1000.0, first 4.5e-4 center front
set label 4 '400 - 450 nm' at first 1000.0, first 1.4e-4 center front
set label 5 '850 nm' at first 1000.0, first 2.8e-3 center front
set label 6 '1064 nm' at first 1000.0, first 7.6e-3 center front
set label 7 '1315 nm' at first 1000, first 0.4 center front
set label 8 '1400 nm' at first 1000, first 0.15 center front

plot 'data.txt' every :::0::7 notitle with lines linestyle 1

unset label 1
unset label 2
unset label 3
unset label 4
unset label 5
unset label 6
unset label 7
unset label 8
