"""Downloads Mag 7 daily prices (2015 to today) and saves them to mag7_prices.json for the website."""
import json
import yfinance as yf

TICKERS = ["NVDA", "GOOGL", "MSFT", "META", "AAPL", "TSLA", "AMZN"]
px = yf.download(TICKERS, start="2015-01-01", auto_adjust=True, progress=False)["Close"]
px = px[TICKERS].dropna(how="all").ffill()
out = {
    "tickers": TICKERS,
    "dates": [d.strftime("%Y-%m-%d") for d in px.index],
    "close": {t: [None if v != v else round(float(v), 4) for v in px[t]] for t in TICKERS},
}
with open("mag7_prices.json", "w") as f:
    json.dump(out, f, separators=(",", ":"))
print(f"Saved mag7_prices.json: {len(px)} days, {px.index[0].date()} to {px.index[-1].date()}")
