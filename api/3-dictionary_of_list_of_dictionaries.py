#!/usr/bin/python3
"""
Retrieves employee data from a REST API
in JSON format and displays info.
"""
import json
import requests
import sys


def export_all_json_data(tasks):
    filename = f"{todo_all_employees}.json"

    with open(filename, "w") as json_file:
        json.dump(data, json_file)

    print(f"Data has been written to {filename}")


def all_employees(id):
    name_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    response_name = requests.get(name_url)
    response_todo = requests.get(todo_url)

    if response_name.status_code == 200 and response_todo.status_code == 200:
        employee_data = response_name.json()
        tasks = response_todo.json()

        return employee_data, tasks
    else:
        print("Failed to retrieve employee data.")

    data = {}
    for task in tasks:
        user_id = task['userid']
        employee_name = task['username']
        all_data = {
            "username": employee_name,
            "task": task['title'],
            "completed": task['completed']
        }
        if user_id in all_data:
            all_data[user_id].append(all_data)
            all_data[task] = tasks
        else:
            data[user_id] = [all_data]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 3-dictionary_of_list_of_dictionaries.py <tasks>")
        sys.exit(1)

    tasks = sys.argv[1]
    export_all_json_data(tasks)
