DIR1="${1}"
DIR2="${2}"

DIFFTOOL="diff-pdf --view"

function usage() {
  printf "Usage: $0 DIR1 DIR2\n"
}

if [ -z "${DIR2}" ]
then
  usage
  exit 1
fi

if [ ! -d "${DIR1}" ]
then
  printf "Could not find %b\n" "${DIR1}"
  exit 1
fi
if [ ! -d "${DIR2}" ]
then
  printf "Could not find %b\n" "${DIR2}"
  exit 1
fi


IFS=$"\n\t"
for FILE in "${DIR1}/"*.pdf
do
  if [ ! -e "${FILE}" ]
  then
    printf "'%b' is not a file.\n" "${FILE}"
    exit 1
  fi
  FILE=$(basename "${FILE}")
  
  printf "Checking %b\n" "${FILE}"
  eval "${DIFFTOOL} ${DIR1}/${FILE} ${DIR2}/${FILE}"
done
