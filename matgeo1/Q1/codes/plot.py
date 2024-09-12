import ctypes
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./generate.so')

lib.section.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
lib.section.restype = None

A = (4, 2)
B = (6, 5)
C = (1, 4)

x_div = ctypes.c_double()
y_div = ctypes.c_double()
lib.section(B[0], B[1], C[0], C[1], 1, ctypes.byref(x_div), ctypes.byref(y_div))

D = (x_div.value, y_div.value)

fig, ax = plt.subplots()
ax.plot([A[0], B[0]], [A[1], B[1]], 'k-')
ax.plot([B[0], C[0]], [B[1], C[1]], 'k-')
ax.plot([C[0], A[0]], [C[1], A[1]], 'k-')
ax.plot([A[0], D[0]], [A[1], D[1]], 'b--')

ax.scatter(*A, color='red', zorder=5)
ax.scatter(*B, color='green', zorder=5)
ax.scatter(*C, color='blue', zorder=5)
ax.scatter(*D, color='purple', zorder=5)

ax.text(*A, 'A (4, 2)', color='red', fontsize=12, verticalalignment='bottom')
ax.text(*B, 'B (6, 5)', color='green', fontsize=12, verticalalignment='bottom')
ax.text(*C, 'C (1, 4)', color='blue', fontsize=12, verticalalignment='top')
ax.text(*D, f'D ({D[0]}, {D[1]})', color='purple', fontsize=12, verticalalignment='bottom')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Triangle ABC with Median AD')

ax.set_aspect('equal', 'box')
ax.grid(True)

plt.savefig('triangle_plot.png')
plt.show()

