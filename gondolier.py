import tkinter as tk
from tkinter import ttk
import window_manager
import commands_manager

# WINDOW
window = tk.Tk()  # Create the window
window.title("Docker Container Manager")

window_manager.center_window(window)  # Center the window on the screen


# Create a Frame to hold widgets
frame = ttk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True)

# Add widgets to the frame
label = ttk.Label(frame, text="The list of images goes here!")
label.pack(pady=10)

# TABLE
# Create a Treeview widget to display the result
columns = ("Container ID", "Image", "Command", "Created", "Status")
treeview = ttk.Treeview(window, columns=columns, show="headings")

# Set column headings
for col in columns:
    treeview.heading(col, text=col)


# Pack the Treeview widget
treeview.pack(fill="both", expand=True)

# BUTTON
execute_button = ttk.Button(
    window,
    text="Execute Docker PS",
    command=lambda: commands_manager.execute_command("docker ps -a", treeview),
)
execute_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
