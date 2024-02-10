from portfolio_management import generate_portfolio
def adjust_strategies_for_life_events(user_preferences, current_strategies):
    adjusted_strategies = {
        "New Child Portfolio": generate_portfolio(),
        "Marriage Portfolio": generate_portfolio()
    }
    return adjusted_strategies
