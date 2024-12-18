import subprocess
import time
from datetime import datetime
from collections import deque

# Configuration
ADB_COMMAND = 'adb shell "cat /proc/meminfo"'  # Command to get memory info
OUTPUT_FILE = "output.txt"  # File to check for conditions
INTERVAL = 2  # Time interval in seconds between each command execution

# Pre-filename and post-exit buffers
pre_filename_logs = deque(maxlen=10)  # Store logs for 5 seconds before filename appears
post_exit_logging = False
post_exit_countdown = 10  # Log 5 seconds after 'exit'

def run_adb_command(command):
    """Runs the ADB command and returns the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error executing command: {e}"

def log_output(output, log_file):
    """Logs the output of the ADB command to a file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"[{timestamp}]\n{output}\n\n")

def extract_log_file():
    """Extracts the log filename from output.txt if it contains a .txt filename."""
    try:
        with open(OUTPUT_FILE, "r") as file:
            lines = file.readlines()
        for line in lines:
            if line.strip().endswith(".txt"):
                print("Found the filenmame")
                return line.strip()
    except FileNotFoundError:
        print(f"{OUTPUT_FILE} not found. Please ensure the file exists.")
    return None

def check_exit_condition():
    """Checks if 'exit' is present in output.txt."""
    try:
        with open(OUTPUT_FILE, "r") as file:
            lines = file.readlines()
        for line in lines:
            if 'exit' in line.lower():
                print("Found 'exit' in output.txt.")
                return True
    except FileNotFoundError:
        pass
    return False

def clear_output_file():
    """Clears the contents of output.txt."""
    try:
        with open(OUTPUT_FILE, "w") as file:
            file.truncate(0)
        print(f"Cleared {OUTPUT_FILE}.")
    except FileNotFoundError:
        print(f"{OUTPUT_FILE} not found. Nothing to clear.")

def main():
    global post_exit_logging, post_exit_countdown

    print(f"Monitoring {OUTPUT_FILE} and logging ADB command '{ADB_COMMAND}' every {INTERVAL} seconds. Press Ctrl+C to stop.")
    current_log_file = None

    while True:
        output = run_adb_command(ADB_COMMAND)

        # Check conditions from output.txt
        if not current_log_file:
            current_log_file = extract_log_file()
        
        if current_log_file and not post_exit_logging:
            # Write pre-filename logs first
            while pre_filename_logs:
                print("Logging pre command data...")
                log_output(pre_filename_logs.popleft(), current_log_file)
            log_output(output, current_log_file)
            print("Normal Logging")
        else:
            # Store pre-filename logs
            pre_filename_logs.append(output)
            print("Storing prelog data")
        
        if post_exit_logging:
            log_output(output, current_log_file)
            print("Post-exit Logging")
            post_exit_countdown -= 1
            if post_exit_countdown <= 0:
                post_exit_logging = False
                clear_output_file()
                break
        
        if check_exit_condition():
            post_exit_logging = True

        time.sleep(INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript stopped by user.")
        clear_output_file()
