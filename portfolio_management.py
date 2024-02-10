import numpy as np

def generate_portfolio():
    assets = ["Stocks", "Bonds", "Real Estate", "Commodities"]
    weights = np.random.dirichlet(np.ones(len(assets)), size=1).flatten()
    portfolio = dict(zip(assets, weights))
    return portfolio

def optimize_portfolio(user_preferences, current_portfolio):
    optimized_portfolio = {asset: weight * 0.9 for asset, weight in current_portfolio.items()}
    return optimized_portfolio

