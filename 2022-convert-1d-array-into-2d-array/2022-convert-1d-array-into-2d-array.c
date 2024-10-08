/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */ 
#include <stdlib.h>

int** construct2DArray(int* original, int originalSize, int m, int n, int* returnSize, int** returnColumnSizes) {
    // Check if the construction is possible
    if (originalSize != m * n) {
        *returnSize = 0; 
        return NULL; 
    }

    // Allocate memory for the 2D array and column sizes
    int** result = (int**)malloc(m * sizeof(int*));
    *returnColumnSizes = (int*)malloc(m * sizeof(int));
    
    for (int i = 0; i < m; i++) {
        result[i] = original + i * n; // Point to the correct segment of original
        (*returnColumnSizes)[i] = n;   // Set column size for each row
    }

    *returnSize = m; // Set return size
    return result;   // Return the constructed 2D array
}