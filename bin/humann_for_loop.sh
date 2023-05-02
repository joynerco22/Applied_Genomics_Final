#!/bin/bash


files=$(ls ${1}_bins_dir)
echo "$files"
for MAG in $files; do humann -i ${1}_bins_dir/"${MAG}" -o "${MAG}"_results --threads 8 --search-mode uniref50 --metaphlan-options "--index mpa_vJan21_CHOCOPhlAnSGB_202103"; done
  
