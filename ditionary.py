import random
generated_ticket_number = set()
def generate_unique_ticket():

    while True:
        ticket_number = random.randint(1,100)
        if ticket_number not in generated_ticket_number:
            generated_ticket_number.add(ticket_number)
            return ticket_number



n = int(input("Enter the number of projects: "))
project_list = []


for i in range(n):
    project_name = input(f"Enter the name of project : ")
    project_data = {'name': project_name, 'customers': []}
    num_cus = int(input(f"Enter the number of customers for project {project_name}: "))


    for _ in range(num_cus):
        name = input("Enter the customer name: ")
        issue = input("Enter the issue: ")
        ticket_number = generate_unique_ticket()
        print("the ticket number is ",ticket_number)
        customer_details = {'name': name, 'issue': issue, 'ticket_number': ticket_number}
        project_data['customers'].append(customer_details)
    project_list.append(project_data)


for project in project_list:
    print(f"Project: {project['name']}")
    for customer in project['customers']:
        print( f"Customer Name: {customer['name']}, Issue: {customer['issue']}, Ticket Number: {customer['ticket_number']}")
print(project_list)














