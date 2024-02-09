# import tkinter as tk
# from tkinter import ttk


def center_window(app_window):
    app_window.update_idletasks()
    app_width = app_window.winfo_width()
    app_height = app_window.winfo_height()
    screen_width = app_window.winfo_screenwidth()
    screen_height = app_window.winfo_screenheight()

    # Calculate new width and height as 2/3 of the screen dimensions
    new_width = int(screen_width / 4)
    new_height = int(screen_height * 2 / 3)
    print(f"new_width, new_height: {new_width}, {new_height}")

    # Calculate new x and y coordinates to center the window
    x = (screen_width - new_width) // 2
    y = (screen_height - new_height) // 2

    # Update the window geometry with the new dimensions and position
    app_window.geometry(f"{new_width}x{new_height}+{x}+{y}")


# https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/
