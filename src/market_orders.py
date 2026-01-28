import sys
from binance.um_futures import UMFutures
from src.config import API_KEY, API_SECRET, BASE_URL
from src.utils import setup_logger, validate_input

logger = setup_logger()

def place_market_order(symbol, side, quantity):
    try:
        # Connect to Binance
        client = UMFutures(key=API_KEY, secret=API_SECRET, base_url=BASE_URL)
        
        # Validate
        sym, qty, _ = validate_input(symbol, quantity)
        
        logger.info(f"Placing Market Order: {side} {qty} {sym}")
        
        # Send Order
        response = client.new_order(
            symbol=sym,
            side=side.upper(),
            type="MARKET",
            quantity=qty
        )
        
        logger.info(f"SUCCESS: Order ID {response['orderId']} Filled.")
        print(f"Done! Order ID: {response['orderId']}")
        
    except Exception as e:
        logger.error(f"Failed to place order: {e}")

if __name__ == "__main__":
    # Example usage: python src/market_orders.py BTCUSDT BUY 0.01
    if len(sys.argv) < 4:
        print("Usage: python -m src.market_orders <SYMBOL> <SIDE> <QTY>")
    else:
        place_market_order(sys.argv[1], sys.argv[2], sys.argv[3])
