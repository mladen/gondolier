def configure_styles(ttk):
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
        "TLabel",
        background="#0091E5",  # #394246
        foreground="white",
    )

    style.configure(
        "Treeview",
        background="#0091E5",
        foreground="white",
        rowheight=25,
        bordercolor="#0091E5",
        fieldbackground="#0091E5",
    )
