import numpy as np
import matplotlib.pyplot as plt

# Function to read points from the file
def read_triangle_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            # Parse the line to extract coordinates
            if 'Point' in line:
                coords = line.split(': ')[1].strip('() \n').split(',')
                # Clean the coordinates
                coords = [coord.strip() for coord in coords]
                points.append((float(coords[0]), float(coords[1])))
    return np.array(points)

# Function to calculate lengths of the triangle sides
def calculate_lengths(points):
    P, Q, R = points
    PQ = np.sqrt((P[0] - Q[0])**2 + (P[1] - Q[1])**2)  # Length of PQ
    QR = np.sqrt((Q[0] - R[0])**2 + (Q[1] - R[1])**2)  # Length of QR
    PR = np.sqrt((P[0] - R[0])**2 + (P[1] - R[1])**2)  # Length of PR
    return PQ, QR, PR

# Main plotting function
def plot_triangle(points):
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
    plt.plot(x, y, marker='o', label='Triangle PQR')
    
    # Annotate the points
    plt.text(P[0], P[1], f'P ({P[0]:.2f}, {P[1]:.2f})', fontsize=12, ha='right')
    plt.text(Q[0], Q[1], f'Q ({Q[0]:.2f}, {Q[1]:.2f})', fontsize=12, ha='right')
    plt.text(R[0], R[1], f'R ({R[0]:.2f}, {R[1]:.2f})', fontsize=12, ha='right')

    # Calculate lengths
    PQ, QR, PR = calculate_lengths(points)

    # Annotate lengths
    mid_QR = (Q + R) / 2
    mid_PR = (P + R) / 2
    mid_PQ = (P + Q) / 2
    
    plt.text(mid_QR[0], mid_QR[1], f'QR: {QR:.2f}', fontsize=10, ha='center', color='blue')
    plt.text(mid_PR[0], mid_PR[1], f'PR: {PR:.2f}', fontsize=10, ha='center', color='blue')
    plt.text(mid_PQ[0], mid_PQ[1], f'PQ: {PQ:.2f}', fontsize=10, ha='center', color='blue')

    # Set equal aspect ratio
    plt.axis('equal')
    plt.title('Triangle PQR')
    plt.grid(True)
    plt.xlabel('X-axis (cm)')
    plt.ylabel('Y-axis (cm)')
    plt.legend()
    plt.show()

# File path to the triangle points
file_path = 'triangle_PQR.txt'

# Read the points from the file
triangle_points = read_triangle_points(file_path)

# Plot the triangle and display lengths
plot_triangle(triangle_points)

