import numpy as np

# SEMF coefficients from [1]
a1 = 15.56  # MeV
a2 = 17.23
a3 = 0.697
a4 = 93.14
a5 = 12.00

# Define the function f(A) = 2a2*a3^2*A^(4/3) - a3*a4^2*A + 4a2*a3*a4*A^(2/3) + 2a2*a4^2
def f(A):
    return 2*a2*a3**2 * A**(4/3) - a3*a4**2 * A + 4*a2*a3*a4 * A**(2/3) + 2*a2*a4**2

# Define the derivative f'(A)
def f_prime(A):
    return (8/3)*a2*a3**2 * A**(1/3) - a3*a4**2 + (8/3)*a2*a3*a4 * A**(-1/3)

# Newton-Raphson method
def newton_raphson(A0, tol=1e-12, max_iter=100):
    A = A0
    print(f"Iteration 0: A = {A:.10f}, f(A) = {f(A):.10e}")
    
    for i in range(max_iter):
        f_val = f(A)
        f_prime_val = f_prime(A)
        
        if abs(f_prime_val) < 1e-15:
            print("Derivative too small, method may fail.")
            break
        
        A_new = A - f_val / f_prime_val
        
        print(f"Iteration {i+1}: A = {A_new:.10f}, f(A) = {f(A_new):.10e}")
        
        if abs(A_new - A) < tol:
            print(f"\nConverged after {i+1} iterations.")
            print(f"Maximal A = {A_new:.10f}")
            return A_new
        
        A = A_new
    
    print(f"\nMax iterations reached. A = {A:.10f}")
    return A

# Try different initial guesses
print("=" * 60)
print("Solving for A using Newton-Raphson method")
print("=" * 60)

# Initial guess (A is mass number, typically > 0)
A0 = 90  # Starting guess

print(f"\nStarting with A0 = {A0}")
print("-" * 60)
solution = newton_raphson(A0)

def Z(A):
    num = a4 * A 
    den = 2 * (a3 * A**(2/3) + a4)
    return num/den 

print(f"Most stable element: Z = {Z(solution):.10f}")
