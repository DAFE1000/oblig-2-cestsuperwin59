import numpy as np
import matplotlib.pyplot as plt

#function
def f(x):
    return np.exp(-x/4) * np.arctan(x)

#derivative
def g(x):
    return np.arctan(x) - 4/(x**2 + 1)

#derivative of g(x)
def dg(x):
    return 1/(x**2 + 1) + 8*x/(x**2 + 1)**2

#use Newton method
x = 1.0
for i in range(5):
    x = x - g(x)/dg(x)

#top point
x_top = x
y_top = f(x)

print("x =", round(x_top, 4))
print("y =", round(y_top, 4))

#plot
xs = np.linspace(-2, 8, 400)
ys = f(xs)

plt.plot(xs,ys)
plt.scatter(x_top, y_top)
plt.grid()
plt.show()

plt.savefig("plot.png")
print("Plot saved as plot.png")