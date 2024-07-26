#!/bin/env sh
filename="$(ls *.md)"
ls $filename | entr pandoc $filename -o ${filename%.*}.pdf --toc --toc-depth=3
