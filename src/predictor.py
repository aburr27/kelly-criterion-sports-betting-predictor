import numpy as np

def predict_win_probability(team_rating, opponent_rating, home_field_adv=1.5):
    """
    Basic model to predict win probability using a rating differential (like Elo/FPI).
    """
    rating_diff = team_rating - opponent_rating + home_field_adv
    win_prob = 1 / (1 + np.exp(-rating_diff / 10))  # Logistic model
    return round(win_prob, 3)

def expected_value(pred_win_prob, decimal_odds):
    """
    Compute expected value (EV%) given predicted win probability and odds.
    """
    ev = (pred_win_prob * decimal_odds) - 1
    return round(ev * 100, 2)  # EV in percentage
