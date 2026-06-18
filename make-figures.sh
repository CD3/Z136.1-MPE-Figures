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
# 


function make_gnuplot_term_command_for_extension
{
  local EXT=$1
  if [ "$1" = "png" ]
  then
    # FIXME: need to get Helvetica font working....
    # and size
    # echo "set term png linewidth 1 dashlength 1 size 640,480" # font 'arial,20.0'"
    echo "set term png"
  fi
}

mkdir -p build
for FILE in */*/*.plt
do
  cd $(dirname ${FILE})
  INPUT=$(basename ${FILE})
  for EXT in png
  do
    OUTPUT="../../build/${EXT}/${INPUT/%plt/${EXT}}"
    mkdir -p $(dirname ${OUTPUT})
    printf "${INPUT} -> ${OUTPUT}\n"
    gnuplot \
      -e "set output '${OUTPUT}'" \
      -e "$(make_gnuplot_term_command_for_extension ${EXT})" \
      $(basename ${FILE})

    cd - > /dev/null
  done
done

printf "Done generating figures. All image files are in build/\n"
printf "To clean the project, just remove the build/ directory.\n"
