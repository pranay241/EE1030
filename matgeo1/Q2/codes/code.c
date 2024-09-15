#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to create a matrix
double **createMat(int m, int n) {
    int i;
    double **a = (double **)malloc(m * sizeof(*a));
    for (i = 0; i < m; i++)
        a[i] = (double *)malloc(n * sizeof(*a[i]));
    return a;
}

// Function to free matrix
void freeMat(double **a, int m) {
    for (int i = 0; i < m; i++)
        free(a[i]);
    free(a);
}

// Function to print matrix
void printMat(double **p, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++)
            printf("%lf ", p[i][j]);
        printf("\n");
    }
}

// Function to calculate the coordinates of P
void computePoints(double QR, double length_diff, double *Px, double *Py) {
    // Coordinates of Q and R
    double Qx = 0, Qy = 0;
    double Rx = QR, Ry = 0;

    // Lengths of sides
    double PQ = length_diff + QR;  // Length of PQ
    double PR = length_diff;       // Length of PR

    // Coordinates of P using trigonometry
    double angle = M_PI / 4; // 45 degrees in radians

    *Px = (Rx + Qx + PR * cos(angle)) / 2.0;
    *Py = (Ry + Qy + PR * sin(angle)) / 2.0;
}

int main() {
    // Define the side length QR and the length difference
    double QR = 3.0; // 3 cm
    double length_diff = 6.0; // QP - PR = 6 cm

    // Variables for P coordinates
    double Px, Py;

    // Compute the coordinates for P
    computePoints(QR, length_diff, &Px, &Py);

    // Coordinates for Q and R
    double Qx = 0, Qy = 0;
    double Rx = QR, Ry = 0;

    // Write to file
    FILE *fptr = fopen("triangle_points.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fptr, "%lf,%lf\n", Px, Py); // P
    fprintf(fptr, "%lf,%lf\n", Qx, Qy); // Q
    fprintf(fptr, "%lf,%lf\n", Rx, Ry); // R

    fclose(fptr);

    return 0;
}

