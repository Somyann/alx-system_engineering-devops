#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

def get_employee_name(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    response.raise_for_status()
    user_data = response.json()
    return user_data.get("username")

def get_employee_todos(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    response.raise_for_status()
    todos = response.json()
    return todos

def write_to_csv(employee_id, username, todos):
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([employee_id, username, todo.get("completed"), todo.get("title")])

