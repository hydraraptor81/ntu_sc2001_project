#!/bin/bash
OPT_FLAGS="-Ofast -march=native -mtune=native -flto=auto -funroll-loops"
gcc $OPT_FLAGS hybrid_sort.c -o ../bin/hybrid_sort
gcc $OPT_FLAGS mergesort.c -o ../bin/mergesort
gcc $OPT_FLAGS generate_arr.c -o ../bin/generate_arr
