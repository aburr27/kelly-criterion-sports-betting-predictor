\"\"\"Main script to load CSV, generate predictions, compute EV and Kelly bet sizes.\"\"\"
        from src.kelly_calculator import kelly_bet_size, kelly_fraction
        from src.predictor import predict_win_probability, expected_value
        from src.utils import load_games_from_csv, implied_prob_from_decimal
        from src.models import Recommendation
        import pprint

        def analyze_games(csv_path='data/example_bet_data.csv'):
            games = load_games_from_csv(csv_path)
            recs = []
            for g in games:
                # Determine predicted probability using available ratings
                if g.team_rating is None or g.opponent_rating is None:
                    # If ratings missing, skip or fall back to implied — here we skip
                    print(f\"Skipping {g.team} vs {g.opponent} because ratings are missing.\")
                    continue
                pred = predict_win_probability(g.team_rating, g.opponent_rating, home_field_adv=0.0)
                dec = g.decimal_odds or  None
                if dec is None:
                    print(f\"Skipping {g.team} vs {g.opponent} because decimal odds are missing.\")
                    continue
                sportsbook_prob = implied_prob_from_decimal(dec)
                ev = expected_value(pred, dec)
                bet_amount, f = kelly_bet_size(pred, dec, g.bankroll or 0.0, g.kelly_adj or 0.5)
                rec = Recommendation(
                    team=g.team,
                    opponent=g.opponent,
                    predicted_win_prob=pred,
                    sportsbook_implied_prob=sportsbook_prob,
                    ev=ev,
                    kelly_fraction=f,
                    bet_amount=bet_amount
                )
                recs.append(rec)
            return recs

        if __name__ == '__main__':
            recs = analyze_games('data/example_bet_data.csv')
            pp = pprint.PrettyPrinter(indent=2)
            for r in recs:
                print('------------------------------')
                pp.pprint({
                    'Matchup': f\"{r.team} vs {r.opponent}\",
                    'Predicted Win %': f\"{r.predicted_win_prob*100:.2f}%\",
                    'Sportsbook Implied %': f\"{(r.sportsbook_implied_prob or 0)*100:.2f}%\",
                    'Expected Value %': f\"{r.ev*100:.2f}%\",
                    'Kelly Fraction': f\"{r.kelly_fraction:.4f}\",
                    'Recommended Bet $': f\"${r.bet_amount:,.2f}\"
                })
