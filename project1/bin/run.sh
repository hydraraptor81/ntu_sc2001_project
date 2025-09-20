#!/usr/bin/env bash

read -p "Enter max value in a set (e.g., 1000): " x
read -p "Enter the number of sets (e.g., 3): " num_sets

base_dir="../"
array_dir="$base_dir/arrays"
sorted_dir="$base_dir/sorted"

mkdir -p "$array_dir" "$sorted_dir"

./generate_arr "$x" "$num_sets" "$array_dir"
./mergesort "$num_sets" "$array_dir" "$sorted_dir"
./hybrid_sort "$num_sets" "$array_dir" "$sorted_dir"
