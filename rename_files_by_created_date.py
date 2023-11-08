# This script takes all files in a folder and renames them by their creation date and time
# Format "year-month-day-hour-minutes-seconds"

import os
import datetime

def rename_files_with_creation_date(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            stat_info = os.stat(file_path)
            creation_timestamp = stat_info.st_birthtime
            creation_datetime = datetime.datetime.fromtimestamp(creation_timestamp)
            new_name = creation_datetime.strftime("%Y-%m-%d-%H-%M-%S") + os.path.splitext(filename)[1]
            new_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_path)
            print(f"Renamed {filename} to {new_name}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    rename_files_with_creation_date(folder_path)
