# Opera Browser Process Management Script

This Python script provides a set of functions to manage the Opera browser process. It allows you to find the PID (Process ID) of the Opera browser process, locate the Opera installation folder, and delete a specific file from the latest version of Opera.

## Prerequisites

Before using this script, make sure you have the following Python libraries installed:

- [psutil](https://pypi.org/project/psutil/): Used for process management.
- [os](https://docs.python.org/3/library/os.html): Used for file and folder operations.
- [shutil](https://docs.python.org/3/library/shutil.html): Used for file operations.

# Opera Browser Process Management Script

## Functions

1. **find_opera_pid()**
   - This function finds the PID of the Opera browser process.
2. **find_process_by_pid(pid)**
   - This function takes a PID as input and returns the path to the executable of the corresponding process.
3. **find_latest_opera_version_folder(path)**
   - This function finds the latest version folder of the Opera browser installation in the specified path.
4. **delete_file(file_path)**
   - This function deletes a specified file.

## Usage

To use this script:
1. Ensure that the required libraries are installed.
2. Run the script.
3. The script will automatically find the Opera browser process and the latest Opera version folder. It will attempt to delete a file named "opera_gx_splash.exe" from the latest version of Opera.

## Note

- If the Opera browser process is not found, it will print "Opera browser PID not found."
- If the latest Opera version folder is not found, it will print "Opera folder not found."
- If the file "opera_gx_splash.exe" is successfully deleted, it will print a confirmation message. If the file does not exist or if an error occurs during deletion, appropriate messages will be displayed.

Please use this script responsibly and ensure that you have the necessary permissions to perform file and process operations on your system.


## RUN .EXE

1. Download build folder.
2. Ensure that you have Opera running.
3. Run the 'opera.exe' file. 
4. The 'opera_gx_splash.exe' file will be deleted, and in case of any issues, you will receive the message 'Opera folder not found'.
