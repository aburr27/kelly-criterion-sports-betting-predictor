def odds_to_implied_prob(decimal_odds):
    return round(1 / decimal_odds, 3)

def american_to_decimal(american_odds):
    if american_odds > 0:
        return round((american_odds / 100) + 1, 2)
    else:
        return round((100 / abs(american_odds)) + 1, 2)
