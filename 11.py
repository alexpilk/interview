import requests


def get_todo_item(item_id):
    return requests.get(f'https://jsonplaceholder.typicode.com/todos/{item_id}').json()


def get_first_todo_item():
    return get_todo_item(1)


print(get_first_todo_item())
