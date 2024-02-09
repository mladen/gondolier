# Update the table with the result
def update_table(rows, treeview):
    # Clear previous table data
    for i in treeview.get_children():
        treeview.delete(i)

    # Insert new rows into the table
    for row in rows:
        treeview.insert("", "end", values=row)
