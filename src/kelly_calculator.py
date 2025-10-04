\"\"\"Kelly Criterion betting size calculator.\"\"\"
        from typing import Tuple

        def kelly_fraction(implied_win_prob: float, decimal_odds: float) -> float:
            \"\"\"Return the Kelly fraction (no bankroll scaling).\"\"\"
            # Kelly formula: f* = (bp - q) / b, where b = decimal_odds - 1, p = implied_win_prob, q = 1 - p
            b = decimal_odds - 1
            p = implied_win_prob
            q = 1 - p
            if b <= 0:
                return 0.0
            f = (b * p - q) / b
            return max(0.0, f)

        def kelly_bet_size(implied_win_prob: float, decimal_odds: float, bankroll: float, adj_factor: float = 0.5) -> Tuple[float, float]:
            \"\"\"Calculate recommended bet amount and return (bet_amount, kelly_fraction).
            
            adj_factor is a conservative multiplier (common practice: 0.25 - 0.5)
            \"\"\"
            f = kelly_fraction(implied_win_prob, decimal_odds)
            bet = bankroll * f * adj_factor
            return round(bet, 2), f
