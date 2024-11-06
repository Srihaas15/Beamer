#include <stdio.h>
#include <stdlib.h>
#include "libs/matfun.h"
#include "libs/geofun.h"
void calculate_p(double *p, double points[5][2]) {
    double x1 = 2.0, y1 = 1.0;
    double x3 = -1.0, y3 = 3.0;
    double **matrix = createMat(3, 3);
    matrix[0][0] = x1; matrix[0][1] = y1; matrix[0][2] = 1.0; // Point (2, 1)
    matrix[1][0] = *p; matrix[1][1] = -1.0; matrix[1][2] = 1.0; // Point (p, -1)
    matrix[2][0] = x3; matrix[2][1] = y3; matrix[2][2] = 1.0; // Point (-1, 3)
    int rank = 3;
    for (int i = 0; i < 3; i++) {        
        if (matrix[i][0] == 0 && matrix[i][1] == 0 && matrix[i][2] == 0) {
            rank--;
            continue; 
        }
        for (int j = i + 1; j < 3; j++) {
            if (matrix[j][i] != 0) {
                double ratio = matrix[j][i] / matrix[i][i];
                for (int k = 0; k < 3; k++) {
                    matrix[j][k] -= ratio * matrix[i][k];
                }
            }
        }
    }
    if (rank < 3) {
        *p = (y3 - y1) / (x3 - x1) * (x3 - x1) + y1; 
    } else {
        *p = 5.0;
    }

    for (int i = 0; i < 5; i++) {
        double t = (double)i / 4; 
        points[i][0] = (1 - t) * x1 + t * x3; 
        points[i][1] = (1 - t) * y1 + t * y3; 
    }
    for (int i = 0; i < 3; i++) {
        free(matrix[i]);
    }
    free(matrix);
}



