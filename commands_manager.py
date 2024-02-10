import subprocess
import table_manager
import re  # Import the regular expression module


def execute_command(command=None, treeview=None):
    # Define the terminal command to execute
    if command is None:
        command = "docker ps"

    # Execute the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Check the result
    if result.returncode == 0:
        print("Command executed successfully.")
        print("Output:")
        print(result.stdout)

        # Parse the output into rows
        # Split each line using a regular expression to split on multiple spaces
        rows = [re.split(r"\s{2,}", line) for line in result.stdout.strip().split("\n")]
        for row in rows:
            print(row)

        # Update the table with the result
        table_manager.update_table(rows, treeview)
    else:
        print("Error executing command.")
        print("Error message:")
        print(result.stderr)
