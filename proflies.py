from faker import Faker

fake = Faker()

# Number of people to generate
num_people = 20

people = []

for _ in range(num_people):
    person = {
        'name': fake.name(),
        'username': fake.user_name(),
        'email': fake.email(),
        'address': fake.address(),
        'birthdate': fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d'),
        'job': fake.job(),
        'company': fake.company(),
        'phone_number': fake.phone_number(),
        'ssn': fake.ssn(),
    }
    people.append(person)

# for person in people:
#     print(person)
    
with open('people.txt', 'w') as file:
    for person in people:
        file.write(str(person) + '\n')

print("Data saved to 'people.txt'")