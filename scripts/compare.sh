set -u
rm -rf build*

GOLDEN_SNAPSHOT=${1:-"snapshots/2026-06-23-1/"}

if [ ! -d "${GOLDEN_SNAPSHOT}" ]
then
  printf "Golden snapshot directory '${GOLDEN_SNAPSHOT}' does not exist.\n"
  printf "This should be a directory containing EPS and PDF images of the figures to compare the output of the current scripts to.\n"
  exit 1
fi

printf "Running new bash script with eps and pdf arguments\n"
bash make-figures.sh eps pdf > /dev/null 2>&1


printf "Removing creation date and title lines from post script files.\n"
sed -i "/%%CreationDate/d;/%%Title/d;/\/CreationDate/d;/\/Title/d" build*/eps/*


printf "Running diff on two build directories\n"
diff -r build/eps "${GOLDEN_SNAPSHOT}/eps" && printf "EPS Images are IDENTICAL!\n"

DIFFPDF=$(which diff-pdf || which comparepdf || which diffpdf || echo "")
if [ -z "${DIFFPDF}" ]
then
  printf "Can't diff PDF files, could not find 'diff-pdf' or 'diffpdf'. You can install it with 'apt install diff-pdf-wx' or 'apt install diffpdf'.\n"
  exit 1
fi
DIFFPDF_OPTS=""
if [ $(basename ${DIFFPDF}) = "diffpdf" ]
then
  DIFFPDF_OPTS="-a"
fi
if [ $(basename ${DIFFPDF}) = "comparepdf" ]
then
  DIFFPDF_OPTS="-ca"
fi

DIFFERENCES=""
IFS=$'\n\t'
for LINE in $(diff -r build/pdf "${GOLDEN_SNAPSHOT}/pdf")
do
  # Binary files are different. Use a PDF diffing tool to make sure.
  FILE=$(echo ${LINE} | sed "s|Binary files.*pdf/||;s| .*||")

  "${DIFFPDF}" ${DIFFPDF_OPTS} build/pdf/${FILE} "${GOLDEN_SNAPSHOT}/pdf/${FILE}"
  if [ "$?" -ne 0 ]
  then
    DIFFERENCES="${DIFFERENCES}\n${LINE}"
  fi
done
if [ -n "${DIFFERENCES}" ]
then
  printf "${DIFFERENCES}\n"
  printf "You can use 'diffpdf -a file1.pdf file2.pdf' or 'diff-pdf --view file1.pdf file2.pdf' to see the differences.\n"
else
  printf "PDF Images are IDENTICAL! (or at least appear to be)\n"
fi

