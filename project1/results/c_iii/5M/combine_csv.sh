#!/usr/bin/env bash

results_dir="/home/hr/Desktop/NTU/Y2S1/SC2001/Projects/ntu_sc2001_project/project1/results"
output_file="$results_dir/c_iii/combined_5M_hybridsort.csv"

echo "S,Size,AvgTime,AvgComparisons" > "$output_file"

for S in $(seq 2 150); do
    file="$results_dir/c_iii/5M/c_iii_S${S}_hybridsort.csv"
    if [[ -f "$file" ]]; then
        tail -n +2 "$file" | sed "s/^/$S,/" >> "$output_file"
    fi
done

echo "Combined CSV saved to $output_file"

