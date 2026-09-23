import numpy as np
import matplotlib.pyplot as plt

# Define complex numbers from Exercice 18: (modulus r, argument theta in rad, LaTeX label)
complex_numbers = [
    (1, 2 * np.pi, r'$e^{2i\pi}$'),
    (1, np.pi, r'$e^{i\pi}$'),
    (1, -np.pi, r'$e^{-i\pi}$'),
    (1, np.pi / 3, r'$e^{i\frac{\pi}{3}}$'),
    (2, 2 * np.pi / 3, r'$2 e^{i\frac{2\pi}{3}}$'),
    (1, np.pi / 4, r'$e^{i\frac{\pi}{4}}$'),
    (np.sqrt(2), 3 * np.pi / 4, r'$\sqrt{2} e^{i\frac{3\pi}{4}}$'),
    (1, np.pi / 6, r'$e^{i\frac{\pi}{6}}$'),
    (4, 7 * np.pi / 6, r'$4 e^{i\frac{7\pi}{6}}$'),
]

fig, ax = plt.subplots(figsize=(8, 8))

# Draw reference circles for the distinct moduli present in the problem
moduli = {1, np.sqrt(2), 2, 4}
theta_circle = np.linspace(0, 2 * np.pi, 300)

for r in moduli:
    ax.plot(
        r * np.cos(theta_circle),
        r * np.sin(theta_circle),
        color='gray',
        linestyle='--',
        linewidth=0.8,
        alpha=0.6,
    )

# Plot each complex point, position vector, and text label
for r, theta, label in complex_numbers:
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Plot point
    ax.scatter(x, y, color='crimson', zorder=5, s=35)

    # Dotted radial line from origin to point
    ax.plot([0, x], [0, y], color='crimson', linestyle=':', alpha=0.5, zorder=3)

    # Offset for text labels
    offset_r = r + 0.35
    ax.text(
        offset_r * np.cos(theta),
        offset_r * np.sin(theta),
        label,
        fontsize=11,
        ha='center',
        va='center',
        zorder=6,
    )

# Center spines at origin
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Axis limits and labels
ax.set_xlim([-4.8, 4.8])
ax.set_ylim([-4.8, 4.8])
ax.set_xlabel(r'$\mathrm{Re}(z)$', loc='right')
ax.set_ylabel(r'$\mathrm{Im}(z)$', loc='top')

plt.grid(True, linestyle=':', alpha=0.4)
plt.title('Exercice 18: Representation in the Complex Plane', pad=20)
ax.set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.savefig('ex18_complex_plane.png', dpi=300)
plt.show()
