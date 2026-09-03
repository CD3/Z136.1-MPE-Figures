# Fig11.plt
# Plot of correction factor for multiple-pulse exposures
# For ANSI Z136.1, make plot 4in x 3in
#
# Author: Brian J. Lund

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"
set style line 10 linetype 1 linewidth 1 linecolor rgb "#d0d0d0"
set style line 11 linetype 1 linewidth 1 linecolor rgb "#f0f0f0"

set xrange [1.0:1.0e+6]
set yrange [0.09:1.1]
set logscale xy

set format x '10^{%L}'
set format y '{%.1f}'

set mxtics 10
set mytics 10
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 10,linestyle 11

set xlabel 'Number of Pulses'
set ylabel '{/=12 C_p}'

set label 1 '{/Symbol a \243} 5 mrad, {/Symbol a \263} 100 mrad' \
              at first 3.0e4, first 0.9 center
set label 2 '5 mrad < {/Symbol a \243 a}_{max}' \
             at first 3.0e4, first 0.35 center
#set label 3 '{/=16 {/Symbol a} > {/Symbol a}_{max}}' \
#             at first 3.0e4, first 0.18 center
set label 3 '{/Symbol a}_{max} < {/Symbol a} {/Symbol \243} 100 mrad' \
             at first 3.0e4, first 0.18 center

# plot fcp(x) = x**-0.25, fcp(x) notitle with lines linestyle 1
plot 'data-1.txt' notitle with lines linestyle 1, \
     'data-2.txt' notitle with lines linestyle 1, \
     'data-3.txt' notitle with lines linestyle 1

unset label 1
unset label 2
unset label 3

