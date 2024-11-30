from peewee import *

pg_db = PostgresqlDatabase('postgres', user='postgres', password='docker',
                           host='localhost', port=5432)
pg_db.connect()

# pg_db.execute_sql("ATTACH DATABASE ':memory:' AS cache;")


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = pg_db # This model uses the "people.db" database.

print('it worked')