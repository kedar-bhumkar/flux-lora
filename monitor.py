import os
import time

def monitor_directory(folder_path):
    # Get the initial file count
    initial_files = set(os.listdir(folder_path))
    start_time = time.time()
    print(f"Initial file count: {len(initial_files)}")
    while True:
        # Sleep for 5 seconds
        time.sleep(5)

        # Get the current file count
        current_files = set(os.listdir(folder_path))
        file_count = len(current_files)
        #print(f"Current file count: {file_count}")
        # Check if 3 or more files have been added
        if len(current_files - initial_files) >= 3:
            print(f"{len(current_files - initial_files)} files added. Quitting...")
            break

        # Check if more than 3 minutes have passed
        if time.time() - start_time > 200:
            print("More than 3 minutes have passed. Quitting...")
            break

        #print(f"Current file count: {file_count}")

#if __name__ == "__main__":
#    folder_to_watch = "C:\\Users\\kedar\\Desktop\\Delete this\\images"  # Replace with your folder path
#    monitor_directory(folder_to_watch)
