import logging
import os

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger("CAT-Modelling-System")
logger.setLevel(logging.INFO)

# Duplicate handlers avoid karne ke liye
if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # File Handler
    file_handler = logging.FileHandler(
        os.path.join(LOG_DIR, "app.log"),
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)