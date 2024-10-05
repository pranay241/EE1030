import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file
points = np.loadtxt("triangle_points.txt", delimiter=',')

# Ensure that there are at least three points
if points.shape[0] < 3:
    raise ValueError("The file must contain at least three points.")

# Define A, B, C based on the loaded points
A, B, C = points[:3]

# Calculate the midpoint D of BC
D = (B + C) / 2

# Coordinates for plotting
x = np.array([A[0], B[0], C[0], D[0]])
y = np.array([A[1], B[1], C[1], D[1]])

# Plot the points and the line segments
plt.figure()

# Plot triangle ABC
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label='AB')
plt.plot([B[0], C[0]], [B[1], C[1]], 'b-', label='BC')
plt.plot([C[0], A[0]], [C[1], A[1]], 'b-', label='CA')

# Plot median AD
plt.plot([A[0], D[0]], [A[1], D[1]], 'g--', label='Median AD')

# Plot points A, B, C, and D
plt.scatter(x, y, color='blue')

# Annotate each point with coordinates
plt.text(A[0], A[1], f'A({A[0]:.1f},{A[1]:.1f})', fontsize=12, ha='right')
plt.text(B[0], B[1], f'B({B[0]:.1f},{B[1]:.1f})', fontsize=12, ha='right')
plt.text(C[0], C[1], f'C({C[0]:.1f},{C[1]:.1f})', fontsize=12, ha='right')
plt.text(D[0], D[1], f'D({D[0]:.1f},{D[1]:.1f})', fontsize=12, ha='right')

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Triangle ABC with Median AD")
plt.grid(True)
plt.legend()
plt.savefig('triangle_plot.png')
plt.show()

