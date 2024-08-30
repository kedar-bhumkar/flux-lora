import os
import time
from constants import default_batch_size, default_sleep_time, default_timeout


def monitor_directory(folder_path):
    # Get the initial file count
    initial_files = set(os.listdir(folder_path))
    start_time = time.time()
    print(f"Initial file count: {len(initial_files)}")
    while True:
        # Sleep for 5 seconds
        time.sleep(default_sleep_time)

        # Get the current file count
        current_files = set(os.listdir(folder_path))

        # Check if 3 or more files have been added
        if len(current_files - initial_files) >= default_batch_size:
            print(f"{len(current_files - initial_files)} files added. Quitting...")
            break

        # Check if more than 3 minutes have passed
        if time.time() - start_time > default_timeout:
            print("More than 3 minutes have passed. Quitting...")
            break
