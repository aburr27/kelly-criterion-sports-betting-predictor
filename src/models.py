\"\"\"Data models used by the project.\"\"\"
        from dataclasses import dataclass
        from typing import Optional

        @dataclass
        class GameRow:
            date: str
            team: str
            opponent: str
            league: str
            sport: str
            bet_type: str
            sportsbook: str
            odds_offered: str
            team_rating: Optional[float]
            opponent_rating: Optional[float]
            decimal_odds: Optional[float]
            bankroll: Optional[float]
            kelly_adj: Optional[float]

        @dataclass
        class Recommendation:
            team: str
            opponent: str
            predicted_win_prob: float
            sportsbook_implied_prob: float
            ev: float
            kelly_fraction: float
            bet_amount: float
