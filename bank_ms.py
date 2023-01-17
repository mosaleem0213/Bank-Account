import mysql.connector as e
con=e.connect(
    host="localhost",
    user="root",
    passwd="####",
    database="bank"
)
cursor=con.cursor()
def account():
    try:
        print("")
        print("<< MAKE AN NEW ACCOUNT FOR NEW USER >>\n")
        name=input("Enter Account Holder Name: ")
        pan=input("Enter Pan Card Number: ")
        dob=input("Enter Date Of Birth: ")
        phone=input("Enter Mobile Number: ")
        addrs=input("Enter Parmanent Address: ")
        opnblc=int(input("Enter Amount For Openning Account: "))
        acnt=input("Enter New Account Number: ")
        data=(name,pan,dob,phone,addrs,opnblc,acnt)
        data2=(name,acnt,opnblc)
        query="insert into account values(%s,%s,%s,%s,%s,%s,%s)"
        query2="insert into amount values(%s,%s,%s)"
        cursor=con.cursor()
        cursor.execute(query,data)
        cursor.execute(query2,data2)
        con.commit()
        print("ACCOUNT OPEN SUCCESSFULLY...")
    except Exception as e:
        print(e)
        print(" \nPLEASE ENTERED RIGHT ACCOUNT NUMBER  ")
        print("-"*50)


def depost():
    print("")
    print("<< DEPOSITE MONEY >>\n")
    amnt=int(input("Enter Amount Balance: "))
    try:
        acnt=input("Enter Account Number: ")
        data=(acnt,)
        query="select balance from amount where acount=%s"
        cursor=con.cursor()
        cursor.execute(query,data)
        show=cursor.fetchone()
        total=show[0]+amnt
        data=(total,acnt)
        query="update amount set balance = %s where acount=%s"
        cursor.execute(query,data)
        con.commit()
        print("Amount Deposite Successfully...")
    except:
        print(" \nPLEASE ENTERED RIGHT ACCOUNT NUMBER  ")
        print("-"*50)

def withdraw():
    print("")
    print("<< WITHDRAW MONEY >>\n")
    amnt=int(input("Enter Amount Balance: "))
    try:
        acnt=input("Enter Account Number: ")
        data=(acnt,)
        query="select balance from amount where acount=%s"
        cursor=con.cursor()
        cursor.execute(query,data)
        show=cursor.fetchone()
        #This line is for amount 
        if show[0] >= amnt:
            total=show[0]-amnt
            data=(total,acnt)
            query="update amount set balance = %s where acount=%s"
            cursor.execute(query,data)
            con.commit()
            print("Amount Withdraw Successfully...")
        else:
            print("Sorry! You don't have sufficient Balance")
    except Exception as e:
        print(" \nPLEASE ENTERED RIGHT ACCOUNT NUMBER  ", e)
        print("-"*50)
   
def balance():
    print("")
    print("<< CHECK BALANCE >>\n")
    try:
        acnt=input("Enter Account Number: ")
        data=(acnt,)
        query="select balance from amount where acount=%s"
        cursor=con.cursor()
        cursor.execute(query,data)
        total=cursor.fetchone()
        print(f" Total Balance Of Account Number {acnt} is = {total[0]}")
    except:
        print(" \nPLEASE ENTERED RIGHT ACCOUNT NUMBER  ")
        print("-"*50)
    
def showdtls():
    print("")
    print("<< SHOW ACCOUNT DETAILS >>\n")
    try:
        acnt=input("Enter Account Number: ")
        data=(acnt,)
        query="select* from account where acount=%s"
        cursor=con.cursor()
        cursor.execute(query,data)
        details=cursor.fetchone()
        for i in details:
            print(i,end=" ")
    except:
        print(" \nPLEASE ENTERED RIGHT ACCOUNT NUMBER  ")
        print("-"*50)
        
def close():
    print("")
    print("<< CLOSE ACCOUNT >>\n")
    try:
        acnt=input("Enter Account Number For Close Account:")
        data=(acnt,)
        query="delete from account where acount=%s"
        query1="delete from amount where acount=%s"
        cursor=con.cursor()
        cursor.execute(query,data)
        cursor.execute(query1,data)
        con.commit()
        print("Account Close Successfully..")
    except:
        print(" \nPLEASE ENTERED RIGHT ACCOUNT NUMBER  ")
        print("-"*50)
   

def bank():
    print("")
    print("\t-----THIS IS BANK OF NEORIA HUSSAINPUR-----\n")
    
    while True:
  
        print(" Press 1 For Create New Account.. ")
        print(" Press 2 For Deposite Money.. ")
        print(" Press 3 For Withdraw Money.. ")
        print(" Press 4 For Check Account Balance.. ")
        print(" Press 5 For Check Account Details.. ")
        print(" Press 6 For Close Account.. ")
        print(" Press 7 For Quite...... \n")
        x=int(input("Choce an One Opration: "))
        if x==1:
            account()
        elif x==2:
            depost()
        elif x==3:
            withdraw()
        elif x==4:
            balance()
        elif x==5:
            showdtls()
        elif x==6:
            close()
        elif x==7:
            break
        else:
            print("Sorry Please Enter Right Option...")

bank()