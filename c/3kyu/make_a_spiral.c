#include <stdlib.h>
#include <stdio.h>

//void spiralize (unsigned n, int spiral[n][n]) {
void spiralize (unsigned n, int** spiral) {
	unsigned cpt = 0;
	unsigned k = -1;
	unsigned l = 0;
	int stop = 0;
	while (!stop) {
		k++;
		l = cpt;
		while (k < n - cpt) {
			if (k > n || k < 0 || l < 0 || l > n || spiral[l][k] == 1 ) {
				stop = 1;
				break;
			}
			if (l + 1 < n && spiral[l + 1][k] == 1) {
				stop = 1;
				break;
			}
			spiral[l][k] = 1;
			k++;
		}
		k--;
		l++;
		while (l < n - cpt) {
			if (k > n || k < 0 || l < 0 || l > n || spiral[l][k] == 1 ) {
				stop = 1;
				break;
			}
			spiral[l][k] = 1;
			l++; 
		}
		l--;
		k--;
		while (k > cpt) {
			if (k > n || k < 0 || l < 0 || l > n || spiral[l][k] == 1 ) {
				stop = 1;
				break;
			}
			spiral[l][k] = 1;
			k--;
		}
		cpt += 2;
		while (l >= cpt) {
			if (k > n || k < 0 || l < 0 || l > n || spiral[l][k] == 1 ) {
				stop = 1;
				break;
			}
			spiral[l][k] = 1;
			l--;
		}
	}

	for (unsigned i = 0; i < n; i++) {
		for (unsigned j = 0; j < n; j++) {
			if (spiral[i][j] != 1)
				spiral[i][j] = 0;
		}
	}
}

// Print spiral
void print_spiral(unsigned len, int** spiral) {
	printf("n = %i\n", len);
	for (size_t i = 0; i < len; i++) {
		for (size_t j = 0; j < len; j++) {
			if (spiral[i][j] == 1)
				printf("%i", spiral[i][j]);
			else
				printf(".");
		}
		printf("\n");
	}
	printf("\n");
}

int main() {
	// Test spiralize
	for (unsigned i = 5; i < 9; i++) {
		// Allocate memory for i * i spiral
		int** spiral = (int**)malloc(i * sizeof(int*));
		for(size_t k = 0; k < i; k++) {
			int* arr = (int*)malloc(i * sizeof(int));
			spiral[k] = arr;
		}

		spiralize(i, spiral);

		print_spiral(i, spiral);

		// Free memory for each row
		for(size_t k = 0; k < i; k++) {
			free(spiral[k]);
		}
		// Free spiral
		free(spiral);
	}
	return 0;
}
