\"\"\"Prediction utilities: simple rating-differential logistic model and EV calc.\"\"\"
        import numpy as np

        def predict_win_probability(team_rating: float, opponent_rating: float, home_field_adv: float = 0.0) -> float:
            \"\"\"Predict win probability from rating differential using a logistic curve.

            The scale is adjustable by dividing the rating diff by a temperature (here 10).
            Return a probability between 0 and 1.
            \"\"\"
            rating_diff = team_rating - opponent_rating + home_field_adv
            # Temperature controls steepness; 10 is a reasonable starting point for ratings on a 0-100 scale.
            prob = 1 / (1 + np.exp(-rating_diff / 10))
            return float(prob)

        def expected_value(pred_win_prob: float, decimal_odds: float) -> float:
            \"\"\"Return EV as a proportion (e.g., 0.06 = +6% expected value).\"\"\"
            return (pred_win_prob * decimal_odds) - 1
