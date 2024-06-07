# common.mk
# Common commands to making all Z136.1 plots
# Inidividual plot makefiles must include this file using the command
#    include common.mk
#
# Created:  19 January 2018
# Updated:  28 November 2023
# Authot:   Brian J. Lund

# set variables for output file type

ifeq ($(TARGET), pdf)
    term = pdfcairo
#    img_path = ../../pdf
    file_ext = pdf
    linewidth = 1
    dashlength = 1
else
    term = postscript eps
#    img_path = ../../eps
    file_ext = eps
    linewidth = 2
    dashlength = 2
endif

output_file = ../../$(img_path)/$(PLOTNAME).$(file_ext)

# The following variables should be set in the individual
# plot makefiles
SIZE ?= 4in,3in
FONT ?= Helvetica
FONTSIZE ?= 20
PLOTNAME ?= a
datafiles ?=

# commands to pass to gnuplot using the -e flag on the command line
term_cmd = "set term $(term) color linewidth $(linewidth) \
	   dashlength $(dashlength) size $(SIZE)"
font_cmd = "set termoption font '$(FONT),$(FONTSIZE)'"
output_cmd = "set output '$(output_file)'"

# command to call gnuplot and make the plots
$(output_file) : $(GNUPLOT_SCRIPT) $(datafiles)
	gnuplot \
	    -e $(term_cmd) \
	    -e $(font_cmd) \
	    -e $(output_cmd) \
	    $(GNUPLOT_SCRIPT)

