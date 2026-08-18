import logging
import os


def log_generator():

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'
    )

    # Create log directory if it does not exist
    log_directory = os.path.join(
        "Reports",
        "Logs"
    )

    os.makedirs(
        log_directory,
        exist_ok=True
    )

    # File Handler
    log_file = os.path.join(
        log_directory,
        "testlogreport.log"
    )

    file_handler = logging.FileHandler(log_file, mode='a')

    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
