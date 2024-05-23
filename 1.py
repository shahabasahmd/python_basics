import random

unique_ticket_number = set()
def geneterate_unique_ticket_number():

    while True:
        ticket_number = random.randint(1, 1000)
        if ticket_number not in unique_ticket_number:
            unique_ticket_number.add(ticket_number)
            return ticket_number


company_projects = {}

while True:
    company_name = input("Enter the company name (or type 'exit' to finish): ")
    if company_name == 'exit':
        break

    projects = []
    while True:
        project_name = input("Enter a project name (or type 'done' to finish): ")
        if project_name == 'done':
            break
        projects.append(project_name)

    company_projects[company_name] = projects


n = int(input("Enter the number of customers "))
project_data = {}
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
    ticket_num = geneterate_unique_ticket_number()

    # Create or update project_data
    if project_name not in project_data:
        project_data[project_name] = []

    customer_details = {"name": cus_name, "ticket number": ticket_num, "issue": issue}
    project_data[project_name].append(customer_details)

    print(f"Ticket number generated: {ticket_num}")

    # Update company_projects
    if company_name not in company_projects:
        company_projects[company_name] = {}

    if project_name not in company_projects[company_name]:
        company_projects[company_name][project_name] = []

    company_projects[company_name][project_name].append(customer_details)

print(company_projects)

#
# for company, projects in company_projects.items():
#     print(f"Company: {company}")
#     for project in projects:     # list of project names
#         print(f"\tProject: {project}")
#         customers = company_projects[company][project]       # Get the customers for the project
#         for customer in customers:
#             print(f"\t\tCustomer Name: {customer['name']}")
#             print(f"\t\tTicket Number: {customer['ticket number']}")
#             print(f"\t\tIssue: {customer['issue']}")

#
# print(company_projects)