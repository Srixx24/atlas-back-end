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

    tasks = {
        str(user_id): [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
            }
            for task in tasks
        ]
    }

    # json_object = json.dumps(tasks, indent=4)

    with open(filename, "w") as json_file:
        # json_file.write(json_object)
        json.dump(tasks, json_file, indent=4)


print(f"Data has been written to user_id.json")


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
    if len(sys.argv) != 2:
        print("Usage: 2-export_to_JSON.py <id>")
        sys.exit(1)

    id = sys.argv[1]
    get_employee_list(id)
