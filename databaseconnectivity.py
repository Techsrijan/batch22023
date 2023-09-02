import pymysql

con=pymysql.connect(host='127.0.0.1',db='flower',user="root",password='')
print("Connection established")
mycursor=con.cursor()

# sql="create table login(username varchar(25),password varchar(8))"
# mycursor.execute(sql)
# print("table created")

# sqlins="insert into login(username,password) values('hum','tum')"
# mycursor.execute(sqlins)

sqlup="update login set password='nahipata' where username='hum'"
mycursor.execute(sqlup)
print('data updated')

con.commit() #dml to save data
print("data inserted")