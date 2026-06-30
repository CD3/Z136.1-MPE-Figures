# Fig10e_MPE.plt
# MPE for visible and near IR laser for sources subtending 50 mrad
# For ANSI Z136.1, make plot 5in x 3.25 in
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

set xlabel 'Exposure Duration (s)'
set ylabel 'Irradiance (W/cm^2)'

set format x '10^{%L}'
set format y ' 10^{%L}'

set label 1 '400 - 450 nm' at first 1.0e+4, first 1.4e-4 center front
set label 2 '475 nm' at first 1.0e+4, first 4.8e-4 center front
set label 3 '500 nm' at first 1.0e+4, first 1.4e-3 center front
set label 4 '532 nm' at first 1.0e+4, first 6.0e-3 center front
set label 5 '550 nm' at first 1.0e+4, first 1.4e-2 center front
set label 6 '400 - 700 nm Thermal' at first 1.0e+4, first 3.8e-2 center front
set label 7 '850 nm' at first 0.2, first 0.02 left front
set arrow 7 from first 0.36, first 0.027 to first 0.53, first 0.13 \
     linestyle 1
set label 8 '1064 nm' at first 1.0e+4, first 0.18 center front
set label 9 '1315 nm' at first 1.0e+4, first 0.4 center front
set label 10 '1400 nm' at first 0.2, first 30 left front
set arrow 10 from first 0.36, first 21.0 to first 0.2, first 3.1 linestyle 1


plot 'data.txt' notitle with lines linestyle 1, \

unset label 1
unset label 2
unset label 3
unset label 4
unset label 5
unset label 6
unset label 7
unset arrow 7
unset label 8
unset label 9
unset label 10
unset arrow 10
