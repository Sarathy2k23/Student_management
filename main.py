from tkinter import *
from tkinter import ttk
import sqlite3


# c=sqlite3.connect("Student.db")
# curses=c.cursor()
# curses.execute("CREATE TABLE IF NOT EXISTS Student(ID INTEGER,NAME VARCHAR(20),AGE INTEGER, DOB VARCHAR(20),GENDER VARCHAR(20),CITY VARCHAR(50))")
# c.commit()
# c.close()
# print("table is created")

class Student():
    
    
    def __init__(self,main):

        self.main=main
        self.T_Frame=Frame(self.main,height=50,width=1200,bg="blue",bd=2,relief=GROOVE)
        self.T_Frame.pack()
        self.Heading=Label(self.T_Frame,width=800,text="Student Management system",font="arial 20 bold",bg="blue")
        self.Heading.pack()
    
        self.Frame_1=Frame(self.main,height=800,width=450,bg="yellow",bd=2,relief=GROOVE)
        self.Frame_1.pack(side=LEFT)

        self.Frame_2=Frame(self.main,height=800,width=700,bg="orange",bd=2,relief=GROOVE)
        self.Frame_2.pack(side=RIGHT)
        self.Frame_1.pack_propagate(0)

        Label(self.Frame_1,text="Student Details",font="Serif",bg="yellow").place(x=0,y=20)

        #inside the lable one 1
        self.Id=Label(self.Frame_1,text="ID",font="arial 12 bold",bg="yellow")
        self.Id.place(x=40,y=60)

        #for entry
        self.Id_Entry=Entry(self.Frame_1,width=50)
        self.Id_Entry.place(x=130,y=60)
        
        #
        #inside the lable one 2 Name
        self.Name=Label(self.Frame_1,text="Name",font="arial 12 bold",bg="yellow")
        self.Name.place(x=40,y=120)

        #for entry
        self.Name_Entry=Entry(self.Frame_1,width=50)
        self.Name_Entry.place(x=130,y=120)

        #
        # #inside the lable one 3 Age
        self.Age=Label(self.Frame_1,text="Age",font="arial 12 bold",bg="yellow")
        self.Age.place(x=40,y=180)

        #for entry
        self.Age_Entry=Entry(self.Frame_1,width=50)
        self.Age_Entry.place(x=130,y=180)



        #
        #inside the lable one 4 DOB
        self.DOB=Label(self.Frame_1,text="DOB",font="arial 12 bold",bg="yellow")
        self.DOB.place(x=40,y=240)

        #for entry
        self.DOB_Entry=Entry(self.Frame_1,width=50)
        self.DOB_Entry.place(x=130,y=240)


        #
        #inside the lable one 5 Gender
        self.Gender=Label(self.Frame_1,text="Gender",font="arial 12 bold",bg="yellow")
        self.Gender.place(x=40,y=300)

        #for entry
        self.Gender_Entry=Entry(self.Frame_1,width=50)
        self.Gender_Entry.place(x=130,y=300)

        #
        #inside the lable one 6 city
        self.City=Label(self.Frame_1,text="City",font="arial 12 bold",bg="yellow")
        self.City.place(x=40,y=360)

        #for entry
        self.City_Entry=Entry(self.Frame_1,width=50)
        self.City_Entry.place(x=130,y=360)

        #===================================+++++++++++++++++++========
        #Button on under entryes
        self.Button=Frame(self.Frame_1,height=200,width=300,bg="yellow",bd=2,relief=GROOVE)
        
        self.Button.place(x=150,y=450)

        self.add=Button(self.Button,text="Add",width=25,command=self.Add).pack()
        self.delete=Button(self.Button,text="Delete",width=25,command=self.Delete).pack()
        self.update=Button(self.Button,text="Update",width=25,command=self.Update).pack()
        self.clear=Button(self.Button,text="Clear",width=25,command=self.Clear).pack()


        #++++++++++++++++++++++++++===========================+++++++=
        #table creation

        self.tree=ttk.Treeview(self.Frame_2,columns=("c1","c2","c3","c4","c5","c6"),show="headings",height=25)
        

        self.tree.column("#1",anchor=CENTER,width=40)
        self.tree.heading("#1",text="ID")
        self.tree.column("#2",anchor=CENTER,width=130)
        self.tree.heading("#2",text="Name")
        self.tree.column("#3",anchor=CENTER,width=40)
        self.tree.heading("#3",text="Age")
        self.tree.column("#4",anchor=CENTER,width=80)
        self.tree.heading("#4",text="DOB")
        self.tree.column("#5",anchor=CENTER,width=80)
        self.tree.heading("#5",text="Gender")
        self.tree.column("#6",anchor=CENTER,width=120)
        self.tree.heading("#6",text="City")

        #insert calue in to table
        
        self.tree.pack()


    #create a Add ,delete ,udate clrar command

    def Add(self):
        id=self.Id_Entry.get()
        name=self.Name_Entry.get()
        age=self.Age_Entry.get()
        dob=self.DOB_Entry.get()
        gender=self.Gender_Entry.get()
        city=self.City_Entry.get()
        c=sqlite3.connect("Student.db")
        curses=c.cursor()
        curses.execute("INSERT INTO Student(ID,NAME,AGE,DOB,GENDER,CITY) VALUES(?,?,?,?,?,?)",(id,name,age,dob,gender,city))
        c.commit()
        c.close()
        print("data inserrt sucess fully")
        self.tree.insert("",index=0,values=(id,name,age,dob,gender,city))

    def Delete(self):
        D_item=self.tree.selection()[0]
        selected_Single_Value=self.tree.item(D_item)['values'][0]
        print(selected_Single_Value)
        c=sqlite3.connect("Student.db")
        cursos=c.cursor()
        cursos.execute("DELETE FROM Student WHERE ID={}".format(selected_Single_Value))
        print("value edited")
        c.commit()
        c.close()
        self.tree.delete(D_item)


    def Update(self):
        id=self.Id_Entry.get()
        name=self.Name_Entry.get()
        age=self.Age_Entry.get()
        dob=self.DOB_Entry.get()
        gender=self.Gender_Entry.get()
        city=self.City_Entry.get()
        D_item=self.tree.selection()[0]
        selected_Single_Value=self.tree.item(D_item)['values'][0]
        print(selected_Single_Value)
        c=sqlite3.connect("Student.db")
        cursos=c.cursor()
        cursos.execute("UPDATE Student SET ID=?, NAME=?,AGE=?,DOB=?,GENDER=?,CITY=? WHERE ID=?",(id,name,age,dob,gender,city,selected_Single_Value))
        c.commit()
        c.close()
        print("Value updated")
        self.tree.item(D_item,values=(id,name,age,dob,gender,city))
        
    def Clear(self):
        self.Id_Entry.delete(0,END)
        self.Name_Entry.delete(0,END)
        self.Age_Entry.delete(0,END)
        self.DOB_Entry.delete(0,END)
        self.Gender_Entry.delete(0,END)
        self.City_Entry.delete(0,END)

       
main=Tk()
main.title("Studen Management System")
main.resizable(False,False)
main.geometry("950x700")

Student(main)

main.mainloop()