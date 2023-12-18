import numpy as np
import matplotlib.pyplot as plt

# Function definitions
def relativistic(r):
    return 0.5 - 1/r + 64/(2*r**2) - 64/r**3

def Newtonian(r):
    return 0.5 - 1/r + 64/(2*r**2)

# Generate a range of radial distances
r_values = np.linspace(0.1, 20, 1000)

# Calculate the potential energy for each radial distance
U_values = relativistic(r_values)
another_values = Newtonian(r_values)

# Plotting both functions on the same plot
plt.plot(r_values, U_values, label='Relativistic', color='blue')
plt.plot(r_values, another_values, label='Newtonian', color='red')

plt.xlabel('Radial Distance (r)')
plt.ylabel('Function Value')
plt.title('Ueff for relativistic vs for newtonian at L=sqrt(64)')
plt.legend()
plt.xlim(0, 20)
plt.ylim(-20, 20)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)

# Show the plot
plt.show()
