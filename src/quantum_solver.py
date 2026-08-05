from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_primitives import Sampler

def run_qaoa_solver(qp, reps=2, maxiter=100):
    sampler = Sampler()
    optimizer = COBYLA(maxiter=maxiter)
    
    qaoa = QAOA(sampler=sampler, optimizer=optimizer, reps=reps)
    solver = MinimumEigenOptimizer(qaoa)
    
    result = solver.solve(qp)
    return result