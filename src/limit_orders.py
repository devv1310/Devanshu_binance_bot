import sys
from binance.um_futures import UMFutures
from src.config import API_KEY, API_SECRET, BASE_URL
from src.utils import setup_logger, validate_input

logger = setup_logger()

def place_limit_order(symbol, side, quantity, price):
    try:
        client = UMFutures(key=API_KEY, secret=API_SECRET, base_url=BASE_URL)
        sym, qty, prc = validate_input(symbol, quantity, price)
        
        logger.info(f"Placing Limit Order: {side} {qty} {sym} @ {prc}")
        
        response = client.new_order(
            symbol=sym,
            side=side.upper(),
            type="LIMIT",
            timeInForce="GTC", # Good Till Cancelled
            quantity=qty,
            price=prc
        )
        
        logger.info(f"SUCCESS: Limit Order Placed. ID: {response['orderId']}")
        print(f"Limit Order Created! ID: {response['orderId']}")
        
    except Exception as e:
        logger.error(f"Limit Order Failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python -m src.limit_orders <SYMBOL> <SIDE> <QTY> <PRICE>")
    else:
        place_limit_order(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])