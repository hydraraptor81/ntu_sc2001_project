#!/usr/bin/env bash

read -p "Enter max value in a set (e.g., 1000): " x
read -p "Enter the number of sets (e.g., 3): " num_sets
read -p "Enter S value (or press Enter for default 20): " S_value

if [ -z "$S_value" ]; then
    S_value=20
fi

if ! [[ "$S_value" =~ ^[0-9]+$ ]] || [ "$S_value" -lt 2 ]; then
    echo "Invalid S value. Must be an integer >= 2."
    exit 1
fi

base_dir="/home/hr/Desktop/NTU/Y2S1/SC2001/Projects/ntu_sc2001_project/project1"
array_dir="$base_dir/arrays"
sorted_dir="$base_dir/sorted"
results_dir="$base_dir/results/c_iii"

for (( S = 2; S <= S_value; S++ )); do
    echo "Running hybrid_sort with S = $S"
    ./hybrid_sort "$num_sets" "$array_dir" "$sorted_dir" "$S"

    # Move and rename output file
    mv hybridsort.csv "$results_dir/c_iii_S${S}_hybridsort.csv"
    echo "Results saved to $results_dir/c_iii_S${S}_hybridsort.csv"
done

