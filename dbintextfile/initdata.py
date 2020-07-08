# инициализация данных для последующего созранения в файлах

# записи
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
alex = dict(name='Alex Mal', age=31, pay=40000, job='spec')
slav = dict(name='Slav S', age=33, pay=50000, job='dev')
yuri = dict(name='Yuri Ivanov', age=45, pay=70000, job='proffesional')

# база данных
db = {}
db['bob'] = bob
db['alex'] = alex
db['slav'] = alex
db['yuri'] = yuri

if __name__ == '__main__':  # если запускатся как сценарий, то выводит все записи из БД
    for key in db:
        print(key, '=>', db[key])
