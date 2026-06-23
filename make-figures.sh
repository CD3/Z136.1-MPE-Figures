#! /bin/bash

# Script to generate the ANSI Z136.1 figures
# 
# to run:
# $ bash make-figures.sh
#
# Gnuplot scripts were originally authored by
# Brian J. Lund on January 19, 2018. then revised
# by Brian J. Lund on November 28, 2023. Figures
# were generated with a set of makefiles.
# 
# CD Clark III received the scripts in 2024 to
# make changes for the 2027 version of the standard.
#

set -u -e

# setup tools we need
source scripts/provision-deps.sh


EXTENSIONS="${*}"
if [ -z "${EXTENSIONS}" ]
then
  EXTENSIONS="png ps"
fi

printf "Generating Z136.1 Figures\n\n"
printf "   Gnuplot: %b\n" "$GNUPLOT"
printf "    Python: %b\n" "$PYTHON"
printf "Extensions: %b\n" "$EXTENSIONS"
printf "\n"



function make_gnuplot_term_command_for_extension
{
  local EXT=$1
  if [ "$1" = "png" ]
  then
    # need to convert size in inches to pixels
    SIZE=$(echo ${SIZE} | "${SED}" "s/in//g" | "${AWK}" -F, '{print 96*$1","96*$2}' | "${SED}" "s/ /,/" )
    echo "set term png linewidth 1 dashlength 1 size ${SIZE} font '${FONT},${FONTSIZE}'"
  fi
  if [ "$1" = "ps" ]
  then
    echo "set term postscript linewidth 2 dashlength 2 size ${SIZE} font '${FONT},${FONTSIZE}'"
  fi
  if [ "$1" = "eps" ]
  then
    echo "set term postscript eps color linewidth 2 dashlength 2 size ${SIZE} font '${FONT},${FONTSIZE}'"
  fi
  if [ "$1" = "pdf" ]
  then
    echo "set term pdfcairo color linewidth 1 dashlength 1 size ${SIZE} font '${FONT},${FONTSIZE}'"
  fi
}

HERE=$PWD
mkdir -p build
for FILE in */*/*.gnuplot
do
  printf "\n\nGnuplot file: %b" "${FILE}"
  cd $(dirname ${FILE})
  INPUT=$(basename ${FILE})
  for EXT in ${EXTENSIONS}
  do
    OUTPUT="../../build/${EXT}/${INPUT/%[_.]*/.${EXT}}"
    mkdir -p $(dirname ${OUTPUT})
    printf "${INPUT} -> ${OUTPUT}\n"
    source env.sh
    "${PYTHON}" make-data.py
    gnuplot \
      -e "set output '${OUTPUT}'" \
      -e "$(make_gnuplot_term_command_for_extension ${EXT})" \
      $(basename ${FILE})
  done
  cd "${HERE}"
done

printf "Done generating figures. All image files are in build/\n"
printf "To clean the project, just remove the build/ directory.\n"
