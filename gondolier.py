import subprocess
import tkinter as tk


def execute_command(current_command="docker ps -a"):
    # Define the terminal command to execute
    command = current_command

    # Execute the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Check the result
    if result.returncode == 0:
        print("Command executed successfully.")
        print("Output:")
        print(result.stdout)

        # Parse the output into rows
        rows = [line.split() for line in result.stdout.strip().split("\n")]
    else:
        print("Error executing command.")
        print("Error message:")
        print(result.stderr)


execute_command()

# Create a Tkinter window
window = tk.Tk()
window.title(
    "Simple Docker Command Center (for people who constantly forget CLI commands), v0.1"
)

# Add widgets and functionality...

# Start the Tkinter event loop
window.mainloop()
