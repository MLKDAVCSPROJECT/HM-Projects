from tkinter import *
from tkinter import messagebox
import mysql.connector as pymysql
class Login:

   def __init__(self,root):

      self.root=root

      self.root.title("Sim Card Management")

      self.root.geometry("1366x700+0+0")

      self.root.resizable(False,False)

      self.loginform()

   def loginform(self):

      Frame_login=Frame(self.root,bg="gray25")

      Frame_login.place(x=0,y=0,height=700,width=1366)

      

           

      frame_input=Frame(self.root,bg='gray25')

      frame_input.place(x=520,y=130,height=450,width=350)



      label1=Label(frame_input,text="Login Here",font=('Al Nile',30),

                   fg="thistle4",bg='black')

      label1.place(x=75,y=20)



      label2=Label(frame_input,text="Username",font=("American Typewriter",20),

                   fg='thistle4',bg='black')

      label2.place(x=30,y=95)

      self.username=Entry(frame_input,font=("American Typewriter",15,"bold"),

                       bg='white')

      self.username.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input,text="Phone Number",font=("American Typewriter",20),

                   fg='thistle4',bg='black')

      label3.place(x=30,y=195)

      self.phonenumber_txt=Entry(frame_input,font=("Al Nile",15,"bold"),

                        bg='white')

      self.phonenumber_txt.place(x=30,y=245,width=270,height=35)

   



      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",

                  font=("Al Nile",15),fg="thistle4",bg="black",

                  bd=0,width=15,height=1)

      btn2.place(x=90,y=340)

        

      btn3=Button(frame_input,command=self.Register,text="Not Yet? Register Now"

                  ,cursor="hand2",font=("american typewriter",10),bg='black',fg="thistle4",bd=0)

      btn3.place(x=110,y=390)



   def login(self):

      if self.username.get()=="" or self.phonenumber_txt.get()=="":

         messagebox.showerror("Nope, Sorry","All fields are required",parent=self.root)

      else:
            con=pymysql.connect(host='localhost',user='root',password='1234',

                                database='simcard')

            cur=con.cursor()

            cur.execute('select * from register where username=%s and phonenumber=%s'

                        ,(self.username.get(),self.phonenumber_txt.get()))

            row=cur.fetchone()

            if row==None:

               messagebox.showerror('Eh?','Invalid Username And phone number'

                                    ,parent=self.root)

               self.loginclear()

               self.username.focus()

            else:

               self.appscreen()

               con.close()

            

   def Register(self):



      Frame_login1=Frame(self.root,bg="gray25")

      Frame_login1.place(x=0,y=0,height=700,width=1366)

      

     

      

      frame_input2=Frame(self.root,bg='gray25')

      frame_input2.place(x=320,y=130,height=450,width=630)



      label1=Label(frame_input2,text="Register Here",font=('al nile',30),

                   fg="thistle4",bg='black')

      label1.place(x=45,y=20)



      label2=Label(frame_input2,text="Username",font=("american typewriter",20),

                   fg='thistle4',bg='black')

      label2.place(x=30,y=95)

      self.entry=Entry(frame_input2,font=("al nile",15, "bold"),

                       bg='white')

      self.entry.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input2,text="Date of Birth",font=("american typewriter",20),

                   fg='thistle4',bg='black')

      label3.place(x=30,y=195)

      self.entry2=Entry(frame_input2,font=("al nile",15,"bold"),

                        bg='white')

      self.entry2.place(x=30,y=245,width=270,height=35)



      label4=Label(frame_input2,text="Phone Number",font=("american typewriter",20),

                   fg='thistle4',bg='black')

      label4.place(x=330,y=95)

      self.entry3=Entry(frame_input2,font=("al nile",15,"bold"),

                       bg='white')

      self.entry3.place(x=330,y=145,width=270,height=35)



      label5=Label(frame_input2,text="Data Plan",

                   font=("american typewriter",20),fg='thistle4',bg='black')

      label5.place(x=330,y=195)

      self.entry4=Entry(frame_input2,font=("al nile",15,"bold"),

                       bg='white')

      self.entry4.place(x=330,y=245,width=270,height=35)
      label4=Label(frame_input2,text="*enter 10 digit number",

                   fg='linen',bg='gray25')

      label4.place(x=330,y=180)
      



      btn2=Button(frame_input2,command=self.register,text="Register"

                  ,cursor="hand2",font=("american typewriter",15),fg="thistle4",

                  bg="black",bd=0,width=15,height=1)

      btn2.place(x=90,y=340)

        

      btn3=Button(frame_input2,command=self.loginform,

                  text="Login",cursor="hand2",

                  font=("al nile",10),bg='black',fg="thistle4",bd=0)

      btn3.place(x=110,y=390)





   def register(self):
      list1 = list()

      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)

      

      else:

         try:

            con=pymysql.connect(host="localhost",user="root",password="1234",

                                database="simcard")

            cur=con.cursor()

            cur.execute("select * from register where phonenumber=%s"

                        ,self.entry3.get())

            row=cur.fetchone()

            if row!=None:

               messagebox.showerror("Error","Please Enter Vallid Phone Number",parent=self.root)

               self.regclear()

               self.entry.focus()

            else:

               cur.execute("insert into register values(%s,%s,%s,%s)"

                           ,(self.entry.get(),self.entry3.get(),

                           self.entry2.get(),

                           list1.append(self.entry4.get())))

               con.commit()

               con.close()

               messagebox.showinfo("Success","Done-Done"

                                   ,parent=self.root)

               self.regclear()

         except Exception as es:

            messagebox.showerror("Tch-Tch",f"Error due to:{str(es)}"

                                 ,parent=self.root)



   def appscreen(self):



      Frame_login=Frame(self.root,bg="gray25")

      Frame_login.place(x=0,y=0,height=700,width=1366)

      
      btn2=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",

                  font=("al nile",15),fg="thistle4",bg="black",

                  bd=0,width=15,height=1)

      btn2.place(x=550,y=205)

      btn1=Button(Frame_login,text="Update plan",command=self.screen,cursor="hand2",

                  font=("american typewriter",25),fg="thistle4",bg="black",

                  bd=0,width=15,height=1)

      btn1.place(x=550,y=305)

      btn3=Button(Frame_login,text="Delete Account",cursor="hand2",command=self.plan,

                  font=("american typewriter",25),fg="thistle4",bg="black",

                  bd=0,width=15,height=1)

      btn3.place(x=550,y=405) 





   def screen(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=1366)


      frame_input3=Frame(self.root,bg='gray25')

      frame_input3.place(x=450,y=130,height=450,width=630)

      label1=Label(frame_input3,text="Update plan",font=('al nile',30,'bold'),

                   fg="thistle4",bg='black')

      label1.place(x=175,y=20)

      label2=Label(frame_input3,text="Username",font=("american typewriter",20,"bold"),

                   fg='thistle4',bg='black')

      label2.place(x=30,y=95)

      self.username=Entry(frame_input3,font=("american typewriter",15,"bold"),

                       bg='white')

      self.username.place(x=30,y=145,width=270,height=35)

      label3=Label(frame_input3,text="Phone Number",font=("american typewriter",20,"bold"),

                   fg='thistle4',bg='black')

      label3.place(x=30,y=195)

      self.phonenumber_txt=Entry(frame_input3,font=("american typewriter",15,"bold"),

                        bg='white')

      self.phonenumber_txt.place(x=30,y=245,width=270,height=35)

      label4=Label(frame_input3,text="Plan",font=("american typewriter",20,"bold"),

                   fg='thistle4',bg='black')

      label4.place(x=30,y=295)
      self.entry3=Entry(frame_input3,font=("american typewriter",15,"bold"),

                       bg='white')
      self.entry3.place(x=30,y=345,width=270,height=35)




      btn1=Button(frame_input3,text="Back",command=self.appscreen,cursor="hand2",

                  font=("american typewriter",15),fg="thistle4",bg="black",

                  bd=0,width=15,height=1)

      btn1.place(x=225,y=400)

      btn2=Button(frame_input3,text="Update",cursor="hand2",command=self.update,

                  font=("american typewriter",25),fg="thistle4",bg="black",

                  bd=0,width=10,height=2)

      btn2.place(x=355,y=200)

   def update(self):
      if self.username.get()=="" or self.phonenumber_txt.get()=="" or self.entry3.get()=="":

         messagebox.showerror("Nope, Sorry","All fields are required",parent=self.root)

      else:

         try:

            con=pymysql.connect(host='localhost',user='root',password='1234',

                                database='simcard')

            cur=con.cursor()

            cur.execute('select * from register where username=%s and phonenumber=%s'

                        ,(self.username.get(),self.phonenumber_txt.get()))

            row=cur.fetchone()

            if row==None:

               messagebox.showerror('Eh?','Invalid Username And Phone number'

                                    ,parent=self.root)

               self.updateclear()

               self.username.focus()

            else:

               sql="update register set plan=%s where phonenumber=%s"
               val=(self.entry3.get(),self.phonenumber_txt.get())
               
               cur.execute(sql,val)
               con.commit()



               
              
               messagebox.showinfo("Done-Done","Got it!")


               self.updateclear()

               self.username.focus()
               

         except Exception as es:

            messagebox.showerror('Tch-Tch',f'Error Due to : {str(es)}'

                                 ,parent=self.root)
   def plan(self):
      Frame_login=Frame(self.root,bg="gray25")
      Frame_login.place(x=0,y=0,height=700,width=1366)


      frame_input3=Frame(self.root,bg='gray25')

      frame_input3.place(x=450,y=130,height=450,width=630)

      label1=Label(frame_input3,text="Delete Account",font=('al nile',30,'bold'),

                   fg="thistle4",bg='black')

      label1.place(x=175,y=20)

      label2=Label(frame_input3,text="Username",font=("al nile",20,"bold"),

                   fg='thistle4',bg='black')

      label2.place(x=30,y=95)

      self.username=Entry(frame_input3,font=("al nile",15,"bold"),

                       bg='white')

      self.username.place(x=30,y=145,width=270,height=35)

      label3=Label(frame_input3,text="Phone Number",font=("american typewriter",20,"bold"),

                   fg='thistle4',bg='black')

      label3.place(x=30,y=195)

      self.phonenumber_txt=Entry(frame_input3,font=("al nile",15,"bold"),

                        bg='white')

      self.phonenumber_txt.place(x=30,y=245,width=270,height=35)

      




      btn1=Button(frame_input3,text="Back",command=self.appscreen,cursor="hand2",

                  font=("al nile",15),fg="thistle4",bg="black",

                  bd=0,width=15,height=1)

      btn1.place(x=225,y=400)

      btn2=Button(frame_input3,text="Delete",cursor="hand2",command=self.delete,

                  font=("al nile",25),fg="thistle4",bg="black",

                  bd=0,width=10,height=2)

      btn2.place(x=355,y=200)
   def delete(self):
      con=pymysql.connect(host='localhost',user='root',password='1234',

                                database='simcard')

      cur=con.cursor()

      if self.username.get()=="" or self.phonenumber_txt.get()=="":

         messagebox.showerror("Nope, Sorry","All fields are required",parent=self.root)
      else:
          try:
              sql="delete from register where phonenumber=%s"
              val=(self.phonenumber_txt.get())
              cur.execute(sql,val)
              con.commit()
             
              messagebox.showinfo("Done-Done","Gotcha!")
               


            
               

          except Exception as es:

            messagebox.showerror('Tch-Tch',f'Error Due to : {str(es)}'
                                 ,parent=self.root)
 

      


   



   def updateclear(self):
      self.username.delete(0,END)

      self.phonenumber_txt.delete(0,END)
       
      self.entry3.delete(0,END)

   def loginclear(self):

      self.username.delete(0,END)

      self.phonenumber_txt.delete(0,END)
      
   def regclear(self):
      self.entry.delete(0,END)

      self.entry2.delete(0,END)

      self.entry3.delete(0,END)

      self.entry4.delete(0,END) 



root=Tk()

ob=Login(root)

root.mainloop()

