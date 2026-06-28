import matplotlib.pyplot as plt
import numpy as np
import math
from math import sin, cos

# Notation: s = displacement, v = velocity, t = time, a = acceleration, t = time, etc.
# suffixed by _x or _y to indicate axes and 0 for naught

# using SI units
a_x = 0 # ignoring air resistance
a_y = -9.8 # g = 9.8m/s^2, free-fall

# projectile starts at the origin, (x,y) indicates coordinates
# in the x-y plane
x = 0
y = 0

v0 = float(input("Enter your initial velocity (m/s) ")) # initial velocity
theta = math.radians(float(input("Enter the angle of the projectile (degrees) "))) # angle in degrees
dt = 0.01 # time increment

# Our velocity is resolved into two vectors along x and y-axes
v0_x = v0*cos(theta)
v0_y = v0*sin(theta)

# we need to save our coordinates
abscissas = []
ordinates = []
times = []
v_x = v0_x # a_x = 0
v_y = v0_y # we're "throwing" something with a certain initial velocity
t = 0 
while y >= 0:
    v_y += a_y*dt
    x += v_x*dt
    y += v_y*dt
    abscissas.append(x)
    ordinates.append(y)
    t += dt
    times.append(t)

max_range = (v0**2 * math.sin(2*theta))/abs(a_y) # abs(a_y) because magnitude
max_height = (v0**2 * math.sin(theta)**2)/(2*abs(a_y)) # ^^^

print(f"Max. range is {max_range} and max. height is {max_height} (metres)")

plt.plot(abscissas,ordinates)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

plt.plot(times,ordinates)
plt.xlabel("Time (seconds)")
plt.ylabel("Height (metres)")
plt.show()
