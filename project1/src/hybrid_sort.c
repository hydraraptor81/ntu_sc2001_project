/* SC2001 Project 1 Integration of Mergesort & Insertion Sort
 * hybrid_sort.c
 * Authors: Aw Hwee Ren, Eamon Ching Yupeng, Ethan Jared Chong Rui Zhi
 * Date: 2025-09-10
 * 
 * Implements mergesort and insertion sort as hybrid algorithm 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define S 20 // Threshold for switching to insertion sort
void merge(int arr[], int l, int m, int r);
void merge_sort(int arr[], int l, int r);
void insertion_sort(int arr[], int l, int r);
int parse_array(const char *filename, int **arr);
void write_array(const char *filename, int arr[], int size);

static long long comparisons = 0;

const int sizes[] = {
    1000, 2500, 5000,
    10000, 25000, 50000,
    100000, 250000, 500000,
    1000000, 2500000, 5000000,
    10000000};
const int num_sizes = sizeof(sizes) / sizeof(sizes[0]);
const int num_sets = 30;

int main (int argc, char *argv[]) {
	if (argc != 3) {
		fprintf(stderr, "Usage: %s /path/to/arrays /path/to/sorted\n", argv[0]);
		return 1;
	}

	const char *input_dir = argv[1];
	const char *output_dir = argv[2];

	FILE *csv_file = fopen("hybridsort.csv", "w");
	if (!csv_file) {
	   	perror("Failed to create hybridsort.csv");
	    return 1;
	}
	fprintf(csv_file, "Size,AvgTime,AvgComparisons\n");	
	
	for (int i = 0; i < num_sizes; i++) {
		int size = sizes[i];
		double total_time = 0;
		long long total_comparisons = 0;

		for (int set = 1; set <= num_sets; set++) {
			char input_file[256];
			snprintf(input_file, sizeof(input_file), "%s/%d_arr_%d.txt", input_dir,
			set, size);

			char output_file[256];
			snprintf(output_file, sizeof(output_file), "%s/sorted_%d_arr_%d.txt", output_dir,
			set, size);

			int *arr = NULL;					
			int arr_size = parse_array(input_file, &arr);
			
			if (arr_size <= 0) {
				fprintf(stderr, "Failed to parse %s\n", input_file);
				continue;
			}

    		comparisons = 0;
			struct timespec start, end;
			clock_gettime(CLOCK_MONOTONIC, &start);
	
			merge_sort(arr, 0, arr_size - 1);

			clock_gettime(CLOCK_MONOTONIC, &end);
			double time_spent = (end.tv_sec - start.tv_sec) +
            (end.tv_nsec - start.tv_nsec) / 1e9;	

			total_time += time_spent;
			total_comparisons += comparisons;

			write_array(output_file, arr, arr_size);
			free(arr);

		printf("Sorted array written to %s\n", output_file);
    	printf("Time taken: %.9f seconds\n", time_spent);
    	printf("Number of key comparisons: %lld\n", comparisons);
		}
		double avg_time = total_time / num_sets;
		long long avg_comparisons = total_comparisons / num_sets;
		fprintf(csv_file, "%d,%.9f,%lld\n", size, avg_time, avg_comparisons);
	}

	return 0;
}

void merge(int arr[], int l, int m, int r) {
	int i, j, k;
	int n1 = m - l + 1; 				// size of left subarray
	int n2 = r - m;						// size of right subarray

	int *L = malloc(n1 * sizeof(int));	// allocate left subarray
	int *R = malloc(n2 * sizeof(int));	// allocate right subarray

	for (i = 0; i < n1; i++)
		L[i] = arr[l + i];
	for (j = 0; j < n2; j++)
		R[j] = arr[m + 1 + j];

	i = 0;
	j = 0;
	k = l;

	while (i < n1 && j < n2) {			// loop until one subarray is empty
		comparisons++;
		if (L[i] <= R[j]) {
			arr[k] = L[i];
			++i;
		}
		else {
			arr[k] = R[j];
			j++;
		}
		k++;
	}

	while (i < n1) {					// loop until left subarray is empty
		arr[k] = L[i];
		i++;
		k++;
	}

	while (j < n2) {					// loop until right subarray is empty
		arr[k] = R[j];
		j++;
		k++;
	}

	free(L);							// free temp subarrays
	free(R);
}

void merge_sort(int arr[], int l, int r) {
	if (r - l + 1 <= S) {				// check if size of subarray = S
		insertion_sort(arr, l, r);		// call insertion sort 
	}
	else if (l < r) {
		int m = l + (r-l) / 2;			// calculate middle

		merge_sort(arr, l, m);			// mergesort left recursively
		merge_sort(arr, m + 1, r);		// mergesort right recursively

		merge(arr, l, m, r);
	}
}

void insertion_sort(int arr[], int l, int r) {
	for (int i = l + 1; i <= r; i++) {
		int key = arr[i];				// element to be inserted
		int j = i - 1;					// element to be compared against

		while (j >= l) {
			comparisons++;
			if (arr[j] > key) {			
				arr[j + 1] = arr[j]; 	// shift arr[j] to the right
				j--;
			}
			else
				break; 					// move on to next element as [i] > [j]
		}
		arr[j + 1] = key;				// insert key to correct position
	}
}
int parse_array(const char *filename, int **arr) {
	FILE *file = fopen(filename, "r");
	if (!file) {
		perror("Failed to open input file");
		return -1;
	}
	
	int set = 1;
	int expected_size = 1000;

	const char *basename = strrchr(filename, '/');
    basename++;

	if (sscanf(basename, "%d_arr_%d.txt", &set, &expected_size) != 2 || 
	expected_size <= 0) {
		fprintf(stderr, "Invalid filename format." 
		"Expected format: <set>_arr_<size>.txt\n");

		return 1;
	}
	
	*arr = malloc(expected_size * sizeof(int));
	if (!*arr) {
		fclose(file);
		fprintf(stderr, "Memory allocation failed\n");
		return -1;
	}

	fgetc(file);						// skip brace of array (first char)

	int index = 0;
	int num;
	while (fscanf(file, "%d", &num) == 1) {
		(*arr)[index++] = num;

		char ch;
		do {
			ch = fgetc(file);
		} while (ch != ',' && ch != '}' && ch != EOF);
		if (ch == '}')
			break;
	}

	fclose(file);

    if (index != expected_size) {
        fprintf(stderr, "Warning: Expected %d elements, but parsed %d\n", 
		expected_size, index);
    }

	return index;
}

void write_array(const char *filename, int arr[], int size) {
	FILE *file = fopen(filename, "w");
	if (!file) {
		perror("Failed to open output file");
		return;
	}

	fprintf(file, "{");
	for (int i = 0; i < size; i++) {
		fprintf(file, "%d", arr[i]);
		if (i < size - 1)
			fprintf(file, ", ");
	}
	fprintf(file, "};\n");

	fclose(file);
}
