/* SC2001 Project 1 Integration of Mergesort & Insertion Sort
 * generate_arr.c
 * Authors: Aw Hwee Ren, Eamon Ching Yupeng, Ethan Jared Chong Rui Zhi
 * Date: 2025-09-08
 * 
 * Generates arrays with values [1, X] of up to 10M integers in powers of 10
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

#ifdef _WIN32
#include <direct.h>
#define MKDIR(dir) _mkdir(dir)
#else
#include <sys/stat.h>
#define MKDIR(dir) mkdir(dir, 0700)
#endif

static unsigned long xorshift_state = 1;

void init_xorshift();
int xorshift_rand(int max);

int main(int argc, char *argv[]) {
    if (argc != 3) {
		fprintf(stderr, "Usage: %s <max_value> /path/to/output\n", argv[0]);
        return 1;
    }

    int max_value = atoi(argv[1]);
    if (max_value <= 0) {
        fprintf(stderr, "max_value must be a positive integer.\n");
        return 1;
    }

    const char *dir = argv[2];
    MKDIR(dir);  // On Windows use: _mkdir(dir)

	int sizes[] = {
    1000, 2500, 5000,
    10000, 25000, 50000,
    100000, 250000, 500000,
    1000000, 2500000, 5000000,
    10000000
	};
    
	int num_sizes = sizeof(sizes) / sizeof(sizes[0]);
	int num_sets = 30;
    
	init_xorshift();

	for (int i = 0; i < num_sizes; i++) {
    	int size = sizes[i];
	    for (int set = 1; set <= num_sets; set++) {
  	     	char filename[256];
			snprintf(filename, sizeof(filename), "%s/%d_arr_%d.txt", dir, set, size);
	        FILE *file = fopen(filename, "w");
	        if (!file) {
	            perror("Failed to open file");
	            continue;
	        }

	        int buffer_size = size * 10;
	        setvbuf(file, NULL, _IOFBF, buffer_size);

    	    if (fprintf(file, "{ ") < 0) {
        		perror("Failed to write to file");
				fclose(file);
				continue;
        	}

        	for (int j = 0; j < size; j++) {
				int num = xorshift_rand(max_value);
	            fprintf(file, "%d", num);
       	    	if (j < size - 1) {
	                fprintf(file, ", ");
        	    }
    	    }

	        if (fprintf(file, " };\n") < 0) {
	            perror("Failed to write to file");
	       	   	fclose(file);
         	   continue;
        	}

        	fclose(file);
        	printf("Generated %s with values in [1, %d]\n", filename, max_value);
    	}
	}

    return 0;
}	

void init_xorshift() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    xorshift_state = tv.tv_sec * 1000000 + tv.tv_usec;
    if (xorshift_state == 0) xorshift_state = 1;
}

int xorshift_rand(int max) {
    xorshift_state ^= xorshift_state << 13;
    xorshift_state ^= xorshift_state >> 17;
    xorshift_state ^= xorshift_state << 5;
    return (int)((xorshift_state % max) + 1);
}
