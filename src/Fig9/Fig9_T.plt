# Fig9_T.plt
# Time correction factors T1 and T2
# For ANSI Z136.1, make plot 6in x 2.5in
#
# Author: Brian J. Lund

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"

set multiplot layout 1,2

# T1
set xrange [450:500]
set yrange [0:100]

set xtics 400, 10
set ytics 0, 10
set grid xtics ytics
set grid linestyle 2, linestyle 3

set xlabel 'Wavelength (nm)'
set ylabel 'T_1 (s)'

set format x '{%.0f}'
set format y '{%.0f}'

plot 'T12.dat' index 0 notitle with lines linestyle 1

# T2
set xrange [0:110]
set yrange [0:110]

set xtics 0, 10
set ytics 0, 10

set xlabel 'Source Angular Subtense {/Symbol a} (mrad)'
set ylabel 'T_2 (s)'

plot 'T12.dat' index 1 notitle with lines linestyle 1

unset multiplot

