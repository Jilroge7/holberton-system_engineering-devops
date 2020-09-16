#!/usr/bin/python3
""" Exports all emp from a REST API to JSON """
if __name__ == "__main__":
    import json
    import requests
    import sys

    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    url = 'https://jsonplaceholder.typicode.com/todos/?userId='
    jlist = []
    ldict = {}
    for users in user:
        user_id = str(users.get("id"))
        tasks = requests.get(url + user_id).json()
        jlist = []
        for task in tasks:
            jdict = {}
            jdict["username"] = users.get("username")
            jdict["task"] = task.get("title")
            jdict["completed"] = task.get("completed")
            jlist.append(jdict)
        ldict[user_id] = jlist

    with open('todo_all_employees.json', 'w') as f:
        fil = json.dumps(ldict)
        f.write(fil)
