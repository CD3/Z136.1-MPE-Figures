import itertools
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

DIFF_CMD = ["diff", "-q"]
APPEARANCE_DIFF_CMD = None
if shutil.which("diff-pdf"):
    APPEARANCE_DIFF_CMD = ["diff-pdf"]
# prefer comparepdf, diff-pdf run slow on sway
if shutil.which("comparepdf"):
    APPEARANCE_DIFF_CMD = ["comparepdf", "-ca"]

if APPEARANCE_DIFF_CMD is None:
    print(
        "Could not find a pdf diff tool to test if PDFs look different. Install `diff-pdf` or `comparepdf`.",
        file=sys.stderr,
    )
    exit(1)


def usage():
    print(
        textwrap.dedent(
            f"""
        {sys.argv[0]} PDF1 PDF2

        Test if two PDFS appear different and exit with return status indicating result.
        Exits with return code 0 if PDFs appear the same and 1 if not.
        Used by script to automate checking for PDF file differences.

        Two PDFs can be different but look the same.
        This script tries to test if the PDFs actually look different using one of a few
        different tool.
        """
        )
    )


if len(sys.argv) < 3:
    usage()
    sys.exit(1)

PDF_FILE_1 = Path(sys.argv[1])
PDF_FILE_2 = Path(sys.argv[2])

for F in [PDF_FILE_1, PDF_FILE_2]:
    if not F.is_file():
        print(f"'{F}' is not a file", file=sys.stderr)
        sys.exit(2)


try:
    subprocess.check_call(DIFF_CMD + [PDF_FILE_1, PDF_FILE_2])
except:
    # print(
    #     f"{PDF_FILE_1} and {PDF_FILE_2} are different. Checking if they appear different."
    # )
    try:
        CMD = APPEARANCE_DIFF_CMD + [PDF_FILE_1, PDF_FILE_2]
        subprocess.check_call(CMD)
    except Exception as e:
        sys.exit(1)
sys.exit(0)
