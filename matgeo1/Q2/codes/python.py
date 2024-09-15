import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file
points = np.loadtxt("triangle_points.txt", delimiter=',')

# Ensure that there are exactly three points
if points.shape[0] != 3:
    raise ValueError("The file must contain exactly three points.")

# Define P, Q, R based on the loaded points
P, Q, R = points

# Coordinates for plotting
x = np.array([P[0], Q[0], R[0], P[0]])
y = np.array([P[1], Q[1], R[1], P[1]])

# Plot the points and the line segments
plt.figure()

# Plot triangle PQR in red
plt.plot(x, y, 'r-', label='Triangle PQR')

# Plot points P, Q, and R in red
plt.scatter([P[0], Q[0], R[0]], [P[1], Q[1], R[1]], color='red')

# Annotate each point with coordinates
plt.text(P[0], P[1], f'P({P[0]:.1f},{P[1]:.1f})', fontsize=12, ha='right', color='red')
plt.text(Q[0], Q[1], f'Q({Q[0]:.1f},{Q[1]:.1f})', fontsize=12, ha='right', color='red')
plt.text(R[0], R[1], f'R({R[0]:.1f},{R[1]:.1f})', fontsize=12, ha='right', color='red')

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Triangle PQR")
plt.grid(True)
plt.legend()
plt.savefig('triangle_pqr_plot.png')
plt.show()

