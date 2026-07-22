# Print the multiplication tables from 1 to 10.

for table in range(1, 11):
    print("Table of", table)

    for i in range(1, 11):
        print(table, "*", i, "=", table * i)

    print() 