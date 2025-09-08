#!/bin/bash
gcc -Ofast -march=native -flto=auto -funroll-loops -fomit-frame-pointer \
    -fno-signed-zeros -fno-trapping-math -ffp-contract=fast \
    -DNDEBUG -fmerge-all-constants -finline-limit=1000 \
    -Wno-unused-result \
    hybrid_sort.c -o ../bin/hybrid_sort

gcc -Ofast -march=native -flto=auto -funroll-loops -fomit-frame-pointer \
    -fno-signed-zeros -fno-trapping-math -ffp-contract=fast \
    -DNDEBUG -fmerge-all-constants -finline-limit=1000 \
    -Wno-unused-result \
    mergesort.c -o ../bin/mergesort

gcc -Ofast -march=native -flto=auto -funroll-loops -fomit-frame-pointer \
    -fno-signed-zeros -fno-trapping-math -ffp-contract=fast \
    -DNDEBUG -fmerge-all-constants -finline-limit=1000 \
    -Wno-unused-result \
    generate_arr.c -o ../bin/generate_arr
