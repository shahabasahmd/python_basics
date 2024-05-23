import random

def ticket_number():
    return random.randint(0, 1000)

def info():
    cus_name = input("Enter customer name: ")
    project_name = input("Enter project name: ")
    ticket_num = ticket_number()
    issue = input("enter the problem : ")
    print("ticket number is ", ticket_num)
    return ticket_num, cus_name, project_name,issue

def print_all_info():

    customers = []

    while True:
        ticket_num, cus_name, project_name, issue = info()
        customers.append((ticket_num, cus_name, project_name, issue))
        exit_input = input("Enter 'exit' to exit or press Enter to continue: ")
        if exit_input == 'exit':
            break

    print("\nCustomer Details:")
    for ticket_num, cus_name, project_name, issue in customers:
        print("Ticket Number:", ticket_num)
        print("Customer Name:", cus_name)
        print("Project Name:", project_name)
        print("The issue is :", issue)
        print()

print_all_info()


