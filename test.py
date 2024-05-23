import random

unique_ticket_number = set()


def generate_unique_ticket_number():
    while True:
        ticket_num = random.randint(1, 1000)
        if ticket_num not in unique_ticket_number:
            unique_ticket_number.add(ticket_num)
            return ticket_num


data = {}
all_datas = {}

while True:
    company_name = input("Enter the company name or enter 'exit' to continue: ")
    if company_name == 'exit':
        break
    projects = {}
    while True:
        project_name = input("Enter the project name or 'done' to exit: ")
        if project_name == 'done':
            break
        projects[project_name] = []
    data[company_name] = projects

    # Ensure that all_datas[company_name] exists
    if company_name not in all_datas:
        all_datas[company_name] = {}

print(data)

n = int(input("Enter the number of customers: "))

for _ in range(n):
    customer_name = input("Enter the customer name: ")
    company_name = input("Enter the company name: ")

    if company_name not in data:
        input_text = input(
            "The entered company is not in the list. Press Enter to add it or 'no' to continue without adding: ")
        if input_text == 'no':
            continue
        projects = {}
        while True:
            project_name = input("Enter the project name for the new company (or 'done' to finish): ")
            if project_name == 'done':
                break
            projects[project_name] = []
        data[company_name] = projects

        # Ensure that all_datas[company_name] exists for the new company
        if company_name not in all_datas:
            all_datas[company_name] = {}

    project_name = input("Enter the project name: ")
    if project_name not in data[company_name]:
        print("There is no such project in this company.")
        continue

    issue = input("Enter the issue: ")
    ticket_number = generate_unique_ticket_number()
    print("The ticket number is", ticket_number)

    if customer_name not in all_datas[company_name]:
        all_datas[company_name][customer_name] = []

    details = {'project name': project_name, 'ticket number': ticket_number, 'issue': issue}
    all_datas[company_name][customer_name].append(details)

print(all_datas)

for i, j in all_datas.items():
    print("the company name : ", i)
    for k, l in j.items():
        print("\tthe customer name :", k)
        for m in l:
            print("\t\tproject : ", m['project name'])
            print("\t\tissue : ", m['issue'])
            print("\t\tticket number : ", m['ticket number'])
