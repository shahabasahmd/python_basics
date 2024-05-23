import random

unique_ticket_number = set()


def generate_unique_ticket_number():
    while True:
        ticket_number = random.randint(1, 1000)
        if ticket_number not in unique_ticket_number:
            unique_ticket_number.add(ticket_number)
            return ticket_number


company_projects = {}
all_data = {}

while True:
    company_name = input("Enter the company name (or type 'exit' to finish): ")
    if company_name == 'exit':
        break

    projects = {}
    while True:
        project_name = input("Enter a project name (or type 'done' to finish): ")
        if project_name == 'done':
            break
        projects[project_name] = []
    company_projects[company_name] = projects
    # check that all_data[company_name] exists
    if company_name not in all_data:
        all_data[company_name] = {}

n = int(input("Enter the number of customers: "))


for _ in range(n):
    cus_name = input("Enter the name of the customer: ")
    company_name = input("Enter the company name: ")

    if company_name not in company_projects:
        input_text = input(
            "There is no such company, press enter to add new company or enter 'no' continue without adding : ")
        if input_text != 'no':
            # Add the new company and its projects
            projects = {}
            while True:
                project_name = input("Enter a project name for the new company (or type 'done' to finish): ")
                if project_name == 'done':
                    break
                projects[project_name] = []
            company_projects[company_name] = projects

            # check that all_data[company_name] exists
            if company_name not in all_data:
                all_data[company_name] = {}
        else:
            continue

    project_name = input("Enter the project name: ")
    if project_name not in company_projects[company_name]:
        print("There is no such project in that company.")
        continue

    issue = input("Enter the issue: ")
    ticket_num = generate_unique_ticket_number()

    if cus_name not in all_data[company_name]:
        all_data[company_name][cus_name] = []

    customer_details = {"project name": project_name, "ticket number": ticket_num, "issue": issue}
    all_data[company_name][cus_name].append(customer_details)

    print(f"Ticket number generated: {ticket_num}")


for company, projects in all_data.items():
    print(f"Company: {company}")
    for customer, details in projects.items():
        print(f"\tCustomer Name: {customer}")
        for detail in details:
            print(f"\t\tProject Name: {detail['project name']}")
            print(f"\t\tTicket Number: {detail['ticket number']}")
            print(f"\t\tIssue: {detail['issue']}")

print(company_projects)
