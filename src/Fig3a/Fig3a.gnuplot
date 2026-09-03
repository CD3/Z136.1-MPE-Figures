# Fig3a_Cone_Angle.plt
# Plot the Limiting Cone Angle for photochemical MPEs
# For ANSI Z136.1, make plot 4in x 3in
#
# Author:  Brian J. Lund

set xrange [0.1:1e+5]
set yrange [1:1000]
set logscale xy

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"
set style line 10 linetype 1 linewidth 1 linecolor rgb "#d0d0d0"
set style line 11 linetype 1 linewidth 1 linecolor rgb "#f0f0f0"

set mytics 5
set mxtics 5
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 10,linestyle 11

set xlabel 'Exposure Duration (s)'
#set ylabel offset -1,0
set ylabel 'Limiting Cone Angel {/Symbol g} (mrad)'

set format x '10^{%L}'
set format y '10^{%L}'

plot 'data.txt' notitle with lines linestyle 1

