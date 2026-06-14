import logging
import os

def log_generator():
    log_dir = "Reports/Logs"
    os.makedirs(log_dir, exist_ok=True)

    logging.basicConfig(
        filename=os.path.join(log_dir, "testlogreport.log"),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p',
        force=True
    )
    return logging.getLogger()