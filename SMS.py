from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import pymysql

m = Tk()

m.title("Student management system")
m.geometry("1370x700+0+0")
Label(m, text='First Name')
title =  Label(m,text="Student management system",bd=9,relief=GROOVE,font=("times new roman",50,"bold"),bg="blue",fg="black")
title.pack(side=TOP,fill=X)

#---------------------- ALL variables--------------------------- 
ROLL_NO_VAR = StringVar()
NAME_VAR = StringVar()
EMAIL_VAR= StringVar()
GENDER_VAR= StringVar()
CONTACT_VAR = StringVar()
DOB_VAR= StringVar()
ADDRESS_VAR=StringVar()
SEARCH_BY = StringVar()
SEARCH_TEXT = StringVar()


# ------------------------All function--------------

def add_students():
    con = pymysql.connect(host="localhost",user="root",password="",database="sms")
    
    if ROLL_NO_VAR.get() == "" or NAME_VAR.get() == "":
        
        messagebox.showerror("error","fill the empty field!!!")
    else:
    #    Creating a cursor object using the cursor() method
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(ROLL_NO_VAR.get(),
        NAME_VAR.get(),EMAIL_VAR.get(),GENDER_VAR.get(),CONTACT_VAR.get(),DOB_VAR.get(),text_address.get('1.0',END)))
        con.commit()
        fetch_data()
        clear()
        con.close()
        messagebox.showinfo("success","Record has been inserted")
def fetch_data():
    con = pymysql.connect(host="localhost",user="root",password="",database="sms")
    cur = con.cursor()
    cur.execute("select * from students") 
    rows = cur.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',END,values=row)
        con.commit()
    con.close()    
def clear():
        ROLL_NO_VAR.set("")
        NAME_VAR.set("")
        EMAIL_VAR.set("")
        GENDER_VAR.set("")
        CONTACT_VAR.set("")
        DOB_VAR.set("")
        text_address.delete("1.0",END)
def get_cursor(ev):
    cursor_row = student_table.focus()
    contents = student_table.item(cursor_row)
    row = contents['values'] 
    ROLL_NO_VAR.set(row[0])
    NAME_VAR.set(row[1])
    EMAIL_VAR.set(row[2])
    GENDER_VAR.set(row[3])
    CONTACT_VAR.set(row[4])
    DOB_VAR.set(row[5])
    text_address.delete("1.0",END)
    text_address.insert(END,row[6])
def update():
    con = pymysql.connect(host="localhost",user="root",password="",database="sms")
    cur = con.cursor()
    cur.execute("update students set NAME = %s,EMAIL = %s, GENDER = %s,CONTACT = %s,DOB = %s,ADDRESS = %s where ROLL_NO = %s",
    (NAME_VAR.get(),EMAIL_VAR.get(),GENDER_VAR.get(),CONTACT_VAR.get(),DOB_VAR.get(),
    text_address.get('1.0',END),ROLL_NO_VAR.get()))
    con.commit()
    fetch_data()
    clear()
    con.close()
    messagebox.showinfo("success","Record has been inserted")
def delete():
    con = pymysql.connect(host="localhost",user="root",password="",database="sms")
    cur = con.cursor()
    cur.execute("delete from students where ROLL_NO = %s",ROLL_NO_VAR.get())
    con.commit()
    fetch_data()
    clear()
    con.close()


# ------------------------manage frame--------------------------------

manage_frame = Frame(m,bd=4,bg="white")
manage_frame.place(x=20,y=100,width=450,height=585)

m_title = Label(manage_frame,text= "Manage Student",font=("times new roman",40,"bold"),fg="black")
m_title.grid(row=0,columnspan=2,pady=20)

lbl_roll =  Label(manage_frame,text= "Roll No:",font=("times new roman",20,"bold"),fg="black")
lbl_roll.grid(row=1,column=0,columnspan=2,pady=10,padx=20,sticky="w")
text_roll = Entry(manage_frame,textvariable=ROLL_NO_VAR,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
text_roll.grid(row=1,column=1,columnspan=2,pady=10,padx=20,sticky="w")

lbl_name =  Label(manage_frame,text= "Name:",font=("times new roman",20,"bold"),fg="black")
lbl_name.grid(row=2,column=0,columnspan=2,pady=10,padx=20,sticky="w")
text_name = Entry(manage_frame,textvariable=NAME_VAR,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
text_name.grid(row=2,column=1,columnspan=2,pady=10,padx=20,sticky="w")

lbl_email =  Label(manage_frame,text= "Email:",font=("times new roman",20,"bold"),fg="black")
lbl_email.grid(row=3,column=0,columnspan=2,pady=10,padx=20,sticky="w")
text_email = Entry(manage_frame,textvariable=EMAIL_VAR,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
text_email.grid(row=3,column=1,columnspan=2,pady=10,padx=20,sticky="w")

lbl_Gender =  Label(manage_frame,text= "Gender:",font=("times new roman",20,"bold"),fg="black")
lbl_Gender.grid(row=4,column=0,columnspan=2,pady=10,padx=20,sticky="w")
combo_Gender = ttk.Combobox(manage_frame,textvariable=GENDER_VAR,font=("times new roman",13,"bold"),state="readonly")
combo_Gender['value']=("male","female","other")
combo_Gender.grid(row=4,column=1,columnspan=2,pady=10,padx=20,sticky="w")

lbl_contact=  Label(manage_frame,text= "Contact:",font=("times new roman",20,"bold"),fg="black")
lbl_contact.grid(row=5,column=0,columnspan=2,pady=10,padx=20,sticky="w")
text_contact = Entry(manage_frame,textvariable=CONTACT_VAR,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
text_contact.grid(row=5,column=1,columnspan=2,pady=10,padx=20,sticky="w")

lbl_dob =  Label(manage_frame,text= "D.O.B:",font=("times new roman",20,"bold"),fg="black")
lbl_dob.grid(row=6,column=0,columnspan=2,pady=10,padx=20,sticky="w")
text_dob = Entry(manage_frame,textvariable=DOB_VAR,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
text_dob.grid(row=6,column=1,columnspan=2,pady=10,padx=20,sticky="w")

lbl_address =  Label(manage_frame,text= "Address:",font=("times new roman",20,"bold"),fg="black")
lbl_address.grid(row=7,column=0,columnspan=2,pady=10,padx=20,sticky="w")
text_address = Text(manage_frame,font=("times new roman",10,"bold"),width=30,height=3)
text_address.grid(row=7,column=1,columnspan=2,pady=10,padx=20,sticky="w")


# --------------------------------btn frame-----------------------------

btn_frame = Frame(manage_frame,bd=3,bg="white")
btn_frame.place(x=15,y=525,width=420)

Addbtn = Button(btn_frame,text="Add",width=10,command=add_students).grid(row=0,column=0,pady=10,padx=10)
Updatebtn = Button(btn_frame,text="Update",width=10,command=update).grid(row=0,column=1,pady=10,padx=10)
Deletebtn = Button(btn_frame,text="Delate",width=10,command = delete).grid(row=0,column=2,pady=10,padx=10)
Clearbtn = Button(btn_frame,text="Clear",width=10,command=clear).grid(row=0,column=3,pady=10,padx=10)

# -------------------------Details frame----------------------

Detail_frame = Frame(m,bd=4,bg="white")
Detail_frame.place(x=500,y=100,width=880,height=585)

lbl_Search = Label(Detail_frame,text= "Search By",font=("times new roman",20,"bold"),bg="white",fg="black")
lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

combo_Search = ttk.Combobox(Detail_frame,textvariable=SEARCH_BY,font=("times new roman",13,"bold"),width=10,state="readonly")
combo_Search['value']=("Roll No","Name","Contact")
combo_Search.grid(row=0,column=1,pady=10,padx=20)
text_Search = Entry(Detail_frame,textvariable=SEARCH_TEXT,font=("times new roman",15,"bold"),width=20,bd=5,relief=GROOVE)
text_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")


Searchbtn = Button(Detail_frame,text="Search",width=10,pady=5).grid(row=0,column=3,pady=10,padx=10)
Showallbtn = Button(Detail_frame,text="Show All",width=10,pady=5).grid(row=0,column=4,pady=10,padx=10)

# --------------------------table frame-------------------------

Table_frame = Frame(Detail_frame,bd=4,bg="black")
Table_frame.place(x=18,y=70,width=760,height=500)

scroll_x = Scrollbar(Table_frame,orient=HORIZONTAL)
scroll_y = Scrollbar(Table_frame,orient=VERTICAL)

student_table = ttk.Treeview(Table_frame,column=("row","name","email","Gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config()
scroll_y.config()

student_table.heading("row",text="ROLL_NO")
student_table.heading("name",text="NAME")
student_table.heading("email",text="EMAIL")
student_table.heading("Gender",text="GENDER")
student_table.heading("contact",text="CONTACT")
student_table.heading("dob",text="D.O.B")
student_table.heading("Address",text="ADDRESS")

student_table['show']='headings'
student_table.column("row",width=100)
student_table.column("name",width=100)
student_table.column("email",width=100)
student_table.column("Gender",width=100)
student_table.column("contact",width=100)
student_table.column("dob",width=100)
student_table.column("Address",width=150)

student_table.pack(fill=BOTH,expand=1)
student_table.bind("<ButtonRelease-1>",get_cursor)

m.mainloop()