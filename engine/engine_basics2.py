#!/usr/bin/python3

## Libraries
from sqlalchemy import create_engine

## connection url
connection_url = "mysql+mysqldb://sqlalchemy_user:sqlalchemy_pwd@localhost/sqlalchemy_db"

## Engine
engine = create_engine(connection_url)

## Connection
conn = engine.connect()

## Transaction
trans = conn.begin()

## Queries
query_1 = "INSERT INTO students VALUES (4, 'Omiwade Nifemi')"
query_2 = "UPDATE students SET stud_name = 'Olayinka James' WHERE stud_id = 2"
query_3 = "INSERT INTO students VALUES (5, 'Adio Abdulhamid')"
query_4 = "DELETE FROM students WHERE stud_name= 'Micheal Henry'"

## Execution
conn.execute(query_1)
conn.execute(query_2)
conn.execute(query_3)
conn.execute(query_4)

## Commit
trans.commit()

## Closing connection
conn.close()
