import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
# Function to calculate polar coordinates
def calculate_polar_coordinates(t, rc, delta_r, omega_r, omega_phi):
    r = rc + delta_r * np.cos(omega_r * t)
    phi = omega_phi * t - 2 * (omega_phi / omega_r) * (delta_r / rc) * np.sin(omega_r * t)
    return r, phi

# Function to convert polar coordinates to Cartesian coordinates
def polar_to_cartesian(r, phi):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return x, y

# Parameters
rc = 13.7 # baseline circular orbit radius
delta_r = 5.1  # perturbation amplitude
omega_r = 0.0167 # frequency of small radial oscillations
omega_phi = 0.0223  # orbital frequency of the baseline circular orbit

# Calculate total period
T_r = 2 * np.pi / omega_r
T_tot = 3 * T_r

# Generate equispaced t-values
t_values = np.linspace(0, T_tot, num=2001)

# Calculate polar coordinates
r_values, phi_values = calculate_polar_coordinates(t_values, rc, delta_r, omega_r, omega_phi)

# Convert polar coordinates to Cartesian coordinates
x_values, y_values = polar_to_cartesian(r_values, phi_values)

ratio = np.sqrt(rc / (rc - 6))
ratio_fraction = Fraction(ratio).limit_denominator()
# Plot the orbit
plt.figure(figsize=(8, 8))
plt.plot(x_values, y_values, label='Perturbed Orbit')
# plt.title('Perturbed Orbit')
plt.title(f'Perturbed Orbit\nrc = {rc}, ω_φ/ω_r = {ratio_fraction}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
