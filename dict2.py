import random

unique_ticket_number = set()
def geneterate_unique_ticket_number():

    while True:
        ticket_number = random.randint(1,1000)
        if ticket_number not in unique_ticket_number:
            unique_ticket_number.add(ticket_number)
            return ticket_number




n = int(input("Enter the Total number aof Customers   : "))
customers_data = {}

for _ in range(n):
    projects = []
    cus_name = input("Enter the name of Customer : ")
    m = int(input("Enter number of projects  :  "))
    for _ in range(m):
        proj_name = input("Enter the name of the project : ")
        prob = input("Enter the probelm : ")
        ticket_number = geneterate_unique_ticket_number()
        print(ticket_number)
        project_data = {'project name':proj_name,'problem':prob,'ticket number':ticket_number}
        projects.append(project_data)

    customers_data[cus_name] = projects
print(customers_data)
print(unique_ticket_number)



