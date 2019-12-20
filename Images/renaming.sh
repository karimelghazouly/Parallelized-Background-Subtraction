#!/bin/sh
num=0
for file in *.jpg; do
      if [[ $file != "renaming.sh" ]]; then
         mv "$file" "$(printf "%u" $num).jpg"
         let num=$num+1
       fi
done
