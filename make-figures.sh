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

set -e -u

# setup tools we need
source scripts/provision-deps.sh

function usage {
cat << EOF
Usage: $0 [-h] [-g path/to/gnuplot] [extension1 [extention2 [...]]]

Make Z136.1 figures by running the gnuplot scripts.

This script basically just cd's into each figure directory, runs
the make-data.py script and then runs the gnuplot script for each of
the filetypes given as an argument.

Example

$ bash $0 pdf eps png

Will generate pdf, eps, and png images for each figure in the build/ directory.

Options:

  -h             Print this help.
  -g PATH        Specify the path to the gnuplot executable you want to use.
                 Useful for specifying a specific version of gnuplot.
  -p PATTERN     Give a pattern to match gnuplot scripts agains. This is used
                 to limit the scripts that are run and is handy for development.


EOF
}

PATTERN="*"
while getopts "g:hp:" opt
do
  case "${opt}" in
    g)
      GNUPLOT=$(readlink -f "${OPTARG}")
      ;;
    p)
      PATTERN="${OPTARG}"
      ;;
    h)
      usage
      exit 0
      ;;
    \?)
      usage
      exit 1
      ;;


  esac
done
shift $((OPTIND-1))



EXTENSIONS="${*}"
if [ -z "${EXTENSIONS}" ]
then
  EXTENSIONS="png ps"
fi

printf "Generating Z136.1 Figures\n\n"
printf "   Gnuplot: %b\n" "$GNUPLOT"
printf "    Python: %b\n" "$PYTHON"
printf "Extensions: %b\n" "$EXTENSIONS"
printf "   Pattern: %b\n" "$PATTERN"
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
for FILE in */*/${PATTERN}.gnuplot
do
  printf "\n\nGnuplot file: %b" "${FILE}"
  cd $(dirname ${FILE})
  INPUT=$(basename ${FILE})
  for EXT in ${EXTENSIONS}
  do
    OUTPUT="../../build/${EXT}/${INPUT/%.gnuplot/.${EXT}}"
    mkdir -p $(dirname ${OUTPUT})
    printf "${INPUT} -> ${OUTPUT}\n"
    source env.sh
    "${PYTHON}" make-data.py
    "${GNUPLOT}" \
      -e "set output '${OUTPUT}'" \
      -e "$(make_gnuplot_term_command_for_extension ${EXT})" \
      $(basename ${FILE})
  done
  cd "${HERE}"
done

for EXT in ${EXTENSIONS}
do
  cd "build/${EXT}"
cat > "Figures.md" << EOF
---
title: Z136.1 MPE Figures
---

<!-- You can convert this file to a Word document using Pandoc -->
EOF
  ls *.${EXT} | sort -V | sed "s/^/![](/;s/$/)\n/" >> Figures.md

  cd "${HERE}"
done

printf "Done generating figures. All image files are in build/\n"
printf "To clean the project, just remove the build/ directory.\n"
printf "\n"
printf "You can generate a Word document with all figures inserted as images using Pandoc.\n"
printf "For example:\n"
printf "\n"
printf "$ cd build/pdf\n$ pandoc Figures.md -o Figures.docx\n"
printf "\n"

