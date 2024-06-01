import numpy as np
import matplotlib.pyplot as plt

#  y^2 = x^3 + 3x + 1 (mod 1777)
modulus = 1777


x_values = np.arange(modulus)
y_values = []

for x in x_values:
    rhs = (x**3 + 3*x + 1) % modulus
    for y in range(modulus):
        if (y**2) % modulus == rhs:
            y_values.append((x, y))


x_coords, y_coords = zip(*y_values)


plt.figure(figsize=(12, 8))
plt.scatter(x_coords, y_coords, s=1, color='blue')
plt.title("Elliptic Curve $y^2 = x^3 + 3x + 1$ (mod 1777)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
