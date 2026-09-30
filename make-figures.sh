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

<!-- You can convert this file to a Word document or PDF using Pandoc -->
<!-- Note that the for PDF images, Pandoc will insert them as PDF which Word does _not_ support natively. -->

#
![Figure 3a. Limiting Cone Angle $\gamma$, Photochemical MPEs](Fig3a.${EXT})

#
![Figure 3b. Correction Factor Cg versus Limiting Cone Angle gamma, Used for Photochemical MPEs for T <= 100 s](Fig3b.${EXT})

#
![Figure 4. Point-Source MPEs for Visible and Near-Infrared Pulsed Sources (Wavelengths From 400 nm to 1400 nm)](Fig4.${EXT})

#
![Figure 5. MPE for Ultraviolet Radiation for Exposure Durations from 1e-9 s to 3e4 s for Ocular Exposure and 1e-9 s to 1e3 s for Skin Exposure](Fig5.${EXT})

#
![Figure 6. MPE for Ultraviolet, Wavelengths From 315 nm to 400 nm, and Infrared Wavelengths From 1400 nm to 1000 um, Laser Radiation for Single Pulses or Continuous Ocular or Skin Exposure, Small or Extended Sources, for 1e-9 s to 3e4 s](Fig6.${EXT})

#
![Figure 7. MPE for Ocular Exposure to Visible Laser Radiation, Wavelengths From 400 nm to 700 nm, for Single Pulses or Continuous Exposure, Small or Extended Sources](Fig7.${EXT})

#
![Figure 8. Correction Factors CA, CB, and CC Used to Determine the MPE for Ocular Exposure to Laser Radiation](Fig8.${EXT})

#
![Figure 9. Correction Times T1 and T2](Fig9.${EXT})

#
![Figure 10a. Ocular Point-Source MPE, alpha <= 1.5 mrad, for Visible and Near-Infrared Laser Radiation, Wavelengths From 400 nm to 1400 nm](Fig10a.${EXT})

#
![Figure 10b. Ocular Extended-Source MPE, alpha = 3 mrad, for Visible and Near-Infrared Laser Radiation, Wavelengths From 400 nm to 1400 nm](Fig10b.${EXT})

#
![Figure 10c. Ocular Extended-Source MPE, alpha = 11 mrad, for Visible and Near-Infrared Laser Radiation, Wavelengths From 400 nm to 1400 nm](Fig10c.${EXT})

#
![Figure 10d. Ocular Extended-Source MPE, alpha = 25 mrad, for Visible and Near-Infrared Laser Radiation, Wavelengths From 400 nm to 1400 nm](Fig10d.${EXT})

#
![Figure 10e. Ocular Extended-Source MPE, alpha = 50 mrad, for Visible and Near-Infrared Laser Radiation, Wavelengths From 400 nm to 1400 nm](Fig10e.${EXT})

#
![Figure 10f. Ocular Extended-Source MPE, alpha = 100 mrad, for Visible and Near-Infrared Laser Radiation, Wavelengths From 400 nm to 1400 nm](Fig10f.${EXT})

#
![Figure 10f. Ocular Extended-Source MPE, alpha = 100 mrad, for Visible and Near-Infrared Laser Radiation, Wavelengths From 400 nm to 1400 nm, for Pulsed or Continuous Exposures Less than 1 s](Fig10g.${EXT})

#
![Figure 11. MPE Reduction Factor, CP, for repetitive-Pulsed Lasers and Multiple Exposures From Scanning Lasers](Fig11.${EXT})

#
![Figure 12. Time dependence of alpha max](Fig12.${EXT})

#
![Figure 13. Correction factor, K lambda, Used to Determine the Corneal MPE for Wavelengths From 1200 nm to 1400 nm](Fig13.${EXT})

EOF


  cd "${HERE}"
done

printf "Done generating figures. All image files are in build/\n"
printf "To clean the project, just remove the build/ directory.\n"
printf "\n"
printf "You can generate a Word document with all figures inserted as images using Pandoc.\n"
printf "For example:\n"
printf "\n"
printf "$ cd build/pdf\n$ pandoc Figures.md -o Figures.docx\n"
printf "$ cd build/pdf\n$ pandoc Figures.md -o Figures.pdf\n"
printf "\n"

