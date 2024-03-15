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

    response_name = requests.get(name_url)

    if response_name.status_code == 200:
        employee_data = response_name.json()

        employee_name = employee_data['username']
        employee_id = employee_data['id']

        tasks = [{
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": "completed",
                "TASK_TITLE": "title"
            }]

        # Start of csv file
        filename = "USER_ID.csv"
        fields = [
                'USER_ID',
                'USERNAME',
                'TASK_COMPLETED_STATUS',
                'TASK_TITLE'
                ]

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(tasks)

        print(f"Data has been written to USER_ID.csv")

    else:
        print("Failed to retrieve data.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 1-export_to_CSV.py <id>")
        sys.exit(1)

    id = sys.argv[1]
    export_csv_data(id)
