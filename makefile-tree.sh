#!usr/bin/env bash

file="README.md"

while read -r line; do
    echo -e "$line\n"
done <$file 



echo "hello first line" 1> Documents/GitHub/Project_Journey/read.md && tree Documents/GitHub/Project_Journey/ | tail -n +2 1> Documents/GitHub/Project_Journey/read.md