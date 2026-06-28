import matplotlib.pyplot as plt
# graphing tool
import numpy as np
# NumPy arrays are faster than using the regular lists and loops

# getting our values
acceleration = float(input("Enter acceleration (m/s^2) "))
v_initial = float(input("Enter initial velocity (m/s) "))
time_max = float(input("Enter total duration (s) "))
time = np.linspace(0,time_max,1000) # generating a range of 1000 values from 0-60, equally spaced from each other
v = v_initial + acceleration*time # the first kinematic equation (for constant acceleration)
x = v_initial*time + 0.5*acceleration*(time**2) # the second kinematic equation (for constant acceleration)

# plotting
plt.subplot(1,2,1)
plt.plot(time,v)
plt.ylabel("Velocity (m/s)")
plt.xlabel("Time (s)")

plt.subplot(1,2,2)
plt.plot(time,x)
plt.ylabel("Displacement (m)")
plt.xlabel("Time (s)")

plt.tight_layout() # cleaning the graphs to put them on one interface
plt.show()
