import time
from config.config import LOG_FILENAME


def log(message, delete_last_line=False):
    if delete_last_line:
        _delete_last_line()

    with open(LOG_FILENAME, 'a') as log_file:
        log_file.write(f"{message}\n")


def start_timing(process_name):
    
    # Logging
    log(f"{process_name}\n")

    # Start timer
    start = time.perf_counter()

    return start


def finish_timing(start, progress_bar=False):
    
    # Finish timer
    end = time.perf_counter()
    
    # Logging
    if not progress_bar:
        _delete_last_line()

    log(f"IT TOOK {(end - start):.6f} SECONDS\n\n")


def print_progress_bar(n1, n2):

    width = 100

    one_side_width = int(width / 2)

    pipes = round(n1 / n2 * width)
    spaces = round((n2-n1) / n2 * width)
    
    pipes_left = pipes if pipes < one_side_width else one_side_width
    pipes_right = 0 if pipes < one_side_width else pipes - one_side_width

    spaces_left = 0 if spaces < one_side_width else spaces - one_side_width
    spaces_right = spaces if spaces < one_side_width else one_side_width

    n1_digits = len(str(n1))
    n2_digits = len(str(n2))
    digit_padding = n2_digits - n1_digits

    progress_bar = "["
    progress_bar += ("|" * pipes_left) + (" " * spaces_left)
    progress_bar += " " + (" " * digit_padding) + str(n1) + " / " + str(n2) + " "
    progress_bar += ("|" * pipes_right) + (" " * spaces_right)
    progress_bar += "]"

    log(progress_bar, delete_last_line=True)


def clear_log_file():
    with open(LOG_FILENAME, 'w') as f:
        pass  # just open and close to clear


def _delete_last_line():
    with open(LOG_FILENAME, 'r') as f:
        lines = f.readlines()
    
    if lines:
        lines = lines[:-1]  # remove the last line
    
    with open(LOG_FILENAME, 'w') as f:
        f.writelines(lines)
