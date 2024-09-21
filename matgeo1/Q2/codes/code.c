#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"  // Including math functions for matrix operations
#include "libs/geofun.h"   // Including geometry functions for vector operations

// Function to calculate the coordinates of points P, Q, and R
void calculateTriangle(double QR, double QP_minus_PR, double angle, double **Q, double **R, double **P) {
    // Set coordinates of points Q and R
    Q[0][0] = 0;  // x-coordinate of Q
    Q[1][0] = 0;  // y-coordinate of Q
    R[0][0] = QR; // x-coordinate of R (QR = 3 cm)
    R[1][0] = 0;  // y-coordinate of R

    // Calculate angle in radians
    double rad = angle * (M_PI / 180.0);

    // Calculate length of PR
    double PR = QP_minus_PR + 3; // Since QP - PR = 6 => QP = PR + 6

    // Using trigonometric functions to find point P
    P[0][0] = Q[0][0] + PR * cos(rad); // x-coordinate of P
    P[1][0] = Q[1][0] + PR * sin(rad); // y-coordinate of P
}

// Main function
int main() {
    double QR = 3;            // Length of QR
    double QP_minus_PR = 6;  // QP - PR
    double angle = 45;        // Angle PQR

    // Create matrices for points Q, R, and P
    double **Q = createMat(2, 1);
    double **R = createMat(2, 1);
    double **P = createMat(2, 1);

    // Calculate coordinates of points
    calculateTriangle(QR, QP_minus_PR, angle, Q, R, P);

    // Output points to a file
    FILE *fptr = fopen("triangle_PQR.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fptr, "Point Q: (%lf, %lf)\n", Q[0][0], Q[1][0]);
    fprintf(fptr, "Point R: (%lf, %lf)\n", R[0][0], R[1][0]);
    fprintf(fptr, "Point P: (%lf, %lf)\n", P[0][0], P[1][0]);

    fclose(fptr);

    // Free allocated memory
    freeMat(Q, 2);
    freeMat(R, 2);
    freeMat(P, 2);

    return 0;
}

