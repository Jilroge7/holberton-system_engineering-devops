#!/usr/bin/python3
""" Exports a emp from a REST API to CSV """
if __name__ == "__main__":
    import csv
    import requests
    import sys

    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        user_id).json()
    u_name = user.get("username")
    url = 'https://jsonplaceholder.typicode.com/todos/?userId='
    tasks = requests.get(url + user_id).json()

    with open('{}.csv'.format(user_id), 'w', newline='') \
            as csvFile:
        writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, u_name,
                            task.get("completed"),
                            task.get("title")])
