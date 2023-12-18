import numpy as np
import matplotlib.pyplot as plt

# Function definition
def potential_energy(r):
    return 0.5 - 1/r + (1000)/(2*r**2) - (1000)/r**3

# Generate a range of radial distances
r_values = np.linspace(0.1, 20, 1000)

# Calculate the potential energy for each radial distance
U_values = potential_energy(r_values)

# Plotting the potential energy with adjustable axes parameters
plt.plot(r_values, U_values, label='Potential Energy')
plt.xlabel('Radial Distance (r)')
plt.ylabel('Potential Energy (U)')
plt.title('Potential Energy Function: U(r) For L = sqrt(1000) > L_ibco')

# Add adjustable axes parameters
plt.xlim(0, 20)  # Set the x-axis limits
plt.ylim(0,20)  # Set the y-axis limits
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Add a horizontal dashed line at y=0
plt.grid(True)

# Show the plot
plt.legend()
plt.show()
