import tkinter as tk
from tkinter import ttk


def center_window(app_window):
    app_window.update_idletasks()
    app_width = app_window.winfo_width()
    app_height = app_window.winfo_height()
    screen_width = app_window.winfo_screenwidth()
    screen_height = app_window.winfo_screenheight()
    # print(f"App Width: {app_width}, App Height: {app_height}")
    # print(f"Screen Width: {screen_width}, Screen Height: {screen_height}")

    x = (screen_width - app_width) // 4
    y = (screen_height - app_height) // 4
    # print(f"X: {x}, Y: {y}")
    app_window.geometry(f"{app_width}x{app_height}+{x}+{y}")


# https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/

# Create the Tkinter window
window = tk.Tk()
window.title("Centered Window")

# Create a Frame to hold widgets
frame = ttk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True)

# Add widgets to the frame
label = ttk.Label(frame, text="The list of images goes here!")
label.pack(pady=10)

# Center the window on the screen
center_window(window)
