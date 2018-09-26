#!/usr/bin/env

# Author: Daniel Diamont

# Take pdfs in a directory and create .txt files from them

SRC=$PWD/"pdf_downloads/*.pdf"

for filename in $SRC
do
    echo "Processing" $filename
    #pdftotext $filename $DEST/$(basename ${filename%.*}).txt
    pdftotext $filename
done 
