# Fig6_UV_IR_MPE.plt
# Plot UV and IR MPE vs Exposure Duration for small sources
# For ANSI Z136.1, make plot 5in x 3.25in
#
# Author: Brian J. Lund

set xrange [1.0e-13:1.0e+5]
set yrange [1.0e-5:1.0e+4]
set logscale xy

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 2 linewidth 2 linecolor rgb "black" dashtype 4
set style line 3 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 4 linetype 1 linewidth 1 linecolor rgb "dark-gray"
set style line 5 linetype 1 linewidth 3 linecolor rgb "black"

set mytics 5
set mxtics 5
set xtics 1.0e-13, 10.0
set ytics 1.0e-5, 10.0
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 3, linestyle 4

set xlabel 'Exposure Duration (s)'
set ylabel 'Radiant Exposure (J/cm^2)'

set format x '10^{%L}'
set format y '10^{%L}'

set label 1 '315 - 400 nm' at first 2e-9, first 1e-3
set label 2 '> 2600 nm' at first 2e-9, first 1.5e-2
set label 3 '1800 - 2600 nm' at first 2e-9, first 1.5e-1
set label 4 '1500 - 1800 nm' at first 2e-9, first 1.5 
set label 5 'UV' at first 100, first 0.7
set label 6 'IR' at first 80, first 30
set label 7 '1400 - 1500 nm' at first 2e-9, first 0.5

#plot 'Fig6_IR_MPE_Data.dat' notitle with lines linestyle 1, \
#     'Fig6_UV_MPE_Data.dat' notitle with lines linestyle 2
plot 'Fig6_IR_MPE_Data.dat' index 0 notitle with lines linestyle 5, \
     '' index 1 notitle with lines linestyle 1, \
     '' index 2 notitle with lines linestyle 1, \
     '' index 3 notitle with lines linestyle 1, \
     'Fig6_UV_MPE_Data.dat' notitle with lines linestyle 2

unset label 1
unset label 2
unset label 3
unset label 4
unset label 5
unset label 6
unset label 7
