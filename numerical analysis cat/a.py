
def func(x, c=0):
    # This function represents the equation we want to solve
    # For x^2 - x - 2 = 0, we return x^2 - x - 2
    return x**2 - x - 2 + c

def regula_falsi(a, b, iterations=100, tol=1e-6):
    fa = func(a)
    fb = func(b)
    
    if fa * fb >= 0:
        print("Regula falsi method fails.")
        return None
    
    for i in range(iterations):
        # Calculate the intermediate value
        x = (a * fb - b * fa) / (fb - fa)
        fx = func(x)
        print(i, x, fx)
        
        # Check if the root is found
        if abs(fx) < tol:
            return x
        
        # Decide which half to take
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx
    
    print("Exceeded maximum iterations")
    return None

# Example usage
a = 1  # Lower bound of initial interval
b = 3  # Upper bound of initial interval

root = regula_falsi(a, b)

if root is not None:
    print(f"The root is approximately {root:.6f}")
    print(f"f({root:.6f}) = {func(root):.6e}")