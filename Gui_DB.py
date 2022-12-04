import tkinter              #for gui apps
import mysql.connector      #establishing connection btw py and sql

#temp var to store connection 
con=mysql.connector.connect(host="localhost", user="root",password="Admin@123") 
cur=con.cursor(buffered=True)

try:
  cur.execute("use registration")
except:
  cur.execute("CREATE DATABASE registration")
  cur.execute("use registration")

try:    # to avoid table creation in every run
  cur.execute("DESC persons")
except:
  cur.execute("CREATE TABLE persons(ID INT PRIMARY KEY AUTO_INCREMENT, NAME VARCHAR(20), AGE INT ,GENDER VARCHAR(6) , EMAIL VARCHAR(40), MOBILE VARCHAR(10))")

def Registration():       #This function will store all values to database
  cur.execute(f"INSERT INTO PERSONS(NAME,AGE,GENDER,EMAIL,MOBILE) VALUES ('{e1.get()}','{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}')" )
  con.commit()


win=tkinter.Tk()            #window frame win
win.geometry("400x400")
win.title("Person registration portal")
l1=tkinter.Label(win,text="Person Details")
l2=tkinter.Label(win,text="Name")
l3=tkinter.Label(win,text="Age")
l4=tkinter.Label(win,text="Gender")
l5=tkinter.Label(win,text="Email")
l6=tkinter.Label(win,text="Mobile Number")

# tkinter has 3 layout manager place(x-y axis),pack(horizontal/vertical),grid(row/col)
l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l4.grid(row=4,column=1)
l5.grid(row=5,column=1)
l6.grid(row=6,column=1)

# entry boxes for entry
e1=tkinter.Entry(win)
e2=tkinter.Entry(win)
e3=tkinter.Entry(win)
e4=tkinter.Entry(win)
e5=tkinter.Entry(win)

# to show all entries in grid
e1.grid(row=2,column=2)
e2.grid(row=3,column=2)
e3.grid(row=4,column=2)
e4.grid(row=5,column=2)
e5.grid(row=6,column=2)

#submit button
b=tkinter.Button(win, text="Submit Here", command=Registration)
b.grid(row=7,column=2)

win.mainloop()