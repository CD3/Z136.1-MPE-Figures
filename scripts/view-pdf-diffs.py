import itertools
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

DIFF_CMD = ["diff", "-q"]

VISUAL_DIFF_CMD = None
if shutil.which("diffpdf"):
    VISUAL_DIFF_CMD = ["diffpdf"]
if shutil.which("diff-pdf"):  # prefer diff-pdf if it exists
    VISUAL_DIFF_CMD = ["diff-pdf", "--view"]

if VISUAL_DIFF_CMD is None:
    print(
        "Could not find a visual diff tool. Install `diff-pdf` or `diffpdf`.",
        file=sys.stderr,
    )
    exit(1)


def usage():
    print(
        textwrap.dedent(
            f"""
        {sys.argv[0]} DIR1 DIR2

        Show differences (visually) between two directories containing PDF files.
        This script will loop through all PDFs in each directory and run a diff
        tool on any files with the same name.
        """
        )
    )


if len(sys.argv) < 3:
    usage()
    exit(1)

DIR1 = Path(sys.argv[1])
DIR2 = Path(sys.argv[2])

for D in [DIR1, DIR2]:
    if not D.is_dir():
        print(f"'{D}' is not a directory", file=sys.stderr)
        exit(2)


PDF_FILES = set(
    map(lambda p: p.name, itertools.chain(DIR1.glob("*.pdf"), DIR2.glob("*.pdf")))
)

FILES_ONLY_IN_DIR1 = []
FILES_ONLY_IN_DIR2 = []
FILES_WITH_NO_DIFF = []
FILES_WITH_DIFF = []

for PDF_FILE in PDF_FILES:
    PDF_FILE_1 = DIR1 / PDF_FILE
    PDF_FILE_2 = DIR2 / PDF_FILE
    if PDF_FILE_1.is_file() and not PDF_FILE_2.is_file():
        FILES_ONLY_IN_DIR1.append(PDF_FILE)
    if not PDF_FILE_1.is_file() and PDF_FILE_2.is_file():
        FILES_ONLY_IN_DIR2.append(PDF_FILE)

    try:
        subprocess.check_call(DIFF_CMD + [PDF_FILE_1, PDF_FILE_2])
        FILES_WITH_NO_DIFF.append(PDF_FILE)
    except:
        FILES_WITH_DIFF.append(PDF_FILE)
        try:
            CMD = VISUAL_DIFF_CMD + [PDF_FILE_1, PDF_FILE_2]
            res = subprocess.check_call(CMD)
        except Exception as e:
            print(f"There was a problem running visual PDF diff tool", file=sys.stderr)
            print(f"Tried to run '{' '.join(map(str, CMD))}'", file=sys.stderr)
            print(f"ERROR: {e}")
