#include <stdio.h>
#include <stdlib.h>

void section(double x1, double y1, double x2, double y2, int k, double *x_div, double *y_div) {
    *x_div = (k * x2 + x1) / (k + 1);
    *y_div = (k * y2 + y1) / (k + 1);
}

