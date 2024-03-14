#!/usr/bin/python3
"""
Retrieves employee data from a REST API and
displays info on TODO list progress.
"""
import requests


def get_employee_list(id):
    name_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(name_url)
    employee_data = response.json()

    todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    response = requests.get(todo_url)
    todos = response.json()

    employee_name = employee_data['name']
    total_tasks = len(todos)
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]

    print(f"Employee {employee_name} is done with tasks "
          f"({len(completed_tasks)}/{total_tasks}):")
    print(f"EMPLOYEE_NAME:\t{employee_name}")
    print(f"NUMBER_OF_DONE_TASKS:\t{completed_tasks}")
    print(f"TOTAL_NUMBER_OF_TASKS:\t{total_tasks}")
    print("Completed Task Titles:")
    for title in completed_tasks:
        print(f"\t{title}")
