
import random
generated_ticket_number = set()
def generate_unique_ticket():

    while True:
        ticket_num = random.randint(1,100)
        if ticket_num not in generated_ticket_number:
            generated_ticket_number.add(ticket_num)
            return ticket_num

n = int(input("Enter the number of projects: "))
project_data = {}

for i in range(n):
    project_name = input(f"Enter the name of project: ")
    project_customers = []
    num_cus = int(input(f"Enter the number of customers for project {project_name}: "))

    for _ in range(num_cus):
        name = input("Enter the customer name: ")
        issue = input("Enter the issue: ")
        ticket_num = generate_unique_ticket()
        print("the ticket number is ", ticket_num)
        customer_details = {'name': name, 'issue': issue, 'ticket_number': ticket_num}
        project_customers.append(customer_details)

    project_data[project_name] = project_customers

for project_name, customers in project_data.items():
    print(f"Project: {project_name}")
    for customer in customers:
        print(f"  Customer Name: {customer['name']}, Issue: {customer['issue']},"
              f" Ticket Number: {customer['ticket_number']}")


