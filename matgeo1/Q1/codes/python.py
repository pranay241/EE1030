import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates for points A, B, and C
A = np.array([4, 2])
B = np.array([6, 5])
C = np.array([1, 4])

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

