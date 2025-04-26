import yfinance as yf
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo", dependencies=["mcp[cli]"])

# --- New yfinance Tools ---

@mcp.tool()
def get_stock_price(ticker: str) -> float | None:
    """
    Fetches the current stock price for a given ticker symbol.

    Args:
        ticker (str): The stock ticker symbol (e.g., "AAPL", "GOOGL").

    Returns:
        float | None: The current market price, or None if not found or an error occurs.
    """
    try:
        stock = yf.Ticker(ticker)
        # Use 'regularMarketPrice' or 'currentPrice'; check yfinance docs for preference
        # Using 'fast_info' can be quicker for just the price
        price = stock.fast_info.get('last_price')
        return price # Will be None if 'last_price' key doesn't exist
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}") # Log the error server-side
        return None

@mcp.tool()
def get_historical_prices(ticker: str, period: str = "1mo", interval: str = "1d") -> str | None:
    """
    Fetches historical stock prices for a given ticker symbol.

    Args:
        ticker (str): The stock ticker symbol (e.g., "AAPL", "GOOGL").
        period (str): The period to fetch data for (e.g., "1d", "5d", "1mo", "3mo", "6mo", "1y", "max"). Defaults to "1mo".
        interval (str): The data interval (e.g., "1m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"). Defaults to "1d".

    Returns:
        str | None: A JSON string representing the historical data (OHLCV),
                    or None if not found or an error occurs.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)
        if hist.empty:
            return None
        # Convert DataFrame to JSON string (orient='index' is often useful)
        # Resetting index makes the Date column a regular column before JSON conversion
        return hist.reset_index().to_json(orient="records", date_format="iso")
    except Exception as e:
        print(f"Error fetching historical data for {ticker}: {e}") # Log the error server-side
        return None