import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cmd = """
    CREATE TABLE IF NOT EXISTS STUDENT(
    fullname text not null,
    usn varchar(10) primary key ,
    branch text not null,
    sem integer not null,
    CGPA integer not null
)
"""

cursor.execute(cmd)
connection.commit()

cmd = "INSERT INTO STUDENT(fullname,usn,branch,sem,CGPA)values(?,?,?,?,?)"
cursor.execute(cmd,('Shreya','4mw23ad046','AIDS','5','9'))

connection.commit()

f=cursor.execute("SELECT * FROM STUDENT").fetchall()
print(f)

r = cursor.execute("select * from STUDENT where fullname = ?",('Spoorthi',)).fetchall()
print(r)

connection.close()