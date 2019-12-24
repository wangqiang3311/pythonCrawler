import sqlite3
con=sqlite3.connect('d:/test.db')
cur=con.cursor()
cur.execute('create table person(id integer primary key,name varchar(20),age integer)')
cur.execute(' insert into person Values(?,?,?)',(1,'wbq',20))
con.commit()
cur.execute('select * from person')
res=cur.fetchall()
for line in res:
    print(line)
