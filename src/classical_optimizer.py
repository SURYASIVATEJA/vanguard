import cvxpy as cp
import numpy as np

def solve_classical_baseline(returns, cov_matrix, risk_aversion=0.5, target_k=4):
    n = len(returns)
    x = cp.Variable(n, boolean=True)
    
    objective = cp.Minimize(risk_aversion * cp.quad_form(x, cov_matrix) - returns.T @ x)
    constraints = [cp.sum(x) == target_k]
    
    prob = cp.Problem(objective, constraints)
    prob.solve(solver=cp.ECOS_BB)
    
    return {
        "allocation": x.value,
        "objective_value": prob.value,
        "status": prob.status
    }