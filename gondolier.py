import tkinter as tk
from tkinter import ttk

# import window_manager
import commands_manager
import style


def main():
    # WINDOW
    window = tk.Tk()  # Create the window
    window.title("Docker Container Manager")

    # window_manager.center_window(window)  # Center the window on the screen
    window.configure(bg="#0091E5")  # Set background color to light blue

    frame_with_left_menu = tk.Frame(window, bg="#0091E5")  # Frame belongs to the window
    frame_with_left_menu.pack(fill=tk.Y, side=tk.LEFT, expand=False)
    # frame_with_left_menu.configure(bg="#0091E5")  # Set background color to light blue

    # Add a home button to the frame_with_left_menu
    button_to_home = ttk.Button(
        frame_with_left_menu,
        text="Home",
        command=lambda: commands_manager.execute_command("docker ps"),
    )
    button_to_home.pack(side=tk.TOP, padx=5, pady=5)

    # Add button to the frame_with_left_menu
    button_to_display_images_table = ttk.Button(
        frame_with_left_menu,
        text="Images",
        command=lambda: commands_manager.execute_command("docker ps"),
    )
    button_to_display_images_table.pack(side=tk.TOP, padx=5, pady=5)

    button_to_display_containers_table = ttk.Button(
        frame_with_left_menu,
        text="Containers",
        command=lambda: commands_manager.execute_command("docker ps"),
    )
    button_to_display_containers_table.pack(side=tk.TOP, padx=5, pady=5)

    button_to_display_volumes_table = ttk.Button(
        frame_with_left_menu,
        text="Volumes",
        command=lambda: commands_manager.execute_command("docker volume ls"),
    )
    button_to_display_volumes_table.pack(side=tk.TOP, padx=5, pady=5)

    # Create a Frame to hold widgets; the frame belongs to the window
    frame_with_list = tk.Frame(window, bg="#0091E5")  # Frame belongs to the window
    frame_with_list.pack(fill=tk.BOTH, expand=True)
    # frame_with_list.configure(bg="#0091E5")  # Set background color to light blue
    # frame_with_list.pack(fill=tk.BOTH, expand=True)
    # frame_with_list.config(relief=tk.RAISED, padding="10")

    # Add a label to the frame_with_list
    label = ttk.Label(
        frame_with_list, text="Here's the list of all the containers on your machine!"
    )
    label.pack(side=tk.TOP, pady=10)

    # STYLES (from style.py)
    style.configure_styles(ttk)  # Configure the styles for the widgets

    # TABLE
    # Create a Treeview widget to display the result
    columns = (
        "Container ID",
        "Image",
        "Command",
        "Created",
        "Size",
        "Status",
        "Names",
        "Ports",
    )
    treeview = ttk.Treeview(frame_with_list, columns=columns, show="headings")

    # Set column headings
    for col in columns:
        treeview.heading(col, text=col)

    # Pack the Treeview widget
    treeview.pack(side=tk.BOTTOM, fill="both", expand=True)

    # BUTTONS
    # Button for listing running containers
    button_to_list_running_containers = ttk.Button(
        window,
        text="List Running Containers",
        command=lambda: commands_manager.execute_command("docker ps", treeview),
    )
    button_to_list_running_containers.pack(
        side=tk.LEFT, padx=5, pady=10
    )  # Pack the first button to the left

    # Button for listing all containers (running and stopped)
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
    # Size:
    # - https://docs.docker.com/storage/storagedriver/#container-size-on-disk
    # - https://docs.docker.com/engine/reference/commandline/container_ls/#size
    commands_manager.execute_command(
        "docker ps -a --format 'table {{.ID}}\t{{.Image}}\t{{.Command}}\t{{.CreatedAt}}\t{{.Size}}\t{{.Status}}\t{{.Names}}\t{{.Ports}}'",
        treeview,
    )

    # Run the Tkinter event loop
    window.mainloop()


if __name__ == "__main__":
    main()
