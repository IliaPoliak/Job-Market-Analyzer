from config.config import FIELD, LOCATION
from logger.logging_utils import clear_log_file, log

from pipeline.collect_data import collect_data
from pipeline.extract_data import extract_data
from pipeline.clean_data import clean_data
from pipeline.save_to_db import save_to_db

import threading


pipeline_lock = threading.Lock()


def run_pipeline():
    # If lock is already held -> this returns False and skips
    if pipeline_lock.acquire(blocking=False):
        try:
            _pipeline()
        finally:
            pipeline_lock.release()  # Release the lock even if pipeline crashes


def _pipeline():

    clear_log_file()

    data = collect_data(FIELD, LOCATION) # Collect data from the website     
    data = extract_data(data) # Extract usefull data from the description such as skills and experience level
    data = clean_data(data)
    save_to_db(data)

    log("DONE")
