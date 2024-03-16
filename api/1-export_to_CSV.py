#!/usr/bin/python3
"""
Retrieves employee data from a REST API
in CSV format displays info.
"""
import csv
import requests
import sys


def export_csv_data(tasks, user_id, employee_name):
    filename = f"{user_id}.csv"

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "USER_ID", 
            "USERNAME", 
            "TASK_COMPLETED_STATUS", 
            "TASK_TITLE"
            ])
        
        for task in tasks:
            task_id = task['id']
            task_title = task['title']
            task_completed = task['completed']
            task_status = "COMPLETED" if task_completed else "NOT COMPLETED"

            writer.writerow([user_id, employee_name, task_status, task_title])

        print(f"Data has been written to USER_ID.csv")


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

        print(f"Employee {employee_name} is done with tasks"
              f"({len(completed_tasks)}/{total_tasks}):")
        print(f"EMPLOYEE_NAME:{employee_name}")
        print(f"NUMBER_OF_DONE_TASKS:{len(completed_tasks)}")
        print(f"TOTAL_NUMBER_OF_TASKS:{total_tasks}")
        print("Completed Task Titles:")
        for title in completed_tasks:
            print(f"\t{title}")
    else:
        print("Failed to retrieve data.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: 1-export_to_CSV.py <tasks> <user_id> <employee_name>")
        sys.exit(1)

    tasks = sys.argv[1]
    user_id = sys.argv[2]
    employee_name = sys.argv[3]
    export_csv_data(tasks, user_id, employee_name)
