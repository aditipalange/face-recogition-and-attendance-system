import mysql.connector

conn = mysql.connector.connect(user='root', password='aditi',host='localhost',database='face_recognition',port=3307)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()