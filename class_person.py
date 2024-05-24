from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        # date_of_birth is in the format 'YYYY-MM-DD'
        dob = datetime.strptime(self.date_of_birth, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age


person1 = Person("John Doe", "USA", "1990-05-24")
print(person1.calculate_age())
