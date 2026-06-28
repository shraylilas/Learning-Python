import matplotlib.pyplot as plt
import numpy as np
# making a few functions
x = np.linspace(-10,10,100)
y1 = x**2
y2 = x + 1
y3 = np.abs(x) # modulus (absolute value) of x
y4 = x**3
y5 = x/2 + 15

plt.subplot(3, 2, 1)
plt.plot(x, y1)
plt.ylabel("y = x^2")

plt.subplot(3, 2, 2)
plt.plot(x, y2)
plt.ylabel("y = x+1")

plt.subplot(3, 2, 3)
plt.plot(x, y3)
plt.ylabel("y = |x|")

plt.subplot(3, 2, 4)
plt.plot(x, y4)
plt.ylabel("y = x^3")

plt.subplot(3, 2, 5)   
plt.plot(x, y5)
plt.ylabel("y = x/2 + 15")

# Hide the unused subplot
ax6 = plt.subplot(3, 2, 6)
ax6.set_visible(False)

plt.tight_layout()
plt.show()
