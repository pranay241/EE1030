#include <stdio.h>
#include <stdlib.h>
#include<math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

// Function to calculate y for the first equation: 3/x + 8/y = -1
double calculate_y1(double x) {
    if (x == 0) {
        return 0; // Avoid division by zero
    }
    return 8 / (-1 - (3 / x));
}

// Function to calculate y for the second equation: 1/x - 2/y = 2
double calculate_y2(double x) {
    if (x == 0) {
        return 0; // Avoid division by zero
    }
    return 2 / (1/x - 2);
}

// Function to plot points to a file
void plotPointsToFile(const char *filename, double **points, int num_points) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Unable to open file");
        return;
    }

    for (int i = 0; i < num_points; ++i) {
        fprintf(file, "%lf %lf\n", points[i][0], points[i][1]);
    }

    fclose(file);
}

int main() {
    double x_start = -10.0, x_end = 10.0, step = 0.1;
    int num_points = (int)((x_end - x_start) / step) + 1;
    double **points1 = createMat(num_points, 2);
    double **points2 = createMat(num_points, 2);
    
    if (points1 == NULL || points2 == NULL) {
        printf("Error: Unable to allocate memory for points.\n");
        return 1;
    }

    int index = 0;

    for (double x = x_start; x <= x_end; x += step) {
        if (x == 0) continue; // Skip x = 0 to avoid division by zero

        double y1 = calculate_y1(x);
        double y2 = calculate_y2(x);

        // Store the points for the first equation
        if (index < num_points) {
            points1[index][0] = x;
            points1[index][1] = y1;

            // Store the points for the second equation
            points2[index][0] = x;
            points2[index][1] = y2;

            index++;
        } else {
            printf("Warning: Index exceeds number of points.\n");
            break;
        }
    }

    // Plot points to a file for the first and second equations
    plotPointsToFile("plot1.txt", points1, num_points);
    plotPointsToFile("plot2.txt", points2, num_points);

    // Free allocated memory
    freeMat(points1, num_points);
    freeMat(points2, num_points);

    return 0;
}

