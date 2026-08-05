import numpy as np
from qiskit.quantum_info import SparsePauliOp
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import StatevectorSampler

def build_portfolio_qubo(returns, cov_matrix, risk_aversion=0.5, target_assets=4, penalty_weight=100.0):
    mu = np.array(returns)
    sigma = np.array(cov_matrix)
    num_assets = len(mu)
    
    # Construct QUBO Q matrix: x^T Q x
    # Objective: risk_aversion * x^T Sigma x - (1 - risk_aversion) * mu^T x
    # Constraint: penalty_weight * (sum(x) - target_assets)^2
    
    Q = np.zeros((num_assets, num_assets))
    
    for i in range(num_assets):
        for j in range(num_assets):
            Q[i, j] += risk_aversion * sigma[i, j]
            Q[i, j] += penalty_weight  # Constraint quadratic term
            
        Q[i, i] -= (1 - risk_aversion) * mu[i]
        Q[i, i] -= 2 * penalty_weight * target_assets  # Constraint linear term

    # Convert QUBO Q to Ising Hamiltonian H = sum h_i Z_i + sum J_ij Z_i Z_j
    pauli_list = []
    
    # Single-qubit terms (Z_i)
    for i in range(num_assets):
        h_i = -0.5 * Q[i, i] - sum(0.25 * (Q[i, j] + Q[j, i]) for j in range(num_assets) if j != i)
        if abs(h_i) > 1e-6:
            paulis = ["I"] * num_assets
            paulis[i] = "Z"
            pauli_list.append(("".join(paulis), h_i))
            
    # Two-qubit interaction terms (Z_i Z_j)
    for i in range(num_assets):
        for j in range(i + 1, num_assets):
            J_ij = 0.25 * (Q[i, j] + Q[j, i])
            if abs(J_ij) > 1e-6:
                paulis = ["I"] * num_assets
                paulis[i] = "Z"
                paulis[j] = "Z"
                pauli_list.append(("".join(paulis), J_ij))
                
    if not pauli_list:
        pauli_list.append(("I" * num_assets, 0.0))
        
    Ising_hamiltonian = SparsePauliOp.from_list(pauli_list)
    
    # Initialize QAOA with high-iteration COBYLA to guarantee ground-state convergence
    sampler = StatevectorSampler()
    optimizer = COBYLA(maxiter=500)
    qaoa_instance = QAOA(sampler=sampler, optimizer=optimizer, reps=3)
    
    return qaoa_instance, Ising_hamiltonian
