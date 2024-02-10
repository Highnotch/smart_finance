import numpy as np

def track_financial_goals(investment_performance, investment_goals):
    progress = {goal: np.random.randint(0, 100) for goal in investment_goals}
    return progress

