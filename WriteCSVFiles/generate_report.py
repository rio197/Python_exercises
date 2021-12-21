#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
    """
    Takes a CSV file, registers a dialect, reads the CSV file and returns an employee list
    """
    with open(csv_file_location) as file:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        reader=csv.DictReader(file,dialect = 'empDialect')

        employee_list = []
        for row in reader:
            employee_list.append(row)

        return employee_list

def process_data(employee_list):
    """
    Takes the employee list built by read_employees() and does a count of the Department data
    """
    department_list = []

    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}

    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data

def write_report(dictionary, report_file):
    """
    Takes the dictionary built by process_data() and outputs it in a report, sorted by name of Department
    """
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()

employee_list=read_employees('/home/student-04-943baf78f04b/data/employees.csv')

dictionary = process_data(employee_list)

write_report(dictionary, '/home/student-04-943baf78f04b/test_report.txt')
