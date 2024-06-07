# Fig3b_Cg.plt
# Plot extended source correction factor C_g for photochemicl MPEs
# For ANSI Z136.1, make plot 4in x 3in
#
# Author: Brian J. Lund

set xrange [10:110]
set yrange [0.9:100.0]
set logscale xy

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"

set mxtics 10 
set mytics 10
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 2, linestyle 3

set xlabel 'Limiting Cone Angle, {/Symbol g} (mrad)'
set ylabel 'C_g'

set format y '10^{%L}'

set label 1 '{/Symbol a \243} 11 mrad' at 11,1.15
set label 2 '{/Symbol a} = 25 mrad' at 11,6.3 rotate by -38.0
set label 3 '{/Symbol a} = 50 mrad' at 11,25 rotate by -38.0
set label 4 '{/Symbol a} = 75 mrad' at 11,55 rotate by -38.0
set label 5 '{/Symbol a} = 100 mrad' at 11,95 rotate by -38.0

plot '-' notitle with lines linestyle 1, \
     '-' notitle with lines linestyle 1, \
     '-' notitle with lines linestyle 1, \
     '-' notitle with lines linestyle 1, \
     '-' notitle with lines linestyle 1
# C_g for photochemical MPEs
# alpha = 1.5 mrad to 11 mrad
# gamma (mrad)    C_g
11.0              1.0
110.0             1.0
e
# alpha = 25 mrad
11.0              5.17
25.0              1.0
110.0             1.0
e
# alpha = 50 mrad
11.0              20.66
50.0              1.0
110.0             1.0
e
# alpha = 75 mrad
11.0              46.49
75.0              1.0
110.0             1.0
e
# alpha = 100 mrad
11.0              82.64
100.0             1.0
110.0             1.0
e

