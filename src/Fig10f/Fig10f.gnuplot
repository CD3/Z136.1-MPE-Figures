# Fig11_MPE.plt
# MPE for visible and near IR laser for sources subtending alpha_max(t) mrad
# for exposure durations from 0.1 s to 3.0e+4 sec
# MPE expressed as radiance (W/cm^2/sr)
# For ANSI Z136.1, make plot 5in x 3.25 in
#
# Author: Brian J. Lund

set xrange [0.1:1.0e+5]
set yrange [1.0e-3:1.0e+4]
set logscale xy

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 2 linewidth 2 linecolor rgb "black"
set style line 3 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 4 linetype 1 linewidth 1 linecolor rgb "dark-gray"
set style line 5 linetype 5 linewidth 2 linecolor rgb "black"

set mytics 5
set mxtics 5
set xtics 0.1, 10.0
set ytics 1.0e-3, 10.0
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 3, linestyle 4

set xlabel 'Exposure Duration (s)'
set ylabel 'Radiance (W/cm^2/sr)'

set format x '10^{%L}'
set format y '10^{%L}'

set label 1 '400 - 450 nm' at first 3.0e+4, first 1.4e-2 center front
set label 2 '475 nm' at first 3.0e+4, first 5.2e-2 center front
set label 3 '500 nm' at first 3.0e+4, first 1.4e-1 center front
set label 4 '532 nm' at first 3.0e+4, first 6.4e-1 center front
set label 5 '550 nm' at first 3.0e+4, first 1.6 center front
set label 7 '850 nm' at first 3.0e+4, first 14.0 center front
set label 8 '1064 nm' at first 3.0e+4, first 40.0 center front
set label 11 '400 - 700 nm - Thermal' at first 2.0e+4, first 7.0 center front

#plot 'data-therm.txt' index 0:2 notitle with lines linestyle 1, \
#     'data-cornea.txt' index 0:1 notitle with lines linestyle 5, \
#     'data-photo.txt' index 0:4 notitle with lines linestyle 2


plot 'data.txt' notitle with lines linestyle 1, \
