import subprocess
from window_manager import window


# EXECUTING A COMMAND IN A TERMINAL
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

# Start the Tkinter event loop
window.mainloop()
