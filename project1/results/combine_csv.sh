#!/usr/bin/env bash

results_dir="../results"
output_file="$results_dir/combined_c_ii_hybridsort.csv"

echo "S,Size,AvgTime,AvgComparisons" > "$output_file"

for S in $(seq 2 150); do
    file="$results_dir/c_ii_S${S}_hybridsort.csv"
    if [[ -f "$file" ]]; then
        tail -n +2 "$file" | sed "s/^/$S,/" >> "$output_file"
    fi
done

echo "Combined CSV saved to $output_file"

