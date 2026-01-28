import time
import sys
from binance.um_futures import UMFutures
from src.config import API_KEY, API_SECRET, BASE_URL
from src.utils import setup_logger, validate_input

logger = setup_logger()

def execute_twap(symbol, side, total_qty, duration_minutes, steps):
    client = UMFutures(key=API_KEY, secret=API_SECRET, base_url=BASE_URL)
    
    sym, total, _ = validate_input(symbol, total_qty)
    steps = int(steps)
    duration_sec = int(duration_minutes) * 60
    
    # Calculate size of each slice
    slice_qty = round(total / steps, 3)
    wait_time = duration_sec / steps
    
    logger.info(f"Starting TWAP: {side} {total} {sym} | {steps} trades | Every {wait_time}s")

    for i in range(steps):
        try:
            logger.info(f"Executing TWAP slice {i+1}/{steps}...")
            client.new_order(
                symbol=sym,
                side=side.upper(),
                type="MARKET",
                quantity=slice_qty
            )
            if i < steps - 1:
                time.sleep(wait_time)
        except Exception as e:
            logger.error(f"Error in TWAP slice {i+1}: {e}")

    logger.info("TWAP Strategy Completed.")

if __name__ == "__main__":
    # Usage: python -m src.advanced.twap BTCUSDT BUY 0.05 1 5
    # (Buy 0.05 BTC over 1 minute, split into 5 trades)
    if len(sys.argv) < 6:
        print("Usage: python -m src.advanced.twap <SYMBOL> <SIDE> <TOTAL_QTY> <MINUTES> <STEPS>")
    else:
        execute_twap(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
