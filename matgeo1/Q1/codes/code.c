#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

void point_gen(FILE *fptr, double **A, double **B, double **C, double **D, int num_points) {
    // Generate points for each side of the triangle
    for (int i = 0; i <= num_points; i++) {
        double temp = (double)i / (double)num_points;
        double temp1 = 1 - temp;

        // Points on AB
        double **AB = Matadd(Matscale(A, 2, 1, temp1), Matscale(B, 2, 1, temp), 2, 1);
        printf("%lf,%lf\n", AB[0][0], AB[1][0]);
        fprintf(fptr, "%lf,%lf\n", AB[0][0], AB[1][0]);
        freeMat(AB, 2);

        // Points on BC
        double **BC = Matadd(Matscale(B, 2, 1, temp1), Matscale(C, 2, 1, temp), 2, 1);
        printf("%lf,%lf\n", BC[0][0], BC[1][0]);
        fprintf(fptr, "%lf,%lf\n", BC[0][0], BC[1][0]);
        freeMat(BC, 2);

        // Points on CA
        double **CA = Matadd(Matscale(C, 2, 1, temp1), Matscale(A, 2, 1, temp), 2, 1);
        printf("%lf,%lf\n", CA[0][0], CA[1][0]);
        fprintf(fptr, "%lf,%lf\n", CA[0][0], CA[1][0]);
        freeMat(CA, 2);

        // Points on AD (median)
        double **AD = Matadd(Matscale(A, 2, 1, temp1), Matscale(D, 2, 1, temp), 2, 1);
        printf("%lf,%lf\n", AD[0][0], AD[1][0]);
        fprintf(fptr, "%lf,%lf\n", AD[0][0], AD[1][0]);
        freeMat(AD, 2);
    }
}

int main() {
    double x1, y1, x2, y2, x3, y3;
    x1 = 4; y1 = 2;
    x2 = 6; y2 = 5;
    x3 = 1; y3 = 4;

    // Define the vertices of the triangle
    int m = 2, n = 1;
    double **A = createMat(m, n);
    double **B = createMat(m, n);
    double **C = createMat(m, n);
    A[0][0] = x1;
    A[1][0] = y1;
    B[0][0] = x2;
    B[1][0] = y2;
    C[0][0] = x3;
    C[1][0] = y3;

    // Calculate the midpoint D of BC
    double **D = createMat(m, n);
    D[0][0] = (B[0][0] + C[0][0]) / 2;
    D[1][0] = (B[1][0] + C[1][0]) / 2;

    FILE *fptr;
    fptr = fopen("triangle_points.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Generate points along the triangle sides and median
    point_gen(fptr, A, B, C, D, 20);

    fclose(fptr);
    
    // Free allocated memory
    freeMat(A, 2);
    freeMat(B, 2);
    freeMat(C, 2);
    freeMat(D, 2);

    return 0;
}

