# WISER x Vanguard Portfolio Co-Pilot 🚀

An interactive portfolio optimization co-pilot powered by **Hybrid QAOA (Qiskit 2.x)** and **Streamlit**, designed for the **WISER x Vanguard Challenge 2026**.

---

## 📌 Project Overview

Portfolio selection under strict cardinality and risk constraints is NP-hard. This project converts mean-variance portfolio optimization with hard cardinality bounds into an Unconstrained Quadratic Binary Optimization (QUBO) problem solved via QAOA (p=3) and Qiskit 2.x primitives.

### Key Features

* **QUBO Engine**: Mathematical encoding of returns, covariance risk, and penalty-weighted cardinality constraints.
* **Hybrid Optimization**: QAOA implementation leveraging `StatevectorSampler` benchmarked against Classical Exact Diagonalization.
* **Financial Guardrails**: Interactive management controls for drawdown limits, transaction costs, risk aversion (q), and penalty weight (P).
* **Co-Pilot Explainability**: Real-time narrative synthesis explaining selected asset trade-offs and compliance verification.

---

## 🏗️ Repository Architecture

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

---

## ⚡ Quick Start & Setup Instructions

### Option A: Local Setup

1. **Clone the Repository:**

git clone https://github.com/Aditya-Garimella13/vanguard.git
cd vanguard-wiser-quantum-portfolio

2. **Set Up a Virtual Environment:**

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies:**

pip install -r requirements.txt

4. **Run the Application:**

streamlit run app/portfolio_copilot.py

---

### Option B: Running in Google Colab (Cloudflare Tunnel Deployment)

1. **Clone Repository & Navigate:**

!git clone https://github.com/your-username/vanguard-wiser-quantum-portfolio.git
%cd vanguard-wiser-quantum-portfolio

2. **Install Dependencies & Cloudflare Tunnel:**

!pip install -r requirements.txt
!wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
!chmod +x cloudflared

3. **Launch Dashboard Server:**

import time, socket

# Kill existing processes
!pkill -9 -f streamlit
!pkill -9 -f cloudflared

# Start Streamlit in background
!streamlit run app/portfolio_copilot.py --server.port 8501 --server.address 0.0.0.0 > streamlit.log 2>&1 &
time.sleep(5)

# Verify binding and tunnel
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex(('127.0.0.1', 8501)) == 0:
    print("✅ Streamlit running! Access via the Cloudflare tunnel link below:\n")
    !./cloudflared tunnel --url http://127.0.0.1:8501
else:
    print("❌ Launch failed. Check logs:\n")
    !cat streamlit.log
s.close()

---

## 👥 Team Members & Contributions

| Name | Role | Core Contributions | Email / Contact |
| :--- | :--- | :--- | :--- |
| **Garimella Rama Aditya** | Quantum Algorithm Lead | Mapped Markowitz formulations into QUBO Hamiltonians, configured Qiskit 2.x StatevectorSampler, and built QAOA (p=3) solvers. | adityaa606@gmail.com |
| **Garimella Surya Siva Teja** | Full Stack & Financial Modeler | Developed the Streamlit dashboard, session-state mechanics, Cloudflare tunneling setup, and risk guardrail engine. | surya080204@gmail.com |

---

## 🛠️ Attributions & Tools

* **Quantum Framework**: Qiskit 2.x (qiskit-algorithms, qiskit-primitives)
* **UI Engine**: Streamlit
* **Core Libraries**: NumPy, Pandas, Matplotlib
* **Dataset Attribution**: Asset return profiles and covariance structures generated using standard Markowitz modern portfolio theory paradigms for benchmarking purposes.
