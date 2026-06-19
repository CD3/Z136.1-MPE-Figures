rm -rf build*

printf "Running Lund makefile(s) with ps target\n"
make TARGET=ps > /dev/null 2>&1
mv build build-goldenimage
mv build-goldenimage/{ps,eps}

printf "Running new bash script with eps argument\n"
bash make-figures.sh eps > /dev/null 2>&1


printf "Removing creation date and title lines from post script files."
sed -i "/%%CreationDate/d;/%%Title/d;/\/CreationDate/d;/\/Title/d" build*/eps/*


printf "Running diff on two build directories\n"
diff -r build build-goldenimage && printf "Images are IDENTICAL!\n"
