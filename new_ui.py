import tkinter
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="Admin@123")
cur=con.cursor(buffered="True")

try:
  cur.execute("USE Register")
except:
  cur.execute("CREATE DATABASE Register")
  cur.execute("USE Register")

try:
  cur.execute("DESC Student")
except:
  cur.execute("CREATE TABLE Student(ID INT PRIMARY KEY,NAME VARCHAR(20),GENDER VARCHAR(6),EMAIL VARCHAR(30),MOBILE VARCHAR(12))")

def Register():
  cur.execute(f"INSERT INTO Student Values('{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}','{e6.get()}')")
  con.commit()


win=tkinter.Tk()
win.geometry("300x300")
win.title("Student Registration Portal")

L1=tkinter.Label(win,text="Student Details : ")
L2=tkinter.Label(win,text="ID")
L3=tkinter.Label(win,text="NAME")
L4=tkinter.Label(win,text="GENDER")
L5=tkinter.Label(win,text="EMAIL")
L6=tkinter.Label(win,text="MOBILE NO")

#PLACE ,PACK ,GRID
L1.grid(row=1,column=1)
L2.grid(row=3,column=1)
L3.grid(row=4,column=1)
L4.grid(row=5,column=1)
L5.grid(row=6,column=1)
L6.grid(row=7,column=1)

e2=tkinter.Entry(win)
e3=tkinter.Entry(win)
e4=tkinter.Entry(win)
e5=tkinter.Entry(win)
e6=tkinter.Entry(win)

e2.grid(row=3,column=2)
e3.grid(row=4,column=2)
e4.grid(row=5,column=2)
e5.grid(row=6,column=2)
e6.grid(row=7,column=2)

b=tkinter.Button(win,text="Submit Here",command=Register)
b.grid(row=8,column=2)
win.mainloop()