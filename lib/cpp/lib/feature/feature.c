#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

void synthesize_matrix(int row, int col, const unsigned char mat_in[row][col], float mat_out[row][col]){ 

    omp_set_num_threads(2);
    #pragma omp parallel default(none) shared(mat_out) firstprivate(row, col, mat_in) 
    {   
        int mid = row*col/2;
        float factor = 1.5;

        #pragma omp for collapse(2)
        for (int ii = 0; ii < row; ii++){
            for (int jj = 0; jj < col; jj++) {
                mat_out[ii][jj] = (mat_in[ii][jj] - mid)*factor;
                if (mat_out[ii][jj] < 0){ 
                    mat_out[ii][jj] += 0.25;
                } else {
                    mat_out[ii][jj] -= 0.25;
                }
            }  
        }
    }
} 
