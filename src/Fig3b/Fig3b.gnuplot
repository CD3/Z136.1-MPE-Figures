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
set style line 10 linetype 1 linewidth 1 linecolor rgb "#d0d0d0"
set style line 11 linetype 1 linewidth 1 linecolor rgb "#f0f0f0"

set mxtics 10 
set mytics 10
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 10,linestyle 11

set xlabel 'Limiting Cone Angle, {/Symbol g} (mrad)'
set ylabel 'C_g'

set format y '10^{%L}'

set label 1 '{/Symbol a \243} 11 mrad' at 11,1.15
set label 2 '{/Symbol a} = 25 mrad' at 11,6.3 rotate by -38.0
set label 3 '{/Symbol a} = 50 mrad' at 11,25 rotate by -38.0
set label 4 '{/Symbol a} = 75 mrad' at 11,55 rotate by -38.0
set label 5 '{/Symbol a} = 100 mrad' at 11,95 rotate by -38.0

plot 'data-1.txt' notitle with lines linestyle 1, \
     'data-2.txt' notitle with lines linestyle 1, \
     'data-3.txt' notitle with lines linestyle 1, \
     'data-4.txt' notitle with lines linestyle 1, \
     'data-5.txt' notitle with lines linestyle 1

