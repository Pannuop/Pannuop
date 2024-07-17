import os
import signal
import time
import subprocess


# Join :- @DX4_CHEATS # Set the path to the script you want to restart
script_to_restart = "new.py"

def restart_script():
    # Join :- @DX4_CHEATS # Run the script
    print("chal raha hai bc.....")
    process = subprocess.Popen(["python3", script_to_restart], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    process = restart_script()
    while True:
        time.sleep(480)  # Join :- @DX4_CHEATS # Sleep for 30 seconds
        # Join :- @DX4_CHEATS # Send Ctrl+C signal to the process
        process.send_signal(signal.SIGINT)
        # Join :- @DX4_CHEATS # Wait for the process to terminate
        process.wait()
        # Join :- @DX4_CHEATS # Restart the script
        process = restart_script()

if __name__ == "__main__":
    main()