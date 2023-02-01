#!usr/bin/env bash

file="README.md"
# target="Folder-Tree-Start"

target="Folder-Tree-Start"
while read -r line; do
    if (($target==$target)); then
        # tree | tail -n +2 1>> test.txt
        cat line <(tree)
        break
    fi
done <$file 



# 