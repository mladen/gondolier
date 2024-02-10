import tkinter as tk
from tkinter import ttk
import window_manager
import commands_manager

# WINDOW
window = tk.Tk()  # Create the window
window.title("Docker Container Manager")

# window_manager.center_window(window)  # Center the window on the screen
window.configure(bg="#0091E5")  # Set background color to light blue

# Create a Frame to hold widgets
frame = tk.Frame(window, bg="#0091E5")
frame.pack(fill=tk.X, expand=True)
# frame.configure(bg="#0091E5")  # Set background color to light blue
# frame.pack(fill=tk.BOTH, expand=True)
# frame.config(relief=tk.RAISED, padding="10")

# Add widgets to the frame
label = ttk.Label(frame, text="Here's the list of all the containers on your machine!")
label.pack(side=tk.TOP, pady=10)
label.configure(background="#0091E5", foreground="white")

# STYLE
style = ttk.Style()

# Set the style of the Treeview
style.theme_use("clam")  # Set the theme to "aquativo"


# Set the background color for buttons, border color, border radius etc.
style.configure(
    "TButton",
    background="#394246",
    foreground="white",
    relief="flat",
)

style.configure(
    "Treeview",
    background="#394246",
    foreground="white",
    rowheight=25,
    bordercolor="#0091E5",
)

# TABLE
# Create a Treeview widget to display the result
columns = ("Container ID", "Image", "Command", "Created", "Status", "Names", "Ports")
treeview = ttk.Treeview(frame, columns=columns, show="headings")

# Set column headings
for col in columns:
    treeview.heading(col, text=col)


# Pack the Treeview widget
treeview.pack(side=tk.BOTTOM, fill="both", expand=True)

# BUTTON FOR LISTING RUNNING CONTAINERS
button_to_list_running_containers = ttk.Button(
    window,
    text="List Running Containers",
    command=lambda: commands_manager.execute_command("docker ps", treeview),
)
button_to_list_running_containers.pack(
    side=tk.LEFT, padx=5, pady=10
)  # Pack the first button to the left

# BUTTON FOR LISTING ALL CONTAINERS (not just running ones)
button_to_list_all_containers = ttk.Button(
    window,
    text="List All Containers",
    command=lambda: commands_manager.execute_command("docker ps -a", treeview),
)
button_to_list_all_containers.pack(
    side=tk.LEFT, padx=5, pady=10
)  # Pack the second button to the left next to the first button


# LOAD THE TABLE ON START
# commands_manager.execute_command("docker ps -a", treeview)
commands_manager.execute_command(
    "docker ps -a --format 'table {{.ID}}\t{{.Image}}\t{{.Command}}\t{{.CreatedAt}}\t{{.Status}}\t{{.Names}}\t{{.Ports}}'",
    treeview,
)


# Run the Tkinter event loop
window.mainloop()
