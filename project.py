import tkinter as tk
import subprocess

# Define the terminal command to execute
command = "docker ps -a"

# Execute the command
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Check the result
if result.returncode == 0:
    print("Command executed successfully.")
    print("Output:")
    print(result.stdout)
else:
    print("Error executing command.")
    print("Error message:")
    print(result.stderr)

# Create a Tkinter window
window = tk.Tk()
window.title(
    "Simple Docker Command Center (for people who constantly forget CLI commands), v0.1"
)

# Add widgets and functionality...

# Start the Tkinter event loop
window.mainloop()
