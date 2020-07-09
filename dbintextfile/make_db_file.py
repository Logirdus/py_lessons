"""
Сохраняет в файл базу данных, находящуюся в оперативной памяти, используя
собственный формат записи: предполагается, что в данных отсутствуют строки:
'endrec', 'enddb' и '=>'; предполагается, что база даннх является словарем
словарей (см. сценарий инициализации initdata.py)
Структура записей проученных из оперативной памяти (т.е. из модуля initdata.py):
{
key1 {name=value, name2=value2, name3=value3, ...}
key2 {name=value,....}
}
"""

dbfilename = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = '=>'

def storeDbase (db, dbfilename=dbfilename):
    "сохраняет базу данных в файл"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()


if __name__ == '__main__':
    from initdata import db
    storeDbase(db)