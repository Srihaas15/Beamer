import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./libcalculate_p.so')
lib.calculate_p.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double * 10)]

p = ctypes.c_double(0.0)

points_array_type = ctypes.c_double * 10 

points = points_array_type()
lib.calculate_p(ctypes.byref(p), points)

points_list = np.array([[points[i * 2], points[i * 2 + 1]] for i in range(5)])
original_points = np.array([[2, 1], [p.value, -1], [-1, 3]])

plt.figure(figsize=(8, 6))
plt.plot([2, -1], [1, 3], label='Line from (-1, 3) to (2, 1)', color='blue', marker='o')
plt.plot([2, p.value], [1, -1], label='Line from (2, 1) to (p, -1)', color='green', marker='o')

plt.scatter(original_points[:, 0], original_points[:, 1], color='red')

plt.annotate('(-1, 3)', xy=(-1, 3), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate('(2, 1)', xy=(2, 1), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate(f'({p.value:.2f}, -1)', xy=(p.value, -1), textcoords="offset points", xytext=(0,10), ha='center')

plt.xlim(-2, 5)
plt.ylim(-2, 4)

plt.title('Collinear Points and Intermediate Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', linewidth=0.5, ls='-')
plt.axvline(0, color='black', linewidth=0.5, ls='-')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig('../figs/fig.png')
plt.show()


