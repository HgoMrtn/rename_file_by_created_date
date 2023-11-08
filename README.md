# File Renaming Script

This Python script is designed to rename all files within a specified folder based on their creation date and time. The files will be renamed in the format "year-month-day-hour-minutes-seconds" to reflect their creation timestamps accurately.

## How It Works
The script takes a folder path as input and iterates through all the files in the specified folder. For each file, it retrieves the creation timestamp using the `st_birthtime` attribute and converts it into a human-readable date and time format. The script then renames the file with the formatted timestamp appended to its original file extension.

## Usage Instructions
1. **Clone the Repository:**

```bash
git clone https://github.com/username/repository.git
cd repository
```

2. **Run the Script:**

```bash
python rename_files_by_created_date.py
```


Enter the folder path when prompted. The script will rename all files in the specified folder based on their creation timestamps.

## Example
Suppose you have a file named `example.txt` in the specified folder, and its creation timestamp corresponds to 2023-11-08 15:30:45. After running the script, the file will be renamed to `2023-11-08-15-30-45.txt`.

## Notes
- This script utilizes the creation timestamp (`st_birthtime`) of the files to determine their creation date and time. File creation timestamps might not be available or accurate on certain operating systems or file systems.
- Use the script responsibly, and ensure you have appropriate permissions to rename files in the specified folder.

Feel free to contribute and enhance the script's functionality. Happy file renaming!
