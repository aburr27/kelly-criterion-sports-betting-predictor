from kelly_calculator import kelly_bet_size
from predictor import predict_win_probability, expected_value

if __name__ == "__main__":
    # Example matchup: Washington Commanders vs Philadelphia Eagles
    team = "Washington Commanders"
    opponent = "Philadelphia Eagles"
    team_rating = 70.5
    opponent_rating = 75.0
    home_field_adv = 0  # Commanders away

    bankroll = 25000
    adj_factor = 0.5
    decimal_odds = 1.51

    # Step 1: Predict win probability
    predicted_win_prob = predict_win_probability(team_rating, opponent_rating, home_field_adv)
    print(f"Predicted Win Probability: {predicted_win_prob * 100:.2f}%")

    # Step 2: Calculate Expected Value
    ev_percent = expected_value(predicted_win_prob, decimal_odds)
    print(f"Expected Value: {ev_percent:.2f}%")

    # Step 3: Kelly Criterion Bet Size
    bet_amount, kelly_fraction = kelly_bet_size(predicted_win_prob, decimal_odds, bankroll, adj_factor)
    print(f"Kelly Fraction: {kelly_fraction:.2%}")
    print(f"Recommended Bet Size: ${bet_amount:,.2f}")
