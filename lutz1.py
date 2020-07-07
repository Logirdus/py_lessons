bob = ["Bob Smith",40, 30000, "developer"]
alex = ["Alex Zolotarev", 42, 50000, "spec"]

people = [bob, alex]
for person in people:
    print (person)
    print (person[0].split()[-1])
    print (person[2] * 2)

pays = [person[2] for person in people]
print(pays)

pays = map((lambda x: x[2]), people)
print(pays)

NAME, AGE, PAY, POST = range(4)

print (bob[NAME])

print('\nПопробуем словари\n')
#используем словари для создания базы
bob = {'name':'Bob Smith', 'age':40, 'pay':30000, 'job':'developer'}
alex = {'name':'Alex Mal', 'age':31, 'pay':50000, 'job':'spec'}
olga = dict(name='Olga Mal', age=25, pay=10000, job='spec')

people = [bob, alex]
people.append(olga)

for person in people:
    print(person['name'])

def get_name_age():
    for person in people:
        print(person['name'].split()[0], person['age'])


get_name_age()


def get_age(lastname):
    for person in people:
        if person['name'].split()[-1] == lastname:
            print(person['name'], person['age'])


get_age('Mal')

print('Hello')