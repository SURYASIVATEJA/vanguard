import numpy as np
import pandas as pd

def generate_synthetic_market_data(num_assets=8, seed=42):
    np.random.seed(seed)
    asset_names = [f"Asset_{i+1}" for i in range(num_assets)]
    sectors = ["Equity", "Fixed_Income", "Commodity", "Real_Estate"] * (num_assets // 4 + 1)
    sectors = sectors[:num_assets]
    
    expected_returns = np.random.uniform(0.04, 0.14, num_assets)
    vols = np.random.uniform(0.08, 0.25, num_assets)
    
    corr_matrix = np.random.uniform(0.1, 0.6, (num_assets, num_assets))
    np.fill_diagonal(corr_matrix, 1.0)
    cov_matrix = np.outer(vols, vols) * corr_matrix
    
    return {
        "asset_names": asset_names,
        "returns": expected_returns,
        "cov_matrix": cov_matrix,
        "sectors": sectors
    }