#!/bin/sh

cd catatan_persediaan_banjarbaru
find . -type f -exec md5sum {} \; | sort > /tmp/file1_md5sum_sort
cd -
cd tmp/catatan_persediaan_banjarbaru
find . -type f -exec md5sum {} \; | grep -v Tag | sort > /tmp/file2_md5sum_sort
cd -
diff /tmp/file1_md5sum_sort /tmp/file2_md5sum_sort | grep -v CVS | grep "\.\/"
