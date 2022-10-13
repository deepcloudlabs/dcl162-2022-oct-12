import csv

employees = [
    ["1", "jack bauer", 100000, "tr1"],
    ["2", "kate austen", 200000, "tr2"],
    ["3", "james sawyer", 300000, "tr3"],
    ["4", "sun kwon", 400000, "tr4"]
]

with open("employees.csv", mode="wt", newline='') as f:
    writer = csv.writer(f)
    # writer.writerows(employees)
    for employee in employees:
        writer.writerow(employee)
