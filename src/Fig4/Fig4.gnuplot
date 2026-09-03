# Fig4_MPE.plt
# Plot point source MPE for Visible and Near IR Pulsed(?) Sources
# For ANSI Z136.1, make plot 5in x 3.25 in
#
# Author: Brian J. Lund

set xrange [1.0e-13:10.0]
set yrange [1.0e-8:10.0]
set logscale xy

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "#f0f0f0"
set style line 5 linetype 5 linewidth 2 linecolor rgb "black"

set mytics 5
set mxtics 5
set xtics 1.0e-13, 10.0
set ytics 1.0e-9, 10.0
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 3, linestyle 3

set xlabel 'Exposure Duration (s)'
set ylabel 'Radiant Exposure (J/cm^2)'

set format x '10^{%L}'
set format y '10^{%L}'

set label 1 '400 - 700 nm' at first 4e-7, first 1.1e-7 center front
set label 2 '850 nm' at first 4e-7, first 8.0e-7 center front
set label 3 '1064 nm' at first 4e-7, first 4.0e-6 center front
set label 4 '1315 nm' at first 4e-7, first 0.0002 center front
set label 5 '1390 nm' at first 4e-7, first 0.05 center front
set label 6 '1400 nm' at first 4e-7, first 0.3 center front

plot 'data.txt' every :::0::3 notitle with lines linestyle 1, \
     '' every :::5::5 notitle with lines linestyle 2, \
     '' every :::4::4 notitle with lines linestyle 1, \

unset label 1
unset label 2
unset label 3
unset label 4
unset label 5
unset label 6
