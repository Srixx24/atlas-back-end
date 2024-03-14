#!/usr/bin/python3
"""
Retrieves employee data from a REST API and
displays info on TODO list progress.
"""
import requests
import sys


def get_employee_list(id):
    name_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    response_name = requests.get(name_url)
    response_todo = requests.get(todo_url)

    if response_name.status_code == 200 and response_todo.status_code == 200:
        employee_data = response_name.json()
        todos = response_todo.json()

        employee_name = employee_data['name']
        total_tasks = len(todos)
        completed_tasks = [
            todo['title']
            for todo in todos
            if todo['completed']
        ]

        print(f"Employee {employee_name} is done with tasks "
              f"({completed_tasks}/{total_tasks}):")
        print(f"EMPLOYEE_NAME:\t{employee_name}")
        print(f"NUMBER_OF_DONE_TASKS:\t{len(completed_tasks)}")
        print(f"TOTAL_NUMBER_OF_TASKS:\t{total_tasks}")
        print("Completed Task Titles:")
        for title in completed_tasks:
            print(f"\t{title}")
    else:
        print("Failed to retrieve data.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 0-gather_data_from_an_API.py <id>")
        sys.exit(1)

    id = sys.argv[1]
    get_employee_list(id)
