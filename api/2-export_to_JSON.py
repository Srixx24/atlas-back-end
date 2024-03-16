#!/usr/bin/python3
"""
Retrieves employee data from a REST API
in JSON format and displays info.
"""
import json
import requests
import sys


def export_json_data(tasks, user_id, employee_name):
    filename = f"{user_id}.json"

    tasks = [
        {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        }
        for task in tasks
    ]

    info = {"USER_ID": user_id, "tasks": info}

    with open(filename, "w") as json_file:
        json.dump(tasks, json_file, indent=4)

    print(f"Data has been written to user_id.json")


def read_json_data(filename):
    with open(filename, "r") as json_file:
        json_object = json.load(json_file)

    print(json_object)


def get_employee_list(id):
    name_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    response_name = requests.get(name_url)
    response_todo = requests.get(todo_url)

    if response_name.status_code == 200 and response_todo.status_code == 200:
        employee_data = response_name.json()
        tasks = response_todo.json()

        employee_name = employee_data['name']
        export_json_data(id, employee_name, tasks)
    else:
        print("Failed to retrieve data.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: 2-export_to_JSON.py <tasks> <user_id> <employee_name>")
        sys.exit(1)

    tasks = sys.argv[1]
    user_id = sys.argv[2]
    employee_name = sys.argv[3]
    export_json_data(tasks, user_id, employee_name)
