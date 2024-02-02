#! /bin/bash
for i in {3..9}; do 
	echo $i
	cp 000_stage0.md ${i}${i}${i}_stage${i}.md
done
