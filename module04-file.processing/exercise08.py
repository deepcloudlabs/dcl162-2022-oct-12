import csv

with open("employees.csv", mode="wt", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(employees)
