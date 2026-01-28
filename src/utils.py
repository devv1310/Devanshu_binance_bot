import logging
import colorlog

def setup_logger():
    logger = logging.getLogger("BinanceBot")
    logger.setLevel(logging.INFO)

   
    file_handler = logging.FileHandler("bot.log")
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    
    console_handler = colorlog.StreamHandler()
    console_formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s: %(message)s',
        log_colors={'INFO': 'green', 'ERROR': 'red', 'WARNING': 'yellow'}
    )
    console_handler.setFormatter(console_formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

def validate_input(symbol, quantity, price=None):
    """Checks if inputs are valid numbers."""
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError("Quantity must be positive.")
        
        if price:
            p = float(price)
            if p <= 0:
                raise ValueError("Price must be positive.")
                
        return symbol.upper(), qty, float(price) if price else None
    except ValueError as e:
        raise ValueError(f"Input Error: {e}")