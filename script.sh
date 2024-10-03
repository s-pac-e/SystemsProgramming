# Branden Sauceda CAA934 #
mkdir big-directory
cd big-directory
mkdir small-directory
cd small-directory
touch file-1.txt
echo Branden > file-1.txt
seq 1 1 20 >> file-1.txt
wc -w < file-1.txt >> file-2.txt
cp file-1.txt ../
cd ..
mv file-1.txt file-3.txt
rm -rf small-directory/
ls -l
ls -a
cd .. 
rm -rf big-directory/