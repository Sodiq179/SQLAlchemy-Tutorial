#!/usr/bin/python3

## Libraries
from sqlalchemy import create_engine

## connection url
connection_url = "mysql+mysqldb://sqlalchemy_user:sqlalchemy_pwd@localhost/sqlalchemy_db"

## Engine
engine = create_engine(connection_url)

print(engine)

print("----------------------------------------------------------")
print("----------------------------------------------------------")

## Query string
query_1 =  "SELECT stud_id, stud_name FROM students WHERE stud_id=3"

## Engine execution
result = engine.execute(query_1)

print(result.fetchone())
result.close()

print("----------------------------------------------------------")
print("----------------------------------------------------------")

## Query string
query_2 =  "SELECT * FROM students"

## Engine execution
result = engine.execute(query_2)

print(result.fetchall())
result.close()

print("----------------------------------------------------------")
print("----------------------------------------------------------")
## result object can also be iterated
result = engine.execute(query_2)
for row in result:
    print(row)


## Insert value into the table
print("----------------------------------------------------------")
print("----------------------------------------------------------")
query_3 = "INSERT INTO students VALUES (4, 'Omiwade Nifemi')"
engine.execute(query_3)
