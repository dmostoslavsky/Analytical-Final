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
#rc = 13.7 # baseline circular orbit radius for 4/3
#delta_r = 4.1  # perturbation amplitude for 4/3
#omega_r = 0.0167 # frequency of small radial oscillations for 4/3

#rc = 9.375 # baseline circular orbit radius for 5/3
#delta_r = 3.1  # perturbation amplitude for 5/3
#omega_r = 0.0253477771 # frequency of small radial oscillations for 5/3

# rc = 14 # baseline circular orbit radius for 7/4
# delta_r = 5.1  # perturbation amplitude for 7/4
# omega_r = 0.01628008 # frequency of small radial oscillations for 7/4

rc = 18 # baseline circular orbit radius for 3/2
delta_r = 6.1  # perturbation amplitude for 3/2
omega_r = 0.011712139 # frequency of small radial oscillations for 3/2

# Calculate omega_phi using the given ratio
ratio = np.sqrt(rc / (rc - 6))
#omega_phi = 0.0223 #4/3
#omega_phi = 0.042246295 #5/3
# omega_phi = 0.02153652 #7/4
omega_phi = 0.01434438276 #3/2

# Convert ratio to fraction
ratio_fraction = Fraction(ratio).limit_denominator()

# Generate equispaced t-values
T_r = 2 * np.pi / omega_r
T_tot = 3 * T_r
t_values = np.linspace(0, T_tot, num=2001)

# Calculate polar coordinates for the entire perturbed orbit
r_values, phi_values = calculate_polar_coordinates(t_values, rc, delta_r, omega_r, omega_phi)

# Divide the time values into three segments
t_seg1 = t_values[t_values <= T_tot/3]
t_seg2 = t_values[(T_tot/3 < t_values) & (t_values <= 2*T_tot/3)]
t_seg3 = t_values[t_values > 2*T_tot/3]

# Calculate polar coordinates for each segment
r_values_seg1, phi_values_seg1 = calculate_polar_coordinates(t_seg1, rc, delta_r, omega_r, omega_phi)
r_values_seg2, phi_values_seg2 = calculate_polar_coordinates(t_seg2, rc, delta_r, omega_r, omega_phi)
r_values_seg3, phi_values_seg3 = calculate_polar_coordinates(t_seg3, rc, delta_r, omega_r, omega_phi)

# Convert polar coordinates to Cartesian coordinates for each segment
x_values_seg1, y_values_seg1 = polar_to_cartesian(r_values_seg1, phi_values_seg1)
x_values_seg2, y_values_seg2 = polar_to_cartesian(r_values_seg2, phi_values_seg2)
x_values_seg3, y_values_seg3 = polar_to_cartesian(r_values_seg3, phi_values_seg3)

# Plot each segment separately with a different color
plt.figure(figsize=(8, 8))
plt.plot(x_values_seg1, y_values_seg1, label='Segment 1', linewidth=2, color='blue')
plt.plot(x_values_seg2, y_values_seg2, label='Segment 2', linewidth=2, color='orange')
plt.plot(x_values_seg3, y_values_seg3, label='Segment 3', linewidth=2, color='green')
plt.title(f'Perturbed Orbit\nrc = {rc}, ω_φ/ω_r = {ratio_fraction}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
