import random


unique_ticket_number = set()
def geneterate_unique_ticket_number():

    while True:
        ticket_number = random.randint(1,1000)
        if ticket_number not in unique_ticket_number:
            unique_ticket_number.add(ticket_number)
            return ticket_number


company_names = []
while True:
    name = input("Enter the name of companies :")
    company_names.append(name)
    add_company = input("Do yo wish to add the new comapny press enter for add or enter 'no' continue without adding new company  : ")
    if add_company == 'no':
        break




data = {}
n = int(input("Enter the number of customers : "))
for _ in range(n):
    customers = []
    cus_name = input("Enter the Name of customer  : ")
    company_name = input("Enter the company name  : ")

    if company_name not in company_names:
        add_company = input("The company name does not exist in the list. Do you want to add it? Press Enter to add or enter 'no' to continue without adding: ")
        if add_company.lower() != 'no':
            company_names.append(company_name)
        else:
            continue


    ticket_number = geneterate_unique_ticket_number()
    issue = input("Enter the problem : ")
    custom_details = {'name':cus_name,'ticket number':ticket_number,'issue':issue}
    customers.append(custom_details)

    data[company_name] = customers


print(data)






