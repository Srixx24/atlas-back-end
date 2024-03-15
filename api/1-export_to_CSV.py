#!/usr/bin/python3
"""
Retrieves employee data from a REST API
in CSV format displays info.
"""
import csv
import requests
import sys


def export_csv_data(id):
    name_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    response_name = requests.get(name_url)
    response_todo = requests.get(todo_url)

    if response_name.status_code == 200 and response_todo.status_code == 200:
        employee_data = response_name.json()
        todos = response_todo.json()

        employee_name = employee_data['username']
        employee_id = employee_data['id']

        tasks = [
            {
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": todo['completed'],
                "TASK_TITLE": todo['title']
            }
            for todo in todos
        ]

        csv_filename = f"{id}.csv"
        with open(csv_filename, 'w', newline='') as csvfile:
            fields = [
                'USER_ID',
                'USERNAME',
                'TASK_COMPLETED_STATUS',
                'TASK_TITLE'
                ]
            csvwriter = csv.DictWriter(csvfile, fields)
            csvwriter.writeheader()
            csvwriter.writerows(tasks)

        print(f"Data has been written to USER_ID.csv")

    else:
        print("Failed to retrieve data.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 1-export_to_CSV.py <id>")
        sys.exit(1)

    id = sys.argv[1]
    export_csv_data(id)
