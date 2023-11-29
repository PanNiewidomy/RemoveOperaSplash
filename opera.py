import psutil  # Import the psutil library for process management
import os  # Import the os library for file and folder operations
import shutil  # Import the shutil library for file operations

# Function to find the PID of the Opera browser process
def find_opera_pid():
    for process in psutil.process_iter(['pid', 'name']):
        if 'opera' in process.info['name'].lower():
            return process.info['pid']
    return "Opera browser PID not found."

# Function to find a process by its PID
def find_process_by_pid(pid):
    try:
        process = psutil.Process(int(pid))
        return process.exe()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return "Cannot find a process with PID: {}".format(pid)

# Function to find the latest version folder of Opera
def find_latest_opera_version_folder(path):
    # Find all subfolders in the specified path
    folders = [f.path for f in os.scandir(path) if f.is_dir()]
    # Sort the folders by modification date (newest at the end)
    folders.sort(key=lambda x: os.path.getmtime(x))
    # Return the latest folder
    return folders[-1] if folders else None

# Function to delete a file
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")
    except FileNotFoundError:
        print(f"File {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")

# Get the PID of the Opera browser process
opera_pid = find_opera_pid()
pid = opera_pid  # Replace 1234 with the actual PID of the Opera process
opera_exe_path = find_process_by_pid(pid)
# Get the path to the folder containing Opera executable
folder_path = os.path.dirname(opera_exe_path)
# Path to the folder where Opera is installed
opera_install_path = folder_path
# Find the latest version of Opera
latest_opera_folder = find_latest_opera_version_folder(opera_install_path)

if latest_opera_folder:
    # Path to the file we want to delete
    file_to_delete = os.path.join(latest_opera_folder, "opera_gx_splash.exe")
    # Delete the file
    delete_file(file_to_delete)
else:
    print("Opera folder not found.")