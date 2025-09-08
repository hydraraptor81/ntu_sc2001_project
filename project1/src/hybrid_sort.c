/* SC2001 Project 1 Integration of Mergesort & Insertion Sort
 * hybrid_sort.c
 * Authors: Aw Hwee Ren, Eamon Ching Yupeng, Ethan Jared Chong Rui Zhi
 * Date: 2025-09-06
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

int main (int argc, char *argv[]) {
	if (argc != 2) {
		fprintf(stderr, "Usage: mergesort arr_<size>.txt");
		return 1;
	}

	const char *input_filename = argv[1];
	char output_filename[24];
	snprintf(output_filename, sizeof(output_filename), "sorted_%s",
	input_filename);

	int *arr = NULL;				
	int size = parse_array(input_filename, &arr);

	if (size <= 0) {
		fprintf(stderr, "Failed to parse array from %s\n", input_filename);
		return 1;
	}

    comparisons = 0;
	struct timespec start, end;
	clock_gettime(CLOCK_MONOTONIC, &start);

	merge_sort(arr, 0, size - 1);
		
	clock_gettime(CLOCK_MONOTONIC, &end);

	double time_spent = (end.tv_sec - start.tv_sec) +
						(end.tv_nsec - start.tv_nsec) / 1e9;
	
	write_array(output_filename, arr, size);
	free(arr);
	printf("Sorted array written to %s\n", output_filename);
    printf("Time taken: %.9f seconds\n", time_spent);
    printf("Number of key comparisons: %lld\n", comparisons);
	
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

	int expected_size = 1000;

	if (sscanf(filename, "arr_%d.txt", &expected_size) != 1 || 
	expected_size <= 0) {
		fprintf(stderr, "Invalid filename format." 
		"Expected format: arr_<size>.txt\n");

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
