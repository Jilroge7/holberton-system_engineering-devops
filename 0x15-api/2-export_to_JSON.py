#!/usr/bin/python3
""" Return todo list progress for a emp from a REST API """
if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    employees = requests.get('https://jsonplaceholder.typicode.com/users/' +
                             user_id).json()
    emp_name = (employees.get("name"))
    url = 'https://jsonplaceholder.typicode.com/todos/?userId='
    tasks = requests.get(url + user_id).json()
    tasks_done = []
    for task in tasks:
        if (task.get("completed")) is True:
            tasks_done.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
          emp_name, len(tasks_done), len(tasks)))
    for d_task in tasks_done:
        print("\t {}".format(d_task))
