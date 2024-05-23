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
    # Initialize project_data[company_name] as an empty dictionary
    if company_name not in all_data:
        all_data[company_name] = {}

n = int(input("Enter the number of customers: "))

for _ in range(n):
    cus_name = input("Enter the name of the customer: ")
    company_name = input("Enter the company name: ")

    if company_name not in company_projects:
        print("There is no such company.")
        continue

    project_name = input("Enter the project name: ")
    if project_name not in company_projects[company_name]:
        print("There is no such project in that company.")
        continue

    issue = input("Enter the issue: ")
    ticket_num = generate_unique_ticket_number()

    # Ensure that project_data[company_name][project_name] exists
    if project_name not in all_data[company_name]:
        all_data[company_name][project_name] = []

    # Append customer details to the list of customers for the project
    customer_details = {"name": cus_name, "ticket number": ticket_num, "issue": issue}
    all_data[company_name][project_name].append(customer_details)

    print(f"Ticket number generated: {ticket_num}")

print(company_projects)
print(all_data)
for company, projects in all_data.items():
    print(f"Company: {company}")
    for project, customers in projects.items():
        print(f"\tProject: {project}")
        for customer in customers:
            print(f"\t\tCustomer Name: {customer['name']}")
            print(f"\t\tTicket Number: {customer['ticket number']}")
            print(f"\t\tIssue: {customer['issue']}")
