new_employees = {
    'accountant': 'Alice',
    'janitor': None,
    'developer': 'Bob',
    'manager': object()
}


def filter_employees(employees):
    x = {}
    for i in employees:
        if employees[i] == None:
            continue
        if type(employees[i]) != str:
            continue
        x[i] = employees[i]
    return x


print(filter_employees(new_employees))
