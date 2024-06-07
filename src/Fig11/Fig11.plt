# Fig11.plt
# Plot of correction factor for multiple-pulse exposures
# For ANSI Z136.1, make plot 4in x 3in
#
# Author: Brian J. Lund

set style line 1 linetype 1 linewidth 2 linecolor rgb "black"
set style line 2 linetype 1 linewidth 2 linecolor rgb "dark-gray"
set style line 3 linetype 1 linewidth 1 linecolor rgb "dark-gray"

set xrange [1.0:1.0e+6]
set yrange [0.09:1.1]
set logscale xy

set format x '10^{%L}'
set format y '{%.1f}'

set mxtics 10
set mytics 10
set grid xtics ytics
set grid mxtics mytics
set grid linestyle 2, linestyle 3

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
plot '-' notitle with lines linestyle 1, \
     '-' notitle with lines linestyle 1, \
     '-' notitle with lines linestyle 1
# alpha < 5 mrad
1.0   1.0
1.0e+6 1.0 
e
# 5 mrad < alpha < alpha_max
1.0   1.0
40.0  0.4
1.0e+6 0.4
e
# alpha > alpha_max
1.0   1.0
625.0  0.2
1.0e+6 0.2
e

unset label 1
unset label 2
unset label 3

