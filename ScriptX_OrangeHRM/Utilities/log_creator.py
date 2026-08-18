import logging

def log_generator():

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S %p')

    # File Handler
    file_handler = logging.FileHandler("Reports/Logs/testlogreport.log",mode='a')
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger