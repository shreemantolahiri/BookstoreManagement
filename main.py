import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger")

import tkinter
#CREATING DATABASE AND TABLE
mycursor=mydb.cursor()
mycursor.execute("create database if not exists store")
mycursor.execute("use store")

mycursor.execute("create table if not exists Available_Books(BookName varchar(30) primary key,Genre varchar(20),Quantity int(3),Author varchar(20),Price int(4))")
mycursor.execute("create table if not exists Sell_rec(CustomerName varchar(25),PhoneNumber char(10) , BookName varchar(30),Quantity int(5),TotalAmt int(5), Cashier varchar(30))")
mycursor.execute("create table if not exists Staff_details(EmpID int(3) unique key,Name varchar(30), Gender varchar(10),Age int(3), PhoneNumber char(10), Sale_Amt int(5) default 0)" )       
mycursor.execute("select name from Staff_details where EmpID=0")
dot=mycursor.fetchone()

if dot is None:
    mycursor.execute("insert into Staff_details(EmpID,Name) values(0,'admin')")

mydb.commit()



def select10():
    login11=tkinter.Tk()
    login11.geometry("500x500")
    login11.configure(bg="white")    
def select9():
    login10=tkinter.Tk()
    login10.geometry("500x500")
    login10.configure(bg="white")
def select8():
    login9=tkinter.Tk()
    login9.geometry("500x500")
    login9.configure(bg="white")        
def select7():
    login8=tkinter.Tk()
    login8.geometry("500x500")
    login8.configure(bg="white")
def select6():
    login7=tkinter.Tk()
    login7.geometry("500x500")
    login7.configure(bg="white")
def select5():
    login6=tkinter.Tk()
    login6.geometry("500x500")
    login6.configure(bg="white")
def select4():
    login5=tkinter.Tk()
    login5.geometry("500x500")
    login5.configure(bg="white")



#login    
def check():
    user=e1.get()
    pw=e2.get()
    mycursor.execute("select EmpID, Name from Staff_details where EmpID='"+user+"'")
    pot=mycursor.fetchone()
    
    
        
    
    
    if pot is None:
        s1=tkinter.Tk()
        s1.title('Champ Bookstore')
        s1.geometry("300x100")
        s1.configure(bg="white")
        s1=tkinter.Label(s1,text="EmpID INCORRECT! \n LOGIN UNSUCCESFUL!",font=("Ariel",10,"bold"))
        s1.place(x=50,y=50)
    elif pot is not None:
        (rms,mp)=pot
        mycursor.execute("select Name from Staff_details where Name='"+pw+"'")
        a=mycursor.fetchone()
        
        
        
        
     
        if a is None :
                     
                s2=tkinter.Tk()
                s2.title('Champ Bookstore')
                s2.geometry("300x100")
                s2.configure(bg="white")
                s7=tkinter.Label(s2,text="NAME INCORRECT!\n LOGIN UNSUCCESSFUL!",font=("Ariel",10,"bold"))
                s7.place(x=50,y=50)
        
        

        
        elif a is not None:
            (b,)=a
             
            if b!=mp:
                s2=tkinter.Tk()
                s2.title('Champ Bookstore')
                s2.geometry("300x100")
                s2.configure(bg="white")
                s7=tkinter.Label(s2,text="NAME INCORRECT!\n LOGIN UNSUCCESSFUL!",font=("Ariel",10,"bold"))
                s7.place(x=50,y=50)
                
            elif b==mp:
                global barsoom
                barsoom=a[0]

                    

                  


                #HOME PAGE
                
                promptt()
                global login1
                login1=tkinter.Tk()
                login1.lift()
                login1.focus_force() 
                login1.title('Home Page')
                login1.geometry("500x700")
                login1.configure(bg="light blue")
                l12=tkinter.Label(login1,text="Champ Bookstore",font=("Ariel",20,"bold"),bg="light blue")
                l12.place (x=150,y=0)
                l6=tkinter.Label(login1,text="Add Books",font=("Ariel",20,"bold"),bg="light blue")
                l6.place (x=10,y=50)
                b2=tkinter.Button(login1,text="SELECT",font=("Ariel,10"),bg="white",command=select1)
                b2.place(x=250,y=50)
                l7=tkinter.Label(login1,text="Delete Books",font=("Ariel",20,"bold"),bg="light blue")
                l7.place (x=10,y=100)
                b3=tkinter.Button(login1,text="SELECT",font=("Ariel,10"),bg="white",command=select2)
                b3.place(x=250,y=100)
                l8=tkinter.Label(login1,text="Search Books",font=("Ariel",20,"bold"),bg="light blue")
                l8.place (x=10,y=150)
                b4=tkinter.Button(login1,text="SELECT",font=("Ariel,10"),bg="white",command=select3)
                b4.place(x=250,y=150)
                l9=tkinter.Label(login1,text="Staff Details",font=("Ariel",20,"bold"),bg="light blue")
                l9.place (x=10,y=200)
                b5=tkinter.Button(login1,text="SELECT",font=("Ariel,10"),bg="white",command=select4)
                b5.place(x=250,y=200)
                l10=tkinter.Label(login1,text="Sales Data",font=("Ariel",20,"bold"),bg="light blue")
                l10.place (x=10,y=250)
                b6=tkinter.Button(login1,text="SELECT",font=("Ariel,10"),bg="white",command=select5)
                b6.place(x=250,y=250)
                l11=tkinter.Label(login1,text="Available Books",font=("Ariel",20,"bold"),bg="light blue")
                l11.place (x=10,y=300)
                b7=tkinter.Button(login1,text="SELECT",font=("Ariel,10"),bg="white",command=select6)
                b7.place(x=250,y=300)
                l12=tkinter.Label(login1,text="Total Income",font=("Ariel",20,"bold"),bg="light blue")
                l12.place (x=10,y=350)
                b8=tkinter.Button(login1,text="SELECT",font=("Ariel,10"),bg="white",command=select7)
                b8.place(x=250,y=350)
                login.destroy()
                l13=tkinter.Label(login1,text="Out of Stock",font=("Ariel",20,"bold"),bg="light blue")
                l13.place (x=10,y=400)
                b10=tkinter.Button(login1,text="SELECT",font=("Ariel,10"),bg="white",command=select10)
                b10.place(x=250,y=400)
                l14=tkinter.Label(login1,text="Billing",font=("Ariel",20,"bold"),bg="light blue")
                l14.place (x=10,y=450)
                b11=tkinter.Button(login1,text="SELECT",font=("Ariel,10"),bg="white",command=select20)
                b11.place(x=250,y=450)
                b10=tkinter.Button(login1,text="LOGOUT",font=("Ariel,10"),bg="yellow",command=select11)
                b10.place(x=150, y=550)
                b9=tkinter.Button(login1,text="DELETE ALL DATA",font=("Ariel,10"),bg="red",command=select8)
                b9.place(x=100, y=500)
                if barsoom=='admin':
                    
                    b13=tkinter.Button(login1,text="Run Demo",font=("Ariel,10"),bg="green",command=selectdemo)
                    b13.place(x=300, y=500)
            



     
#start page
login=tkinter.Tk()
login.focus_force()
login.title('Welcome')
login.geometry("700x500")
login.configure(bg="light blue")
l1=tkinter.Label(text="WELCOME TO CHAMP BOOKSTORE",font=("Ariel",20,"bold","underline"),bg="light blue")
l1.place (x=150,y=50)

l2=tkinter.Label(text="EmpID:",font=("Ariel",10,"bold"),bg="light blue")
l2.place (x=150,y=150)
e1=tkinter.Entry(width=20,font=("Ariel",10,"bold"))
e1.place(x=250,y=150)
l3=tkinter.Label(text="Name:",font=("Ariel",10,"bold"),bg="light blue")
l3.place (x=150,y=200)
e2=tkinter.Entry(width=20,font=("Ariel",10,))
e2.place(x=250,y=200)
b1=tkinter.Button(text="Login",font=("Ariel",15,"bold"),bg="red",command=check)
b1.place(x=250,y=250)

info=tkinter.Tk()
info.attributes("-topmost", True)
info.title('**IMPORTANT**')
info.attributes('-topmost',True)
info.geometry("300x200")
info.configure(bg="white")
info1=tkinter.Label(info,text="If you are ADMIN, ",font=("Ariel",10,"bold"))
info1.place(x=50,y=50)
info2=tkinter.Label(info,text="Please use following details: ",font=("Ariel",10,"bold"))
info2.place(x=50,y=70)
info3=tkinter.Label(info,text="EmpID: 000",font=("Times New Roman",10,"bold"))
info3.place(x=60,y=100)
info4=tkinter.Label(info,text="Name: admin",font=("Times New Roman",10,"bold"))
info4.place(x=60,y=120)



#DELETE ALL DATA
def select8():
              if barsoom=='admin':
                  def yes():
                      query="drop database store"
                      mycursor.execute(query)
                      mydb.commit()
                      
                      login1.destroy()
                      confirm.destroy()
                  def no():
                          confirm.destroy()
                  confirm=tkinter.Tk()
                  confirm.geometry("400x300")
                  confirm.configure(bg="light blue")
                  conf=tkinter.Label(confirm, text= "Confirm?",font= ("Ariel",10,"bold"),bg="light blue")
                  conf.place(x=20, y= 100)
                  cony=tkinter.Button(confirm, text="YES", font=("Ariel,10"),bg="red",command=yes)
                  cony.place(x= 130, y= 100)
                  conn=tkinter.Button(confirm, text="NO", font=("Ariel,10"),bg="green",command=no)
                  conn.place(x=210,y=100)
                  CONT=tkinter.Label(confirm,text="Warning: This will erase all data.",font= ("Ariel",10,"bold"))
                  CONT.place(x=20,y=10)

              else:

                    info2=tkinter.Tk()
                    info2.title('ERROR')
                    info2.attributes('-topmost',True)
                    info2.geometry("300x100")
                    info2.configure(bg="white")
                    info3=tkinter.Label(info2,text="Only admin can perform",font=("Ariel",10,"bold"))
                    info3.place(x=50,y=50)
                    info3=tkinter.Label(info2,text="DELETE ALL DATA ",font=("Ariel",10,"bold"))
                    info3.place(x=50,y=70)
                  

#demo entry
def selectdemo():
    #addingbooks
    mycursor.execute("select BookName from Available_Books where BookName='The Fault in our Stars'")    
    dot=mycursor.fetchone()

    if dot is None:
        mycursor.execute("insert into Available_Books values('The Fault in our Stars','Romance',25,'John Green',199) ")
    mycursor.execute("select BookName from Available_Books where BookName='The Immortals of Meluha'")    
    dot=mycursor.fetchone()

    if dot is None:
        mycursor.execute("insert into Available_Books values('The Immortals of Meluha','Indian Mythology',15,'Amish Tripathi',299) ")
    mycursor.execute("select BookName from Available_Books where BookName='Life of Pi'")    
    dot=mycursor.fetchone()

    if dot is None:
        mycursor.execute("insert into Available_Books values('Life of Pi','Adventure',25,'Yann Martel',349) ")
    mycursor.execute("select BookName from Available_Books where BookName='Five Point Someone'")    
    dot=mycursor.fetchone()

    if dot is None:
        mycursor.execute("insert into Available_Books values('Five Point Someone','Novel',10,'Chetan Bhagat',229) ")
    #adding staff details
    mycursor.execute("select EmpID from staff_details where EmpID=10")    
    dot=mycursor.fetchone()

    if dot is None:
        mycursor.execute("insert into staff_details VALUES(10,'Manoj','male',23,6574125874,0) ")
    mycursor.execute("select EmpID from staff_details where EmpID=11")    
    dot=mycursor.fetchone()

    if dot is None:
        mycursor.execute("insert into staff_details VALUES(11,'Meghna','female',32,9465781123,0) ")
    mycursor.execute("select EmpID from staff_details where EmpID=12")    
    dot=mycursor.fetchone()
    

    if dot is None:
        mycursor.execute("insert into staff_details VALUES(12,'Chirag','male',24,9854455541,0) ")
    mycursor.execute("select EmpID from staff_details where EmpID=13")    
    dot=mycursor.fetchone()

    if dot is None:
        mycursor.execute("insert into staff_details VALUES(13,'Kashish','female',27,9854454177,0) ")
    mydb.commit()
    pup1=tkinter.Tk()
    pup1.geometry("300x100")
    pup1.configure(bg="white")
    pup2=tkinter.Label(pup1,text="DEMO RECORDS ADDED!",font=("Times New Roman",10,"bold"))
    pup2.place(x=50,y=50)
        
        
    
                  



#Add Books


def select1():
        def add1():
                 def submit():
                        book=ab2.get()

                        priced=str(ab10.get())
                        chit=len(priced)
                        if ab4 is not None:
                                genre=ab4.get()

                        chit2=len(str(ab6))
                        if chit2>=1:
                                qty=int(ab6.get())
                        if ab8 is not None:
                                author=ab8.get()
                        if chit>=1:
                                price=int(priced)
                         
                                
                                 
                        
                        
                              
                        mycursor.execute("insert into Available_Books(bookname,genre,quantity,author,price) values('{}','{}','{}','{}','{}')".format(book,genre,qty,author,price))
                        mydb.commit()


                        pup1=tkinter.Tk()
                        pup1.geometry("300x100")
                        pup1.configure(bg="white")
                        pup2=tkinter.Label(pup1,text="BOOK ADDED SUCCESSFULLY!",font=("Times New Roman",10,"bold"))
                        pup2.place(x=50,y=50)
                        promptt()

                 login2=tkinter.Tk()
                 
                 login2.title('Add Book')
                 login2.geometry("500x500")
                 login2.configure(bg="white")
                 l1=tkinter.Label(login2,text="ADD BOOKS",font=("Ariel",20,"bold"),bg="light blue")
                 l1.place (x=150,y=50)
                 ab1=tkinter.Label(login2,text="Book Name ",font=("Ariel",10,"bold"),bg="light blue")
                 ab1.place (x=50,y=100)
                 ab2=tkinter.Entry(login2,width=25,font=("Ariel",10,))
                 ab2.place(x=150,y=100)
                 ab3=tkinter.Label(login2,text="Genre",font=("Ariel",10,"bold"),bg="light blue")
                 ab3.place (x=50,y=150)
                 ab4=tkinter.Entry(login2,width=20,font=("Ariel",10))
                 ab4.place(x=150,y=150)
                 ab5=tkinter.Label(login2,text="Quantity",font=("Ariel",10,"bold"),bg="light blue")
                 ab5.place (x=50,y=200)
                 ab6=tkinter.Entry(login2,width=20,font=("Ariel",10,))
                 ab6.place(x=150,y=200)
                 ab7=tkinter.Label(login2,text="Author",font=("Ariel",10,"bold"),bg="light blue")
                 ab7.place (x=50,y=250)
                 ab8=tkinter.Entry(login2,width=20,font=("Ariel",10,))
                 ab8.place(x=150,y=250)
                 ab9=tkinter.Label(login2,text="Price",font=("Ariel",10,"bold"),bg="light blue")
                 ab9.place (x=50,y=300)
                 ab10=tkinter.Entry(login2,width=20,font=("Ariel",10,))
                 ab10.place(x=150,y=300)
                 ab11=tkinter.Button(login2,text="Submit",font=("Ariel,10"),bg="yellow",command=submit)
                 ab11.place(x=250,y=350)
        #add book qty                
        def add2():
                 def submitq():
                                        y=len(abdd)
                                        abcd=abdd[2:y-3]
                        
                        
                                        book= abcd
                                        
                                        mycursor.execute("select * from available_books where bookname='{}'".format(book))
                                        n=mycursor.fetchone()
                                        if n is not None:
                                                chit2=len(str(ab4))
                                                if chit2>=1:
                                                        qty=int(ab4.get())
                                                        mycursor.execute("update Available_Books set quantity = quantity + '{}' where bookname='{}'".format(qty,book))
                                                        mydb.commit()
                                                        pup1=tkinter.Tk()
                                                        pup1.geometry("300x100")
                                                        pup1.configure(bg="white")
                                                        pup2=tkinter.Label(pup1,text="QTY ADDED SUCCESSFULLY!",font=("Times New Roman",10,"bold"))
                                                        
                                                        pup2.place(x=50,y=50)
                                                        promptt()
                                                else:
                                                        pup1=tkinter.Tk()
                                                        pup1.geometry("300x100")
                                                        pup1.configure(bg="white")
                                                        pup2=tkinter.Label(pup1,text="ENTER VALID QTY!",font=("Times New Roman",10,"bold"))
                                                        pup2.place(x=50,y=50)
                                        else:
                                                        pup1=tkinter.Tk()
                                                        pup1.geometry("300x100")
                                                        pup1.configure(bg="white")
                                                        pup2=tkinter.Label(pup1,text="ENTER VALID NAME!",font=("Times New Roman",10,"bold"))
                                                        pup2.place(x=50,y=50)
                                                
                                                
                                        
                 login2=tkinter.Tk()
                 login2.geometry("500x300")
                 login2.configure(bg="light blue")
                 l1=tkinter.Label(login2,text="ADD BOOKS",font=("Ariel",20,"bold"),bg="light blue")
                 l1.place (x=150,y=50)
                 ab1=tkinter.Label(login2,text="Book Name ",font=("Ariel",10,"bold"),bg="light blue")
                 ab1.place (x=50,y=100)
                 variable = tkinter.StringVar(login2)
                 variable.set('Select a Book') # default value
                 mycursor.execute("select bookname from available_books")
                 dd=mycursor.fetchall()
                 def callback(*args):
                         global abdd
                         abdd=variable.get()
                         
                 ab6=tkinter.OptionMenu(login2,variable,*dd)
                 ab6.place(x=170,y=100)
                 variable.trace("w",callback)
                 ab3=tkinter.Label(login2,text="Quantity",font=("Ariel",10,"bold"),bg="light blue")
                 ab3.place (x=50,y=150)
                 ab4=tkinter.Entry(login2,width=20,font=("Ariel",10,))
                 ab4.place(x=150,y=150)
                 ab11=tkinter.Button(login2,text="Add Quantity",font=("Ariel,10"),bg="yellow",command=submitq)
                 ab11.place(x=200,y=250)
                
        s2=tkinter.Tk()
        s2.geometry("500x500")
        s2.configure(bg="light blue")
        K=tkinter.Label(s2,text="ADD BOOK",font=("Ariel",10,"bold"),bg="light blue")
        K.place(x=10,y=150)
        S=tkinter.Button(s2,text="SELECT",font=("Ariel,10"),bg="white",command=add1)
        S.place(x=250,y=150)
        Z=tkinter.Label(s2,text="ADD QUANTITY",font=("Ariel",10,"bold"),bg="light blue")
        Z.place(x=10,y=250)
        X=tkinter.Button(s2,text="SELECT",font=("Ariel,10"),bg="white",command=add2)
        X.place(x=250,y=250)




#LOGOUT
def select11():
    #start page
            global login
            login=tkinter.Tk()
            login.focus_force()

            login.title('Welcome')
            login.geometry("700x500")
            login.configure(bg="light blue")
            l1=tkinter.Label(text="WELCOME TO CHAMP BOOKSTORE",font=("Ariel",20,"bold"),bg="light blue")
            l1.place (x=150,y=50)
            l2=tkinter.Label(text="EmpID:",font=("Ariel",10),bg="light blue")
            l2.place (x=150,y=150)
            global e1
            e1=tkinter.Entry(width=20,font=("Ariel",10,"bold"))
            e1.place(x=250,y=150)
            l3=tkinter.Label(text="Name:",font=("Ariel",10),bg="white")
            l3.place (x=150,y=200)
            global e2
            e2=tkinter.Entry(width=20,font=("Ariel",10,))
            e2.place(x=250,y=200)
            b1=tkinter.Button(text="Login",font=("Ariel",20,"bold"),bg="red",command=check)
            b1.place(x=250,y=250)

            info=tkinter.Tk()
            info.title('IMPORTANT')
            info.attributes('-topmost',True)
            info.geometry("300x200")
            info.configure(bg="white")
            info1=tkinter.Label(info,text="If you are ADMIN, ",font=("Ariel",10,"bold"))
            info1.place(x=50,y=50)
            info2=tkinter.Label(info,text="Please use following details: ",font=("Ariel",10,"bold"))
            info2.place(x=50,y=70)
            info3=tkinter.Label(info,text="EmpID: 0",font=("Times New Roman",10,"bold"))
            info3.place(x=60,y=100)
            info4=tkinter.Label(info,text="Name: admin",font=("Times New Roman",10,"bold"))
            info4.place(x=60,y=120)
            login1.destroy()
    



                 


#Delete Books


def select2():
    def submitd():
            y=len(abfd)
            abcd=abfd[2:y-3]
                        
                        
            book= abcd
                                        
            qty=int(ab4.get())
            
            mycursor.execute("select * from Available_Books where bookname='{}'".format(book))
            row=mycursor.fetchone()
            if row is not None:
                                
                                mycursor.execute("select quantity from Available_books where bookname='{}'".format(book))
                                check=mycursor.fetchone()
                                num=int(check[0])
                                if num>=qty:
                                        mycursor.execute("update Available_Books set quantity = quantity - '{}' where bookname='{}'".format(qty,book))
                                        mydb.commit()
                                        pup1=tkinter.Tk()
                                        pup1.geometry("300x100")
                                        pup1.configure(bg="white")
                                        pup2=tkinter.Label(pup1,text="QTY DELETED SUCCESSFULLY!",font=("Times New Roman",10,"bold"))
                                        pup2.place(x=50,y=50)
                                        promptt()
                                else:
                                        pup9=tkinter.Tk()
                                        pup9.geometry("300x100")
                                        pup9.configure(bg="white")
                                        pup10=tkinter.Label(pup9,text="INSUFFICIENT QTY!",font=("Times New Roman",15,"bold"))
                                        pup10.place(x=50,y=50)
                                        
            else:
                                pup9=tkinter.Tk()
                                pup9.geometry("300x100")
                                pup9.configure(bg="white")
                                pup10=tkinter.Label(pup9,text="ENTER VALID BOOKNAME!",font=("Times New Roman",10,"bold"))
                                pup10.place(x=50,y=50)          
 

    def submitdr():
            y=len(abfd)
            abcd=abfd[2:y-3]
                        
                        
            book= abcd
            qty=ab4.get()
            mycursor.execute("select * from Available_Books where bookname='{}'".format(book))
            row1=mycursor.fetchone()
            if row1 is not None:
                                
                                mycursor.execute("delete from Available_Books where bookname='{}'".format(book))
                                mydb.commit()
                                pup5=tkinter.Tk()
                                pup5.geometry("300x100")
                                pup5.configure(bg="white")
                                pup6=tkinter.Label(pup5,text="BOOK DELETED SUCCESSFULLY!",font=("Times New Roman",10,"bold"))
                                pup6.place(x=50,y=50)
            else:
                                pup9=tkinter.Tk()
                                pup9.geometry("300x100")
                                pup9.configure(bg="white")
                                pup10=tkinter.Label(pup9,text="ENTER VALID BOOKNAME!",font=("Times New Roman",10,"bold"))
                                pup10.place(x=50,y=50)
                               
    login3=tkinter.Tk()
    login3.geometry("500x500")
    login3.configure(bg="light blue")
    l1=tkinter.Label(login3,text="DELETE BOOKS",font=("Ariel",20,"bold"),bg="light blue")
    l1.place (x=150,y=50)
    ab1=tkinter.Label(login3,text="Book Name:",font=("Ariel",10,"bold"),bg="light blue")
    ab1.place (x=50,y=100)
    variable = tkinter.StringVar(login3)
    variable.set('Select a Book') # default value
    mycursor.execute("select bookname from available_books where quantity>0" )
    dd=mycursor.fetchall()
    def callback(*args):
            global abfd
            abfd=variable.get()
                         
    ab6=tkinter.OptionMenu(login3,variable,*dd)
    ab6.place(x=170,y=100)
    variable.trace("w",callback)

    
    ab3=tkinter.Label(login3,text="Qty:" ,font=("Ariel",10,"bold"),bg="light blue")
    ab3.place (x=50,y=200)
    ab4=tkinter.Entry(login3,width=20,font=("Ariel",10,))
    ab4.place(x=150,y=200)
    ab11=tkinter.Button(login3,text="Delete Quantity",font=("Ariel,10"),bg="yellow",command=submitd)
    ab11.place(x=150,y=300)
    ab5=tkinter.Label(login3,text="OR:" ,font=("Ariel",10,"bold"),bg="light blue")
    ab5.place (x=50,y=400)
    ab12=tkinter.Button(login3,text="Delete Book Record",font=("Ariel,10"),bg="yellow",command=submitdr)
    ab12.place(x=150,y=400)

#search books


def select3():
      #search by bookname
    def searchbb():
            def submitbb1():
                    book=abc2.get()
                    mycursor.execute("select * from Available_Books where bookname='{}'".format(book))
                    row1=mycursor.fetchone()
                    if row1 is not None:
                            book=row1[0]
                            genre=row1[1]
                            qty=row1[2]
                            author=row1[3]
                            price=row1[4]
                            logn2=tkinter.Tk()
                            logn2.geometry("500x500")
                            logn2.configure(bg="light blue")
                            l1=tkinter.Label(logn2,text="BOOK DETAILS",font=("Ariel",20,"bold"),bg="light blue")
                            l1.place (x=150,y=50)
                            ab1=tkinter.Label(logn2,text="Book Name ",font=("Ariel",10,"bold"),bg="light blue")
                            ab1.place (x=50,y=100)
                            bookLabel= tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")

                            bookLabel.config(text= book)
                            bookLabel.place(x=150,y=100)
                            ab3=tkinter.Label(logn2,text="Genre",font=("Ariel",10,"bold"),bg="light blue")
                            ab3.place (x=50,y=150)
                            ab4=tkinter.Label(logn2,text="",font=("Ariel",10),bg="light blue")
                            ab4.config(text=genre)
                            ab4.place(x=150,y=150)
                            ab5=tkinter.Label(logn2,text="Quantity",font=("Ariel",10,"bold"),bg="light blue")
                            ab5.place (x=50,y=200)
                            ab6=tkinter.Label(logn2,text="" ,font=("Ariel",10,),bg="light blue")
                            ab6.config(text=qty)
                            ab6.place(x=150,y=200)
                            ab7=tkinter.Label(logn2,text="Author",font=("Ariel",10,"bold"),bg="light blue")
                            ab7.place (x=50,y=250)
                            ab8=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                            ab8.config(text=author)
                            ab8.place(x=150,y=250)
                            ab9=tkinter.Label(logn2,text="Price",font=("Ariel",10,"bold"),bg="light blue")
                            ab9.place (x=50,y=300)
                            ab10=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                            ab10.config(text=price)
                            ab10.place(x=150,y=300)
                    else:
                                pup9=tkinter.Tk()
                                pup9.geometry("300x100")
                                pup9.configure(bg="white")
                                pup10=tkinter.Label(pup9,text="ENTER VALID BOOKNAME!",font=("Times New Roman",10,"bold"))
                                pup10.place(x=50,y=50) 
                            
                    

            log4=tkinter.Tk()
            log4.geometry("500x500")
            log4.configure(bg="light blue")
            abc1=tkinter.Label(log4,text="Book Name:",font=("Ariel",10,"bold"),bg="light blue")
            abc1.place (x=50,y=100)
            abc2=tkinter.Entry(log4,width=20,font=("Ariel",10,))
            abc2.place(x=150,y=100)
            abc11=tkinter.Button(log4,text="Submit",font=("Ariel,10"),bg="yellow",command=submitbb1)
            abc11.place(x=150,y=300)

            
                    
       #search by author     
    def searchba():
            def submitba1():
                    
               author=abc4.get()
               mycursor.execute("select * from Available_Books where author='{}'".format(author))
               row2=mycursor.fetchall()
               ct=int(mycursor.rowcount)
               
               if ct>0:
                   
                   logn2=tkinter.Tk()
                   logn2.geometry("750x500")
                   logn2.configure(bg="light blue")
                   n=20
                   label1=tkinter.Label(logn2,text="Book Name",font=("Times New Roman",10,"bold"),bg="light blue")
                   label1.place(x=50,y=0)
                   label2=tkinter.Label(logn2,text="Genre",font=("Times New Roman",10,"bold"),bg="light blue")
                   label2.place(x=250,y=0)
                   label3=tkinter.Label(logn2,text="Qty",font=("Times New Roman",10,"bold"),bg="light blue")
                   label3.place(x=375,y=0)
                   label4=tkinter.Label(logn2,text="Author",font=("Times New Roman",10,"bold"),bg="light blue")
                   label4.place(x=500,y=0)
                   label5=tkinter.Label(logn2,text="Price",font=("Times New Roman",10,"bold"),bg="light blue")
                   label5.place(x=650,y=0)



                   for j in row2:
                                       
                                        book=j[0]
                                        genre=j[1]
                                        qty=j[2]
                                        author=j[3]
                                        price=j[4]
                                        m=50
                                        n=(n+50)
                                        bookLabel= tkinter.Label(logn2,text="",font=("Ariel",10,))
                                        bookLabel.config(text= book)
                                        bookLabel.place(x=m, y=n)
                                        ab4=tkinter.Label(logn2,text="",font=("Ariel",10),bg="light blue")
                                        ab4.config(text=genre)
                                        ab4.place(x=m+200,y=n)
                                        ab6=tkinter.Label(logn2,text="" ,font=("Ariel",10,),bg="light blue")
                                        ab6.config(text=qty)
                                        ab6.place(x=(m+325),y=n)
                                        ab8=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                        ab8.config(text=author)
                                        ab8.place(x=(m+450),y=n)
                                        ab10=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                        ab10.config(text=price)
                                        ab10.place(x=(m+600),y=n)
                        
               else:
                   pup9=tkinter.Tk()
                   pup9.geometry("300x100")
                   pup9.configure(bg="white")
                   pup10=tkinter.Label(pup9,text="ENTER VALID AUTHOR!",font=("Times New Roman",10,"bold"))
                   pup10.place(x=50,y=50)      
                      
                            
                    
            log5=tkinter.Tk()
            log5.geometry("500x500")
            log5.configure(bg="lightblue")
            abc3=tkinter.Label(log5,text="Author Name:",font=("Ariel",10,"bold"),bg="light blue")
            abc3.place (x=50,y=100)
            abc4=tkinter.Entry(log5,width=20,font=("Ariel",10,))
            abc4.place(x=150,y=100)
            abc12=tkinter.Button(log5,text="Submit",font=("Ariel,10"),bg="yellow",command=submitba1)
            abc12.place(x=150,y=300)
#search by genre
    def searchbg():
            def submitbg1():

               genre=abc16.get()
               mycursor.execute("select * from Available_Books where genre='{}'".format(genre))
               row3=mycursor.fetchall()
               ct=int(mycursor.rowcount)
               if ct>0:
                   
                   logn2=tkinter.Tk()
                   logn2.geometry("700x500")
                   logn2.configure(bg="light blue")
                   n=20
                   label1=tkinter.Label(logn2,text="Book Name",font=("Times New Roman",10,"bold"),bg="light blue")
                   label1.place(x=50,y=0)
                   label2=tkinter.Label(logn2,text="Genre",font=("Times New Roman",10,"bold"),bg="light blue")
                   label2.place(x=250,y=0)
                   label3=tkinter.Label(logn2,text="Qty",font=("Times New Roman",10,"bold"),bg="light blue")
                   label3.place(x=375,y=0)
                   label4=tkinter.Label(logn2,text="Author",font=("Times New Roman",10,"bold"),bg="light blue")
                   label4.place(x=500,y=0)
                   label5=tkinter.Label(logn2,text="Price",font=("Times New Roman",10,"bold"),bg="light blue")
                   label5.place(x=650,y=0)



                   for j in row3:
                                        
                                        book=j[0]
                                        genre=j[1]
                                        qty=j[2]
                                        author=j[3]
                                        price=j[4]
                                        m=50
                                        n=(n+50)
                                        bookLabel= tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                        bookLabel.config(text= book)
                                        bookLabel.place(x=m, y=n)
                                        ab4=tkinter.Label(logn2,text="",font=("Ariel",10),bg="light blue")
                                        ab4.config(text=genre)
                                        ab4.place(x=m+200,y=n)
                                        ab6=tkinter.Label(logn2,text="" ,font=("Ariel",10,),bg="light blue")
                                        ab6.config(text=qty)
                                        ab6.place(x=(m+325),y=n)
                                        ab8=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                        ab8.config(text=author)
                                        ab8.place(x=(m+450),y=n)
                                        ab10=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                        ab10.config(text=price)
                                        ab10.place(x=(m+600),y=n)

               else:
                                pup9=tkinter.Tk()
                                pup9.geometry("300x100")
                                pup9.configure(bg="white")
                                pup10=tkinter.Label(pup9,text="ENTER VALID GENRE!",font=("Times New Roman",10,"bold"))
                                pup10.place(x=50,y=50) 
                    

            log6=tkinter.Tk()
            log6.geometry("500x500")
            log6.configure(bg="light blue")
            abc15=tkinter.Label(log6,text="Genre:",font=("Ariel",10,"bold"),bg="light blue")
            abc15.place (x=50,y=100)
            abc16=tkinter.Entry(log6,width=20,font=("Ariel",10,))
            abc16.place(x=150,y=100)
            abc17=tkinter.Button(log6,text="Submit",font=("Ariel,10"),bg="yellow",command=submitbg1)
            abc17.place(x=150,y=300)


            
            
            




    login4=tkinter.Tk()
    login4.geometry("500x500")
    login4.configure(bg="white")
    
    ab11=tkinter.Button(login4,text="Search by Book Name",font=("Ariel,10"),bg="yellow",command=searchbb)
    ab11.place(x=150,y=100)
    ab12=tkinter.Button(login4,text="Search by Author",font=("Ariel,10"),bg="yellow",command=searchba)
    ab12.place(x=150,y=300)
    ab13=tkinter.Button(login4,text="Search by Genre",font=("Ariel,10"),bg="yellow",command=searchbg)
    ab13.place(x=150,y=200)                         
                             


#staff details


#entering staff details
def select81():
                 def submit():
                        


                        global selection
                        
                        selection =(varr.get())
                        emp=ab2.get()
                        name=ab4.get()
                        
                        age=int(ab8.get())
                        phno=(ab10.get())
                        



                        mycursor.execute("select * from Staff_details where EmpID="+emp+"")
                        row=mycursor.fetchone()


                        if row is not None :

                                s2=tkinter.Tk()
                                s2.geometry("300x100")
                                s2.configure(bg="white")
                                s2=tkinter.Label(s2,text="Already a member...",font=("Ariel",10,"bold"))
                                s2.place(x=50,y=50)

                        elif selection :
                              
                               gender=selection
                               mycursor.execute("insert into Staff_details(EmpID,Name,Gender,Age,PhoneNumber) values('{}','{}','{}','{}','{}')".format(emp,name,gender,age,phno))
                               mydb.commit()
                               pup1=tkinter.Tk()
                               pup1.geometry("300x100")
                               pup1.configure(bg="white")
                               pup2= tkinter.Label(pup1,text="RECORD ADDED!",font=("Times New Roman",10,"bold"))
                               pup2.place(x=50,y=50)
                        else:
                               pup1=tkinter.Tk()
                               pup1.geometry("300x100")
                               pup1.configure(bg="white")
                               pup2= tkinter.Label(pup1,text="PLEASE SELECT GENDER!",font=("Times New Roman",10,"bold"))
                               pup2.place(x=50,y=50)

                           

                        
                 login9=tkinter.Tk()
                 login9.geometry("500x500")
                 login9.configure(bg="light blue")
                 ab1=tkinter.Label(login9,text="EmpID",font=("Ariel",10,"bold"),bg="light blue")
                 ab1.place (x=50,y=50)
                 ab2=tkinter.Entry(login9,width=20,font=("Ariel",10,))
                 ab2.place(x=150,y=50)
                 ab3=tkinter.Label(login9,text="Name",font=("Ariel",10,"bold"),bg="light blue")
                 ab3.place (x=50,y=100)
                 ab4=tkinter.Entry(login9,width=20,font=("Ariel",10))
                 ab4.place(x=150,y=100)
                 ab5=tkinter.Label(login9,text="Gender",font=("Ariel",10,"bold"),bg="light blue")
                 ab5.place (x=50,y=150)

                 

                 varr = tkinter.StringVar(login9)
                 
                 R1 = tkinter.Radiobutton(login9, text="Male", variable=varr, value='Male')
                 R1.place(x=150,y=150)
                 R2 = tkinter.Radiobutton(login9, text="Female", variable=varr, value='Female')
                 R2.place(x=250,y=150)
                 R1.select()
                 





                 ab7=tkinter.Label(login9,text="Age",font=("Ariel",10,"bold"),bg="light blue")
                 ab7.place (x=50,y=200)
                 ab8=tkinter.Entry(login9,width=20,font=("Ariel",10,))
                 ab8.place(x=150,y=200)
                 ab9=tkinter.Label(login9,text="Phone No.",font=("Ariel",10,"bold"),bg="light blue")
                 ab9.place (x=50,y=250)
                 ab10=tkinter.Entry(login9,width=20,font=("Ariel",10,))
                 ab10.place(x=150,y=250)
                 ab11=tkinter.Button(login9,text="Submit",font=("Ariel,10"),bg="yellow",command=submit)
                 ab11.place(x=250,y=300)



#search staff
def select91():
                 def staffs():
                       nam=tt.get()
                       mycursor.execute("select * from Staff_details where Name='{}'".format(nam))
                       row1=mycursor.fetchall()
                       ct=int(mycursor.rowcount)
                       
                       

                       if ct>0:
                         
                         logn2=tkinter.Tk()
                         logn2.geometry("850x500")
                         logn2.configure(bg="light blue")
                         n=20
                         label1=tkinter.Label(logn2,text="EmpID",font=("Times New Roman",10,"bold"),bg="light blue")
                         label1.place(x=50,y=0)
                         label2=tkinter.Label(logn2,text="Name",font=("Times New Roman",10,"bold"),bg="light blue")
                         label2.place(x=250,y=0)
                         label3=tkinter.Label(logn2,text="Gender",font=("Times New Roman",10,"bold"),bg="light blue")
                         label3.place(x=375,y=0)
                         label4=tkinter.Label(logn2,text="Age",font=("Times New Roman",10,"bold"),bg="light blue")
                         label4.place(x=500,y=0)
                         label5=tkinter.Label(logn2,text="Phn No.",font=("Times New Roman",10,"bold"),bg="light blue")
                         label5.place(x=650,y=0)
                         label6=tkinter.Label(logn2,text="Sale Made(in Rs.)",font=("Times New Roman",10,"bold"),bg="light blue")
                         label6.place(x=750,y=0)



                         for j in row1:
                                    emp=j[0]
                                    name=j[1]
                                    gender=j[2]
                                    age=j[3]
                                    phn=j[4]
                                    sale=j[5]
                                    m=50
                                    n=(n+50)
                                    bookLabel= tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                    bookLabel.config(text=emp)
                                    bookLabel.place(x=m, y=n)
                                    ab4=tkinter.Label(logn2,text="",font=("Ariel",10),bg="light blue")
                                    ab4.config(text=name)
                                    ab4.place(x=m+200,y=n)
                                    ab6=tkinter.Label(logn2,text="" ,font=("Ariel",10,),bg="light blue")
                                    ab6.config(text=gender)
                                    ab6.place(x=(m+325),y=n)
                                    ab8=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                    ab8.config(text=age)
                                    ab8.place(x=(m+450),y=n)
                                    ab10=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                    ab10.config(text=phn)
                                    ab10.place(x=(m+600),y=n)
                                    ab11=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                    ab11.config(text=sale)
                                    ab11.place(x=(m+700),y=n)
                       else:
                           pup1=tkinter.Tk()
                           pup1.geometry("300x100")
                           pup1.configure(bg="white")
                           pup2= tkinter.Label(pup1,text="ENTER VALID NAME!",font=("Times New Roman",10,"bold"))
                           pup2.place(x=50,y=50)
                         


                 login10=tkinter.Tk()
                 login10.geometry("500x500")
                 login10.configure(bg="light blue")
                 bb=tkinter.Label(login10, text="Staff Name",font=("Ariel",10,"bold"),bg="light blue")
                 bb.place(x=20,y=100)
                 tt=tkinter.Entry(login10, width=25,font=("Ariel",10,))
                 tt.place(x=120 ,y=100)
                 nn=tkinter.Button(login10,text="SELECT",font=("Ariel,10"),bg="yellow",command=staffs)
                 nn.place(x=70,y=200)
                
#del staff
def select16():
                 def staffd():

                            pno=str(tt.get())
                            
                            mycursor.execute("select name from staff_details where EmpID='{}'".format(pno))
                            row1=mycursor.fetchone()
                            if row1 is not None:
                                
                                def yes():
                                        mycursor.execute("delete from staff_details where PhoneNumber='{}'".format(pno))
                                        mydb.commit()
                                        pup1=tkinter.Tk()
                                        pup1.geometry("300x100")
                                        pup1.configure(bg="white")
                                        pup2= tkinter.Label(pup1,text="RECORD DELETED!",font=("Times New Roman",10,"bold"))
                                        pup2.place(x=50,y=50)
                                        pup5.destroy()
                                        login10.destroy()
                                def no():
                                        pup5.destroy()
                                        
                                        
                                pup5=tkinter.Tk()
                                pup5.geometry("300x130")
                                pup5.configure(bg="light blue")
                                pup6=tkinter.Label(pup5,text="DELETE RECORD OF: ",font=("Times New Roman",10),bg="light blue")
                                pup6.place(x=50,y=50)
                                pup7=tkinter.Label(pup5,text="",font=("Times New Roman",10,"bold"),bg="light blue")
                                pup7.configure(text=row1)
                                pup7.place(x=200,y=50)
                                b6=tkinter.Button(pup5,text="YES",font=("Ariel,10"),bg="red",command=yes)
                                b6.place(x=50,y=90)
                                b7=tkinter.Button(pup5,text="NO",font=("Ariel,10"),bg="yellow",command=no)
                                b7.place(x=110,y=90)
                                
                            else:
                                pup9=tkinter.Tk()
                                pup9.geometry("300x100")
                                pup9.configure(bg="white")
                                pup10=tkinter.Label(pup9,text="ENTER VALID PHONE NUMBER!",font=("Times New Roman",10,"bold"))
                                pup10.place(x=50,y=50)
                         
                 login10=tkinter.Tk()
                 login10.geometry("500x500")
                 login10.configure(bg="light blue")
                 bb=tkinter.Label(login10, text="Enter EmpID:",font=("Ariel",10,"bold"),bg="light blue")
                 bb.place(x=20,y=100)
                 tt=tkinter.Entry(login10, width=25,font=("Ariel",10,))
                 tt.place(x=100 ,y=100)
                 nm=tkinter.Button(login10,text="DELETE RECORD",font=("Ariel,10"),bg="yellow",command=staffd)
                 nm.place(x=70,y=200)
#view staff rec        
def select15():
                         mycursor.execute("select * from staff_details")
                         row1=mycursor.fetchall()
                         ct=int(mycursor.rowcount)
                         logn2=tkinter.Tk()
                         logn2.geometry("850x500")
                         logn2.configure(bg="light blue")
                         n=20
                         label1=tkinter.Label(logn2,text="EmpID",font=("Times New Roman",10,"bold"),bg="light blue")
                         label1.place(x=50,y=0)
                         label2=tkinter.Label(logn2,text="Name",font=("Times New Roman",10,"bold"),bg="light blue")
                         label2.place(x=250,y=0)
                         label3=tkinter.Label(logn2,text="Gender",font=("Times New Roman",10,"bold"),bg="light blue")
                         label3.place(x=375,y=0)
                         label4=tkinter.Label(logn2,text="Age",font=("Times New Roman",10,"bold"),bg="light blue")
                         label4.place(x=500,y=0)
                         label5=tkinter.Label(logn2,text="Phn No.",font=("Times New Roman",10,"bold"),bg="light blue")
                         label5.place(x=650,y=0)
                         label6=tkinter.Label(logn2,text="Sale Made(in Rs.)",font=("Times New Roman",10,"bold"),bg="light blue")
                         label6.place(x=750,y=0)



                         for j in row1:
                                    emp=j[0]
                                    name=j[1]
                                    gender=j[2]
                                    age=j[3]
                                    phn=j[4]
                                    sale=j[5]
                                    m=50
                                    n=(n+50)
                                    bookLabel= tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                    bookLabel.config(text=emp)
                                    bookLabel.place(x=m, y=n)
                                    ab4=tkinter.Label(logn2,text="",font=("Ariel",10),bg="light blue")
                                    ab4.config(text=name)
                                    ab4.place(x=m+200,y=n)
                                    ab6=tkinter.Label(logn2,text="" ,font=("Ariel",10,),bg="light blue")
                                    ab6.config(text=gender)
                                    ab6.place(x=(m+325),y=n)
                                    ab8=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                    ab8.config(text=age)
                                    ab8.place(x=(m+450),y=n)
                                    ab10=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                    ab10.config(text=phn)
                                    ab10.place(x=(m+600),y=n)
                                    ab11=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                                    ab11.config(text=sale)
                                    ab11.place(x=(m+700),y=n)

def select4(): 
                if barsoom=='admin':
                    s2=tkinter.Tk()
                    s2.geometry("500x600")
                    s2.configure(bg="light blue")
                    HH=tkinter.Label(s2,text="STAFF DETAILS",font=("Ariel",20,"bold"),bg="light blue")
                    HH.place (x=150,y=50)
                    
                    Z=tkinter.Label(s2,text="SEARCH RECORDS",font=("Ariel",10,"bold"),bg="light blue")
                    Z.place(x=10,y=250)
                    X=tkinter.Button(s2,text="SELECT",font=("Ariel,10"),bg="yellow",command=select91)
                    X.place(x=250,y=250)
                    Z=tkinter.Label(s2,text="VIEW RECORDS",font=("Ariel",10,"bold"),bg="light blue")
                    Z.place(x=10,y=350)
                    X=tkinter.Button(s2,text="SELECT",font=("Ariel,10"),bg="yellow",command=select15)
                    X.place(x=250,y=350)
                    
                    Z1=tkinter.Label(s2,text="DELETE RECORDS",font=("Ariel",10,"bold"),bg="light blue")
                    Z1.place(x=10,y=400)
                    X1=tkinter.Button(s2,text="SELECT",font=("Ariel,10"),bg="yellow",command=select16)
                    X1.place(x=250,y=400)
                    A=tkinter.Label(s2,text="ADD RECORD",font=("Ariel",10,"bold"),bg="light blue")
                    A.place(x=10,y=150)
                    S=tkinter.Button(s2,text="SELECT",font=("Ariel,10"),bg="yellow",command=select81)
                    S.place(x=250,y=150)
                else:
                    info2=tkinter.Tk()
                    info2.title('IMPORTANT')
                    info2.attributes('-topmost',True)
                    info2.geometry("300x200")
                    info2.configure(bg="white")
                    info3=tkinter.Label(info2,text="Please login as admin to perform ",font=("Ariel",10,"bold"))
                    info3.place(x=50,y=50)
                    info3=tkinter.Label(info2,text="ADD and DELETE STAFF operations. ",font=("Ariel",10,"bold"))
                    info3.place(x=50,y=70)



#Available book



def select6():
                 
                         
                         mycursor.execute("select * from Available_Books where Quantity!=0")
                         row1=mycursor.fetchall()
                         ct=int(mycursor.rowcount)
                         login11=tkinter.Tk()
                         login11.title('Available Books')
                         login11.geometry("850x500")
                         login11.configure(bg="light blue")     
                         n=20
                         label1=tkinter.Label(login11,text="Name",font=("Times New Roman",10,"bold"),bg="light blue")
                         label1.place(x=50,y=0)
                         label2=tkinter.Label(login11,text="Genre",font=("Times New Roman",10,"bold"),bg="light blue")
                         label2.place(x=250,y=0)
                         label3=tkinter.Label(login11,text="quantity",font=("Times New Roman",10,"bold"),bg="light blue")
                         label3.place(x=375,y=0)
                         label4=tkinter.Label(login11,text="author",font=("Times New Roman",10,"bold"),bg="light blue")
                         label4.place(x=500,y=0)
                         label5=tkinter.Label(login11,text="price",font=("Times New Roman",10,"bold"),bg="light blue")
                         label5.place(x=650,y=0)



                         for j in row1:
                                    
                                    name=j[0]
                                    genre=j[1]
                                    quantity=j[2]
                                    author=j[3]
                                    price=j[4]
                                    m=50
                                    n=(n+50)
                                    bookLabel= tkinter.Label(login11,text="",font=("Ariel",10,),bg="light blue")
                                    bookLabel.config(text=name)
                                    bookLabel.place(x=m, y=n)
                                    ab4=tkinter.Label(login11,text="",font=("Ariel",10),bg="light blue")
                                    ab4.config(text=genre)
                                    ab4.place(x=m+200,y=n)
                                    ab6=tkinter.Label(login11,text="" ,font=("Ariel",10,),bg="light blue")
                                    ab6.config(text=quantity)
                                    ab6.place(x=(m+325),y=n)
                                    ab8=tkinter.Label(login11,text="",font=("Ariel",10,),bg="light blue")
                                    ab8.config(text=author)
                                    ab8.place(x=(m+450),y=n)
                                    ab10=tkinter.Label(login11,text="",font=("Ariel",10,),bg="light blue")
                                    ab10.config(text=price)
                                    ab10.place(x=(m+600),y=n)

                 
                       


#Sell Record
                 


def select5():
        
                
        def sellhist():
                
                mycursor.execute("select * from Sell_rec" )
                row1=mycursor.fetchall()
                ct=int(mycursor.rowcount)
                logn2=tkinter.Tk()
                logn2.title('Sales')
                logn2.geometry("900x500")
                logn2.configure(bg="light blue")
                n=20
                label1=tkinter.Label(logn2,text="Customer Name",font=("Times New Roman",10,"bold"),bg="light blue")
                label1.place(x=50,y=0)
                label2=tkinter.Label(logn2,text="Phone Number",font=("Times New Roman",10,"bold"),bg="light blue")
                label2.place(x=200,y=0)
                label3=tkinter.Label(logn2,text="Book Name",font=("Times New Roman",10,"bold"),bg="light blue")
                label3.place(x=350,y=0)
                label4=tkinter.Label(logn2,text="Qty",font=("Times New Roman",10,"bold"),bg="light blue")
                label4.place(x=550,y=0)
                label5=tkinter.Label(logn2,text="Total Amt",font=("Times New Roman",10,"bold"),bg="light blue")
                label5.place(x=650,y=0)
                label5=tkinter.Label(logn2,text="Cashier",font=("Times New Roman",10,"bold"),bg="light blue")
                label5.place(x=775,y=0)



                for j in row1:
                            
                            
                            
                            cname=j[0]
                            phn=j[1]
                            bname=j[2]
                            qty=j[3]
                            amt=j[4]
                            cash=j[5]
                            m=50
                            n=(n+50)
                            bookLabel= tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                            bookLabel.config(text= cname)
                            bookLabel.place(x=m, y=n)
                            ab4=tkinter.Label(logn2,text="",font=("Ariel",10),bg="light blue")
                            ab4.config(text=phn)
                            ab4.place(x=m+150,y=n)
                            ab6=tkinter.Label(logn2,text="" ,font=("Ariel",10,),bg="light blue")
                            ab6.config(text=bname)
                            ab6.place(x=(m+300),y=n)
                            ab8=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                            ab8.config(text=qty)
                            ab8.place(x=(m+500),y=n)
                            ab10=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                            ab10.config(text=amt)
                            ab10.place(x=(m+600),y=n)
                            ab11=tkinter.Label(logn2,text="",font=("Ariel",10,),bg="light blue")
                            ab11.config(text=cash)
                            ab11.place(x=(m+725),y=n)
                    
        #reset sell records        
        def reset():
                if barsoom=='admin':
                    def yes():
                         mycursor.execute("delete from sell_rec")
                         mycursor.execute("update staff_details set sale_amt=0")
                        
                         
                         mydb.commit()
                         pup9=tkinter.Tk()
                         pup9.geometry("300x100")
                         pup9.configure(bg="white")
                         pup10=tkinter.Label(pup9,text="SUCCESSFUL!",font=("Times New Roman",20,"bold"))
                         pup10.place(x=50,y=50)
                         
                         selres.destroy()
                         
                        
                    def no():
                            selres.destroy()
                            
                            
                            
                    selres=tkinter.Tk()
                    selres.geometry("180x120")
                    selres.configure(bg="white")
                    con=tkinter.Label(selres, text="Confirm?",font=("Ariel",10,"bold"))
                    con.place(x=60, y=10)
                    b6=tkinter.Button(selres,text="YES",font=("Ariel,10"),bg="red",command=yes)
                    b6.place(x=10,y=70)
                    b7=tkinter.Button(selres,text="NO",font=("Ariel,10"),bg="yellow",command=no)
                    b7.place(x=110,y=70)
                else:

                    info2=tkinter.Tk()
                    info2.title('ERROR')
                    info2.attributes('-topmost',True)
                    info2.geometry("300x100")
                    info2.configure(bg="white")
                    info3=tkinter.Label(info2,text="Only admin can perform: ",font=("Ariel",10,"bold"))
                    info3.place(x=50,y=50)
                    info3=tkinter.Label(info2,text="RESET SALE RECORD ",font=("Ariel",10,"bold"))
                    info3.place(x=50,y=70)
                
                
                
                
        login6=tkinter.Tk()
        login6.geometry("500x500")
        login6.configure(bg="light blue")
        l12=tkinter.Label(login6,text="Sale Record",font=("Ariel",20,"bold"),bg="light blue")
        l12.place (x=150,y=0)
        
        l12=tkinter.Button(login6,text="View Sales History",font=("Ariel",20,"bold"),bg="light blue",command=sellhist)
        l12.place (x=50,y=150)
        l12=tkinter.Button(login6,text="Reset Sale History",font=("Ariel",20,"bold"),bg="light blue",command=reset)
        l12.place (x=50,y=250)



#Total Income



def select7():
        
       mycursor.execute("select SUM(totalamt) from sell_rec" )
       row1=mycursor.fetchone()
       income=row1[0]
       ct=int(mycursor.rowcount)
       logn2=tkinter.Tk()
       logn2.geometry("500x200")
       logn2.configure(bg="light blue")
       n=20
       label1=tkinter.Label(logn2,text="TOTAL INCOME:",font=("Times New Roman",15,"bold"),bg="light blue")
       label1.place(x=50,y=50)
                



       
       bookLabel= tkinter.Label(logn2,text="",font=("Ariel",15,))
       bookLabel.config(text= income)
       bookLabel.place(x=250, y=50)


#OUT OF STOCK
def select10():
                         mycursor.execute("select * from Available_Books where Quantity=0")
                         row1=mycursor.fetchall()
                         ct=int(mycursor.rowcount)
                         login11=tkinter.Tk()
                         login11.geometry("850x500")
                         login11.configure(bg="light blue")     
                         n=20
                         label1=tkinter.Label(login11,text="Name",font=("Times New Roman",10,"bold"),bg="light blue")
                         label1.place(x=50,y=0)
                         label2=tkinter.Label(login11,text="Genre",font=("Times New Roman",10,"bold"),bg="light blue")
                         label2.place(x=250,y=0)
                         label3=tkinter.Label(login11,text="quantity",font=("Times New Roman",10,"bold"),bg="light blue")
                         label3.place(x=375,y=0)
                         label4=tkinter.Label(login11,text="author",font=("Times New Roman",10,"bold"),bg="light blue")
                         label4.place(x=500,y=0)
                         label5=tkinter.Label(login11,text="price",font=("Times New Roman",10,"bold"),bg="light blue")
                         label5.place(x=650,y=0)



                         for j in row1:
                                    print(j)
                                    name=j[0]
                                    genre=j[1]
                                    quantity=j[2]
                                    author=j[3]
                                    price=j[4]
                                    m=50
                                    n=(n+50)
                                    bookLabel= tkinter.Label(login11,text="",font=("Ariel",10,),bg="light blue")
                                    bookLabel.config(text=name)
                                    bookLabel.place(x=m, y=n)
                                    ab4=tkinter.Label(login11,text="",font=("Ariel",10),bg="light blue")
                                    ab4.config(text=genre)
                                    ab4.place(x=m+200,y=n)
                                    ab6=tkinter.Label(login11,text="" ,font=("Ariel",10,),bg="light blue")
                                    ab6.config(text=quantity)
                                    ab6.place(x=(m+325),y=n)
                                    ab8=tkinter.Label(login11,text="",font=("Ariel",10,),bg="light blue")
                                    ab8.config(text=author)
                                    ab8.place(x=(m+450),y=n)
                                    ab10=tkinter.Label(login11,text="",font=("Ariel",10,),bg="light blue")
                                    ab10.config(text=price)
                                    ab10.place(x=(m+600),y=n)


#Billing Tab
def select20():
                def sell():
                        cstmr=ab2.get()
                        phn=ab4.get()
                        
                        y=len(abg)
                        
                        abcd=abg[2:y-3]
                        
                        
                        bookn= abcd
                            
                        
                        
                        quant=int(ab8.get())
                        

                        mycursor.execute("select * from Available_Books where bookname='{}'".format(bookn))
                        row=mycursor.fetchone()
                        if row is not None:
                                
                                mycursor.execute("select quantity from Available_books where bookname='{}'".format(bookn))
                                check=mycursor.fetchone()
                                num=int(check[0])
                                rescalc=int(num-quant)
                                if rescalc>=0:
                                        
                                        def pay():
                                                        mycursor.execute("update Available_Books set quantity = quantity - '{}' where bookname='{}'".format(quant,bookn))
                                                        mydb.commit()
                        
                                

                                                        mycursor.execute("insert into Sell_rec(CustomerName,PhoneNumber,BookName,Quantity,TotalAmt,Cashier) values('{}','{}','{}','{}','{}','{}')".format(cstmr,phn,bookn,quant,jasoom,barsoom))
                                                        mycursor.execute("update staff_details Set Sale_Amt= Sale_Amt + '{}' where Name= '{}'".format(jasoom,barsoom))
                                                        
                                                        mydb.commit()
                                                        pup9=tkinter.Tk()
                                                        pup9.geometry("300x100")
                                                        pup9.configure(bg="white")
                                                        pup10=tkinter.Label(pup9,text="SUCCESSFUL!",font=("Times New Roman",20,"bold"))
                                                        pup9.attributes("-topmost", True)
                                                        pup10.place(x=50,y=50)
                                                        pup1.destroy()
                                                        addr.destroy()
                                                        promptt()
                                                        select20()
                                                        
                                                
                                        def canc():
                                                pup1.destroy()

                                        mycursor.execute("select price from available_books where bookname='{}'".format(bookn))
                                        tup=mycursor.fetchone()
                                        
                                        
                                        
                                                
                                        price=int(tup[0])
                                        global jasoom
                                        jasoom=int(price*quant)
                                        pup1=tkinter.Tk()
                                        pup1.geometry("350x200")
                                        pup1.configure(bg="white")
                                        pup2=tkinter.Label(pup1,text="Total Amount is: ",font=("Times New Roman",20,"bold"))
                                        pup2.place(x=10,y=50)
                                        pup3=tkinter.Label(pup1,text="",font=("Times New Roman",20,"bold"))
                                        pup3.configure(text=jasoom)
                                        pup3.place(x=250,y=50)
                                        but11=tkinter.Button(pup1,text="PAID",font=("Ariel,10"),bg="green",command=pay)
                                        but11.place(x=50,y=150)
                                        but11=tkinter.Button(pup1,text="CANCEL",font=("Ariel,10"),bg="red",command=canc)
                                        but11.place(x=150,y=150)
                                        


                                        
                                        
                                        
                                        
                                        
                                                
                                else:
                                        pup9=tkinter.Tk()
                                        pup9.geometry("300x100")
                                        pup9.configure(bg="white")
                                        pup10=tkinter.Label(pup9,text="INSUFFICIENT QTY!",font=("Times New Roman",15,"bold"))
                                        pup10.place(x=50,y=50)
                                        promptt()
                                        
                        else:
                                pup9=tkinter.Tk()
                                pup9.geometry("300x100")
                                pup9.configure(bg="white")
                                pup10=tkinter.Label(pup9,text="BOOK DOESN'T EXIST!",font=("Times New Roman",10,"bold"))
                                pup10.place(x=50,y=50)          

                          
                                
                         
                                
                addr=tkinter.Tk()
                addr.focus_force()
                addr.geometry("500x500")
                addr.configure(bg="light blue")
                ab1=tkinter.Label(addr,text="Customer name ",font=("Ariel",10,"bold"),bg="light blue")
                ab1.place (x=50,y=50)
                ab2=tkinter.Entry(addr,width=20,font=("Ariel",10,))
                ab2.place(x=170,y=50)
                ab3=tkinter.Label(addr,text="Phone Number",font=("Ariel",10,"bold"),bg="light blue")
                ab3.place (x=50,y=100)
                ab4=tkinter.Entry(addr,width=20,font=("Ariel",10))
                ab4.place(x=170,y=100)
                ab5=tkinter.Label(addr,text="Book Name",font=("Ariel",10,"bold"),bg="light blue")
                ab5.place (x=50,y=150)
                mycursor.execute("select bookname from available_books where quantity>0")
                dd=mycursor.fetchall()
                variable = tkinter.StringVar(addr)
                variable.set('Select a Book') # default value
                def callback(*args):
                         global abg
                         abg=variable.get()
                         
                ab6=tkinter.OptionMenu(addr,variable,*dd)
                ab6.place(x=170,y=150)
                variable.trace("w",callback)
                
                
                ab7=tkinter.Label(addr,text="Quantity",font=("Ariel",10,"bold"))
                ab7.place (x=50,y=200)
                ab8=tkinter.Entry(addr,width=20,font=("Ariel",10,))
                ab8.place(x=170,y=200)
                
                
                ab11=tkinter.Button(addr,text="SUBMIT",font=("Ariel,10"),bg="yellow",command=sell)
                ab11.place(x=250,y=300)


#check quantity func
def promptt():
                mycursor.execute("select bookname,quantity from available_books where quantity<=5")
                rowz=mycursor.fetchall()
                if len(rowz)==0:
                               zbc=25
                elif len(rowz)!=0:
                         def ok():
                                 login11.destroy()
                         login11=tkinter.Tk()
                         login11.geometry("400x400")
                         login11.configure(bg="light blue")     
                         n=70
                         label1=tkinter.Label(login11,text="Name",font=("Times New Roman",10,"bold"),bg="light blue")
                         label1.place(x=50,y=50)
                         label2=tkinter.Label(login11,text="Quantity",font=("Times New Roman",10,"bold"),bg="light blue")
                         label2.place(x=250,y=50)
                         labelz=tkinter.Label(login11,text="Books to be ReOrdered",font=("Times New Roman",15,"bold"),bg="light blue")
                         labelz.place(x=50, y=0)
                         
                         
                         for j in rowz:
                                    
                                    name=j[0]
                                    quantity=j[1]
                                    
                                    m=50
                                    n=(n+50)
                                    bookLabel= tkinter.Label(login11,text="",font=("Ariel",10,))
                                    bookLabel.config(text=name)
                                    bookLabel.place(x=m, y=n)
                                    ab4=tkinter.Label(login11,text="",font=("Ariel",10))
                                    ab4.config(text=quantity)
                                    ab4.place(x=m+200,y=n)

                         okb=tkinter.Button(login11,text="OK",font=("Times New Roman",15,"bold"),command=ok)
                         okb.place(x=100, y=n+100)

                         
                        
                               

        
        









