import numpy as np

def power_iteration(A, num_iterations=1000, tolerance=1e-8):
    n = A.shape[0]
    v = np.random.rand(n)
    v = v / np.linalg.norm(v)
    
    for _ in range(num_iterations):
        Av = A @ v
        eigenvalue = v.T @ Av
        new_v = Av / np.linalg.norm(Av)
        
        if np.allclose(v, new_v, atol=tolerance) or np.allclose(v, -new_v, atol=tolerance):
            return eigenvalue, new_v
        
        v = new_v
    
    return eigenvalue, v

def deflate(A, eigenvalue, eigenvector):
    return A - eigenvalue * np.outer(eigenvector, eigenvector)

def power_iteration_all(A, num_eigenvalues=None):
    if num_eigenvalues is None:
        num_eigenvalues = A.shape[0]
    
    eigenvalues = []
    eigenvectors = []
    A_deflated = A.copy()
    
    for _ in range(num_eigenvalues):
        eigenvalue, eigenvector = power_iteration(A_deflated)
        eigenvalues.append(eigenvalue)
        eigenvectors.append(eigenvector)
        A_deflated = deflate(A_deflated, eigenvalue, eigenvector)
    
    return np.array(eigenvalues), np.array(eigenvectors).T

# Test the Power Iteration method
A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

eigenvalues_power, eigenvectors_power = power_iteration_all(A)
print("Power Iteration Method:")
print("Eigenvalues:", eigenvalues_power)
print("Eigenvectors:")
print(eigenvectors_power)

def qr_algorithm(A, num_iterations=1000, tolerance=1e-8):
    n = A.shape[0]
    Q = np.eye(n)
    
    for _ in range(num_iterations):
        Q_k, R_k = np.linalg.qr(A)
        A_next = R_k @ Q_k
        
        if np.allclose(A, A_next, atol=tolerance):
            break
        
        A = A_next
        Q = Q @ Q_k
    
    eigenvalues = np.diag(A)
    eigenvectors = Q
    
    return eigenvalues, eigenvectors

# Test the QR Algorithm
eigenvalues_qr, eigenvectors_qr = qr_algorithm(A)
print("\nQR Algorithm:")
print("Eigenvalues:", eigenvalues_qr)
print("Eigenvectors:")
print(eigenvectors_qr)

# NumPy's eigenvalue solver (for reference)
eigenvalues_np, eigenvectors_np = np.linalg.eig(A)

print("\nNumPy's eigenvalue solver (for reference):")
print("Eigenvalues:", eigenvalues_np)
print("Eigenvectors:")
print(eigenvectors_np)

# Compare results
print("\nComparison:")
print("Power Iteration eigenvalues:", eigenvalues_power)
print("QR Algorithm eigenvalues:", eigenvalues_qr)
print("NumPy eigenvalues:", eigenvalues_np)

# Function to check if eigenvectors are valid
def check_eigenvectors(A, eigenvalues, eigenvectors):
    for i in range(len(eigenvalues)):
        lhs = A @ eigenvectors[:, i]
        rhs = eigenvalues[i] * eigenvectors[:, i]
        if not np.allclose(lhs, rhs, atol=1e-6):
            return False
    return True

print("\nEigenvector validity:")
print("Power Iteration:", check_eigenvectors(A, eigenvalues_power, eigenvectors_power))
print("QR Algorithm:", check_eigenvectors(A, eigenvalues_qr, eigenvectors_qr))
print("NumPy:", check_eigenvectors(A, eigenvalues_np, eigenvectors_np))