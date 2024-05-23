import random

generated_ticket_number = set()
def generate_unique_ticket():

    while True:
        ticket_number = random.randint(1,100)
        if ticket_number not in generated_ticket_number:
            generated_ticket_number.add(ticket_number)
            return ticket_number



n = int(input("enter the project number "))
project_data ={}

for _ in range(n):
    customers =[]
    project_name = input(f"Enter the name of project : ")
    num_cus = int(input("enter the number of customers: "))

    for _ in range(num_cus):
        name = input("enter the name:  ")
        issue = input("enter the issue : ")
        ticket_number = generate_unique_ticket()
        print(ticket_number)
        customer_details = {'name':name,'issue':issue,'ticket number':ticket_number}
        customers.append(customer_details)

    project_data[project_name]=customers
print(generated_ticket_number)
for project_name, customers in project_data.items():
    print(f"Project: {project_name}")
    for customer in customers:
        print(f"  Customer Name: {customer['name']}")
        print(f"  Issue: {customer['issue']}")
        print(f"  Ticket Number: {customer['ticket number']}")
    print()




