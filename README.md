# 🧮 Kelly Criterion Sports Betting Predictor

This project combines **sports betting analytics** with the **Kelly Criterion** and a **prediction model** to identify value bets, calculate bet sizing, and simulate profitability over time.

It’s designed for **NFL**, but you can easily adapt it to other sports.

## Quick start

        1. Create a Python environment (Python 3.8+ recommended)
        2. Install dependencies: `pip install -r requirements.txt`
        3. Run the example: `python src/main.py`

        The `data/example_bet_data.csv` file contains a sample matchup used by `src/main.py`.

## ⚙️ Core Formula

---

## 🔮 Predictions
The prediction module estimates **win probabilities** using:
- Simple rating systems (FPI, Elo, or Power Index)
- Historical team stats (OFF, DEF)
- Home-field advantage
- Bookmaker odds → implied win %

It outputs:
- **Predicted Win Probability**
- **Expected Value**
- **Recommended Bet Size**

---

## 📊 Example Run
```bash
python src/main.py

Game: Commanders @ Eagles
Predicted Win %: 41.9%
Sportsbook Win %: 43.5%
Expected Value: +6.11%
Recommended Bet: $13.97 (24.5% of bankroll unit)
