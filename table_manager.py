# Update the table with the result
def update_table(rows, treeview):
    # Clear previous table data
    for i in treeview.get_children():
        treeview.delete(i)

    # Skip the first row (column headers) and insert remaining rows into the table
    for row in rows[1:]:
        treeview.insert("", "end", values=row)
