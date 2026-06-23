#! /bin/bash

# Install missing dependencies for the figure build script.

set -u -e

# check for the tools we need
GNUPLOT=$(which gnuplot)
PYTHON=$(which python || which python3)
AWK=$(which gawk || which awk)
SED=$(which sed)

if [ -z "${GNUPLOT}" ]
then
  printf "Installing gnuplot with apt"
  sudo apt install gnuplot
fi

if [ -z "${PYTHON}" ]
then
  printf "Installing python with apt"
  sudo apt install python3
fi

if [ -z "${AWK}" ]
then
  printf "Installing gawk with apt"
  sudo apt install gawk
fi

if [ -z "${SED}" ]
then
  printf "Installing sed with apt"
  sudo apt install sed
fi

GNUPLOT=$(which gnuplot)
PYTHON=$(which python || which python3)
AWK=$(which gawk || which awk)
SED=$(which sed)


