# WISER x Vanguard Portfolio Co-Pilot 🚀

An interactive portfolio optimization co-pilot powered by **Hybrid QAOA (Qiskit 2.x)** and **Streamlit**, designed for the **WISER x Vanguard Challenge 2026**.

## 📌 Project Overview
Portfolio selection under strict cardinality and risk constraints is NP-hard. This project converts mean-variance portfolio optimization with hard cardinality bounds ($K=4$) into an Unconstrained Quadratic Binary Optimization (QUBO) problem solved via QAOA ($p=3$) and Qiskit 2.x primitives.

### Key Features
- **QUBO Engine**: Mathematical encoding of returns, covariance risk, and penalty-weighted cardinality constraints.
- **Hybrid Optimization**: QAOA implementation leveraging `StatevectorSampler` benchmarked against Classical Exact Diagonalization.
- **Financial Guardrails**: Interactive management controls for drawdown limits, transaction costs, risk aversion ($q$), and penalty weight ($P$).
- **Co-Pilot Explainability**: Real-time narrative synthesis explaining selected asset trade-offs and compliance verification.

---

## 🏗️ Repository Architecture
```text
.
├── app/
│   └── portfolio_copilot.py   # Streamlit UI & Co-Pilot Dashboard
├── src/
│   ├── qubo_builder.py        # QUBO Hamiltonian construction (Qiskit 2.x)
│   ├── qaoa_solver.py         # QAOA algorithm execution (p=3)
│   └── data_loader.py         # Synthetic market dataset loader
├── data/
│   ├── asset_universe.csv     # Asset expected returns and volatility profiles
│   └── covariance_matrix.csv  # 8x8 Covariance matrix
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation