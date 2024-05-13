#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 01:01:43 2024

@author: berkeozener
"""

import numpy as np
import matplotlib.pyplot as plt

L = 1  # Normalize side length of the square to 1 for simplicity
x = np.linspace(0, L, 100)
y = np.linspace(0, L, 100)
X, Y = np.meshgrid(x, y)

# Quantum confinement wavefunctions
def quantum_wavefunction(nx, ny, X, Y):
    return np.sin(nx * np.pi * X) * np.sin(ny * np.pi * Y)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
modes = [(1, 1), (1, 2), (2, 1), (2, 2)]
for ax, (nx, ny) in zip(axes.flat, modes):
    Z = quantum_wavefunction(nx, ny, X, Y)
    contour = ax.contourf(X, Y, Z, levels=50, cmap='viridis')
    ax.set_title(f'Wavefunction for nx={nx}, ny={ny}')
    fig.colorbar(contour, ax=ax)
plt.tight_layout()
plt.show()

# Constants
D = 1  # Assume a normalized constant density of states for simplicity
E_F = 5  # Fermi energy at 0K in arbitrary units

E = np.linspace(0, 10, 100)  # Energy range
DOS = D * np.ones_like(E)  # Constant density of states
Fermi_Dirac_0K = np.heaviside(E_F - E, 1)  # Step function at Fermi energy

# Plotting
plt.figure(figsize=(12, 6))

# Density of States plot
plt.subplot(1, 2, 1)
plt.plot(E, DOS, label='Density of States (DOS)')
plt.xlabel('Energy (arbitrary units)')
plt.ylabel('Density of States')
plt.title('Density of States for a 2D Electron Gas')
plt.axvline(x=E_F, color='r', linestyle='--', label='Fermi Energy at 0 K')
plt.legend()

# Fermi-Dirac Distribution at 0 K
plt.subplot(1, 2, 2)
plt.step(E, Fermi_Dirac_0K, where='post', label='Fermi-Dirac Distribution at 0 K')
plt.xlabel('Energy (arbitrary units)')
plt.ylabel('Occupation Probability')
plt.title('Fermi-Dirac Distribution at 0 K')
plt.axvline(x=E_F, color='r', linestyle='--', label='Fermi Energy at 0 K')
plt.ylim(-0.1, 1.1)  # Extend y-axis limits for clarity
plt.legend()

plt.tight_layout()
plt.show()