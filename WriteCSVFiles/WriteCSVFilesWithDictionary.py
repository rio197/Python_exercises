import csv

users = [{"name":"SolMansi", "username": "solm", "department":  "IT infrastructure"},{"name":"Lio Nelson", "username": "lion", "department":  "User Experience Research"},{"name":"Charlie Grey", "username": "greyc", "department":  "Development"}]

keys = ["name", "username", "department"]

with open('by_department.csv', 'w', newline='', encoding='utf-8') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
