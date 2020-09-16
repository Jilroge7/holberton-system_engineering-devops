#!/usr/bin/python3
""" Exports a emp from a REST API to JSON """
if __name__ == "__main__":
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    u_name = user.get("username")
    url = 'https://jsonplaceholder.typicode.com/todos/?userId='
    tasks = requests.get(url + user_id).json()
    jlist = []
    ldict = {}
    for task in tasks:
        jdict = {}
        jdict["task"] = task.get("title")
        jdict["completed"] = task.get("completed")
        jdict["username"] = u_name
        jlist.append(jdict)
    ldict[user_id] = jlist

    with open('{}.json'.format(user_id), 'w') as f:
        fil = json.dumps(ldict)
        f.write(fil)
