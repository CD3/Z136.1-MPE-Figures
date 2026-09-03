# Fig10d_MPE.plt
# MPE for visible and near IR laser for sources subtending 25 mrad
# For ANSI Z136.1, make plot 5in x 3.25in
#
# Author: Brian J. Lund

set xrange [0.1:1.0e+5]
set yrange [1.0e-5:100.0]
set logscale xy

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 2 linewidth 2 linecolor rgb "black"
set style line 3 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 4 linetype 1 linewidth 1 linecolor rgb "dark-gray"
set style line 5 linetype 5 linewidth 2 linecolor rgb "black"

set mytics 5
set mxtics 5
set xtics 0.1, 10.0
set ytics 1.0e-5, 10.0
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 3, linestyle 4

set xlabel 'Exposure Durations (s)'
set ylabel 'Irradiance (W/cm^2)'

set format x '10^{%L}'
set format y '10^{%L}'

set label 1 '400 - 450 nm' at first 3000.0, first 1.4e-4 center front
set label 2 '475 nm' at first 3000.0, first 4.4e-4 center front
set label 3 '500 nm' at first 3000.0, first 1.4e-3 center front
set label 4 '532 nm' at first 3000.0, first 7.0e-3 center front
set label 5 '400 - 700 nm Thermal' at first 3000.0, first 2.1e-2 center front
set label 6 '850 nm' at first 3000.0, first 4.4e-2 center front
set label 7 '1064 nm' at first 0.6, first 0.3 center front
set label 8 '1315 nm' at first 3000.0, first 0.4 center front
set label 9 '1400 nm' at first 3000, first 1.4e-1 center front
     
plot 'data.txt' notitle with lines linestyle 1, \

unset label 1
unset label 2
unset label 3
unset label 4
unset label 5
unset label 6
unset label 7
unset label 8
unset label 9

