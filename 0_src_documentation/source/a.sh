#! /bin/bash
for i in {0..9}; do 
	echo $i
	cat ${i}* > ${i}_agg.md
done
