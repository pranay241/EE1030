#include <stdio.h>
#include <stdlib.h>

// Function to calculate the midpoint of a line segment BC
void midpoint(double x1, double y1, double x2, double y2, double *x_mid, double *y_mid) {
    *x_mid = (x1 + x2) / 2.0;
    *y_mid = (y1 + y2) / 2.0;
}

