#!/usr/bin/python3
""" Return todo list progress for a emp from a REST API """
if __name__ == "__main__":
    import csv
    import requests
    import sys


    employees = (requests.get('https://jsonplaceholder.typicode.com/users/')).json()
    # for employee in employees.json():
    if ((employee.get("id")) == (sys.argv[1])):
        emp_name = employee.get("name")

    tasks = requests.get('https://jsonplaceholder.typicode.com/(sys.argv[1])/todos')
    for task in tasks.json()
        print("Employee {} is done with tasks({}/{}):".format(
              emp_name, len(task), len(tasks.json())))
        if ((task.get("completed") == True):
            print("/t {}".format(task.get("title")))
