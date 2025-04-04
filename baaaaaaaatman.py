# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 19:32:54 2025

@author: daniy
"""

import numpy as np
import csv
import batman
import matplotlib.pyplot as plt

file_path = r"C:\Users\daniy\Downloads\CURVE2.csv"

# Read CSV file
flux = []
linestoskipl = 16  # Skip metadata lines

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for i in range(linestoskipl):  # Skip header
        next(reader)
    
    for row in reader:
        if len(row) >= 1 and row[0] != 'Null':  # Ensure at least one column exists
            try:
                flux.append(float(row[0]))  # Read flux values only
            except ValueError:
                print(f"Skipping invalid row: {row}")

# Convert to numpy array
flux = np.array(flux)

# Check if flux array is empty
if flux.size == 0:
    raise ValueError("No valid data loaded. Check the CSV file format.")

# Generate evenly spaced time array based on flux length
time = np.linspace(-0.5, 0.5, len(flux))


# Normalize flux properly
flux /= np.median(flux)

# Define transit parameters
params = batman.TransitParams()
params.t0 = 0  # Mid-transit at zero-centered time
params.per = 10.0  # Orbital period (days) - adjust as needed
params.rp = 0.1  # Planet-to-star radius ratio (Rp/Rs)
params.a = 15.0  # Semi-major axis in stellar radii (a/Rs)
params.inc = 89.0  # Inclination in degrees
params.ecc = 0.0  # Eccentricity (assuming circular orbit)
params.w = 90.0  # Argument of periastron (irrelevant for circular orbits)
params.u = [0.1, 0.3]  # Quadratic limb-darkening coefficients
params.limb_dark = "quadratic"

# Generate transit model
model = batman.TransitModel(params, time)
model_flux = model.light_curve(params)

# Plot results
plt.figure(figsize=(8, 5))
plt.scatter(time, flux, label="Observed Data", s=10, color="black")  # Scatter for better visualization
plt.plot(time, model_flux, label="Model Fit", color="red", linewidth=2)
plt.xlabel("Time (days)")
plt.ylabel("Flux")
plt.title("Light Curve of Physical model")
plt.xlim(time.min(), time.max())  # Ensure the x-axis covers the full range of data
plt.xlim(-0.5, 0.5)
plt.legend()
plt.show()
