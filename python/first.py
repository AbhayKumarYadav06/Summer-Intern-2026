# import sqlite3
# conn = sqlite3.connect('example.db')
# sql ="""CREATE TABLE IF NOT EXISTS employees (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     mob varchar(10),
#     email varchar(255)
# )"""
# conn.execute(sql)
# print("Table created successfully")
# conn.close()


# import sqlite3
# conn = sqlite3.connect('example.db')
# sql ='''
#         insert into employees (name, age, mob, email) values ('Abhay Kumar Yadav', 22, '1234567890', 'abhaykumaryadav@example.com'),
#          ('John Doe', 30, '0987654321', 'johndoe@example.com'),
#          ('Jane Smith', 28, '5555555555', 'janesmith@example.com'),
#         ('Emily Davis', 35, '1111111111', 'emilydavis@example.com')
# '''
# conn.execute(sql)
# conn.commit()
# conn.close()


# import sqlite3
# conn = sqlite3.connect('example.db')
# sql ='''
#         select * from employees
# '''
# res = conn.execute(sql)
# for row in res:
#     print(row)
# conn.commit()
# conn.close()

# import sqlite3
# conn = sqlite3.connect('example.db')
# sql ='''
#         delete from employees where id = 2
# '''
# conn.execute(sql)
# conn.commit()
# conn.close()

import sqlite3
conn = sqlite3.connect('example.db')
sql ='''
        update employees set name = 'Tanish pinjani' where id = 3
'''
conn.execute(sql)
conn.commit()
conn.close()