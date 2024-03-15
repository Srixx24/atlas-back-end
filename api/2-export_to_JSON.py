#!/usr/bin/python3
"""
Retrieves employee data from a REST API
in JSON format and displays info.
"""
import json
import requests
import sys


def export_json_data(id):
    name_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    response_name = requests.get(name_url)
    response_todo = requests.get(todo_url)

    if response_name.status_code == 200 and response_todo.status_code == 200:
        employee_data = response_name.json()
        todos = response_todo.json()

        employee_name = employee_data['username']
        employee_id = employee_data['id']