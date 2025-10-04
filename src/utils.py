\"\"\"Utility functions for odds conversion and CSV loading.\"\"\"
        import csv
        from typing import List, Dict, Any, Optional
        from .models import GameRow

        def american_to_decimal(american_odds: str) -> Optional[float]:
            \"\"\"Convert American odds (e.g. -115, +150) to decimal odds (e.g. 1.87, 2.5).
            
            If input is already decimal, try to coerce to float.
            \"\"\"
            if american_odds is None:
                return None
            s = str(american_odds).strip()
            if s == '':
                return None
            try:
                if s.startswith('+') or s.startswith('-'):
                    a = int(s)
                    if a > 0:
                        return round((a / 100) + 1, 2)
                    else:
                        return round((100 / abs(a)) + 1, 2)
                # maybe it's already decimal like 1.51
                return float(s)
            except Exception:
                return None

        def implied_prob_from_decimal(decimal_odds: float) -> Optional[float]:
            if not decimal_odds or decimal_odds <= 0:
                return None
            return round(1.0 / decimal_odds, 4)

        def load_games_from_csv(path: str) -> List[GameRow]:
            rows = []
            with open(path, newline='', encoding='utf-8') as fh:
                reader = csv.DictReader(fh)
                for r in reader:
                    # parse ratings and odds with safe fallbacks
                    try:
                        tr = float(r.get('Team Rating')) if r.get('Team Rating') else None
                    except:
                        tr = None
                    try:
                        orr = float(r.get('Opponent Rating')) if r.get('Opponent Rating') else None
                    except:
                        orr = None
                    dec = american_to_decimal(r.get('Odds Offered')) or (float(r.get('Decimal Odds')) if r.get('Decimal Odds') else None)
                    try:
                        bank = float(r.get('Bankroll')) if r.get('Bankroll') else None
                    except:
                        bank = None
                    try:
                        kadj = float(r.get('Kelly Adj.')) if r.get('Kelly Adj.') else 0.5
                    except:
                        kadj = 0.5
                    gr = GameRow(
                        date = r.get('Date',''),
                        team = r.get('Team',''),
                        opponent = r.get('Opponent',''),
                        league = r.get('League',''),
                        sport = r.get('Sport',''),
                        bet_type = r.get('Bet Type',''),
                        sportsbook = r.get('Sportsbook',''),
                        odds_offered = r.get('Odds Offered',''),
                        team_rating = tr,
                        opponent_rating = orr,
                        decimal_odds = dec,
                        bankroll = bank,
                        kelly_adj = kadj
                    )
                    rows.append(gr)
            return rows
