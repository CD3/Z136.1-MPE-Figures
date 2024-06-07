# Make ANSI Z136.1 figure
# To make EPS files:  make TARGET=eps
# TO make PDF files:  make TARGET=pdf
#
# Default TARGET, if not supplied, is pdf
#
# Created: January 19, 2018
# Revised: November 28, 2023
# Author:  Brian J. Lund

MKDIR := mkdir -p
TARGET ?= pdf
SOURCE_DIR := src
BUILD_DIR := build
img_path := $(BUILD_DIR)/$(TARGET)

Figures = Fig3a   \
	  Fig3b  \
	  Fig4   \
	  Fig5   \
	  Fig6   \
	  Fig7   \
	  Fig8   \
	  Fig9   \
	  Fig10a \
	  Fig10b \
	  Fig10c \
	  Fig10d \
	  Fig10e \
	  Fig10f \
	  Fig10g \
	  Fig11  \
	  Fig12  \
	  Fig13

FIGS = $(addprefix $(SOURCE_DIR)/,$(Figures))

.PHONY: all $(FIGS)
all:  $(FIGS)

$(FIGS) :
	[[ -d $(img_path) ]] || $(MKDIR) $(img_path)
	$(MAKE) --directory=$@ img_path=$(img_path) TARGET=$(TARGET)

.PHONY: clean
clean: clean-eps clean-pdf

.PHONY: clean-eps
clean-eps:
	$(RM) $(BUILD_DIR)/eps/*.*

.PHONY: clean-pdf
clean-pdf:
	$(RM) $(BUILD_DIR)/pdf/*.*

