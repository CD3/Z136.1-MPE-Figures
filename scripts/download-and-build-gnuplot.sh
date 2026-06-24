VERSION=${1:-"6.0.2"}


mkdir -p build/gnuplot-${VERSION}
cd build/gnuplot-${VERSION}
wget https://sourceforge.net/projects/gnuplot/files/gnuplot/${VERSION}/gnuplot-${VERSION}.tar.gz/download
tar xf download
cd gnuplot-${VERSION}
./configure --with-qt=no \
            --with-cairo

make


