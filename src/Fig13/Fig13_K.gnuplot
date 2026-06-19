# Fig13_K.plt
# Figure 13 for ANSI Z136.1 - Klambda
#   call '../meps.gp' "4in,3in" "'Fig13.eps'" "'Fig13_K.plt'"

set termoption font "Helvetica, 20"

set xrange [1195:1405]
set yrange [0.9:1.1e+2]
set logscale y

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"

set mxtics 5
set mytics 5
set xtics 1200, 50
set ytics 0.1, 10.0
set grid xtics ytics mxtics mytics
set grid linestyle 2, linestyle 3

set xlabel 'Wavelength (nm)'
set ylabel 'K_{/Symbol l}'

set format x '{/=16 {%.0f}}'
set format y '{/=16 10^{%L}}'

plot '-' notitle with lines linestyle 1
# Wavelength (nm)    Klambda
1200.0               100.0
1400.0                 1.0
e

reset

