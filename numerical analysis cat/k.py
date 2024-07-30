import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    """The function to be minimized."""
    return x**2 + y**2 - x*y + x - y + 1

def gradient_f(x, y):
    """Gradient of the function."""
    dx = 2*x - y + 1
    dy = 2*y - x - 1
    return np.array([dx, dy])

def gradient_descent(learning_rate, max_iterations, tolerance):
    # Initial guess
    point = np.array([0.0, 0.0])
    
    # To store the path of the optimization
    path = [point]
    
    for i in range(max_iterations):
        grad = gradient_f(point[0], point[1])
        new_point = point - learning_rate * grad
        
        # Check for convergence
        if np.linalg.norm(new_point - point) < tolerance:
            break
        
        point = new_point
        path.append(point)
    
    return np.array(path), i+1

# Set parameters
learning_rate = 0.1
max_iterations = 1000
tolerance = 1e-6

# Run gradient descent
path, iterations = gradient_descent(learning_rate, max_iterations, tolerance)

# Print results
print(f"Minimum found at: {path[-1]}")
print(f"Value at minimum: {f(*path[-1])}")
print(f"Number of iterations: {iterations}")

# Plotting
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure(figsize=(10, 8))
plt.contour(X, Y, Z, levels=50)
plt.colorbar(label='f(x, y)')
plt.plot(path[:, 0], path[:, 1], 'ro-', linewidth=1.5, markersize=3)
plt.plot(path[-1, 0], path[-1, 1], 'g*', markersize=10)
plt.title('Gradient Descent Optimization')
plt.xlabel('x')
plt.ylabel('y')
plt.show()