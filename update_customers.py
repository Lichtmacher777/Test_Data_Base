import csv

def update_csv_row(file_name, row_number, column_name, new_value):


    with open(file_name, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

        rows[row_number][rows[0].index(column_name)] = new_value

    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


# Update the name of the person in the 1000th row of the CSV file.
update_csv_row("customers.csv", 1000, "name", "Lucky Customer")
