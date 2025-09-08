#!/bin/bash
gcc -Ofast -march=native -flto -funroll-loops -fomit-frame-pointer -ffast-math -DNDEBUG mergesort.c -o mergesort
gcc -Ofast -march=native -flto -funroll-loops -fomit-frame-pointer -ffast-math -DNDEBUG hybrid_sort.c -o hybrid_sort
gcc -Ofast -march=native -flto -funroll-loops -fomit-frame-pointer -ffast-math -DNDEBUG generate_arr.c -o generate_arr


