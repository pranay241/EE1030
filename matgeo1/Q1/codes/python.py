import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file
points = np.loadtxt("line_points.txt", delimiter=',')

# Ensure that there are at least three points
if points.shape[0] < 3:
    raise ValueError("The file must contain at least three points.")

# Define A, B, C based on the loaded points
A, B, C = points[:3]

# Coordinates for plotting
x = np.array([A[0], B[0], C[0]])
y = np.array([A[1], B[1], C[1]])

# Plot the points and the line segment BC
plt.figure()
plt.plot([B[0], C[0]], [B[1], C[1]], 'r-', label='BC')
plt.scatter(x, y, color='blue')

# Annotate each point
plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='right')
plt.text(C[0], C[1], 'C', fontsize=12, ha='right')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of points A, B, and C")
plt.grid(True)
plt.legend()
plt.savefig('triangle_plot.png')
plt.show()

