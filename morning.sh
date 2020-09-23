#/bin/bash

while read line; do
    chromium --new-tab "$line"
done < ./list.txt
