import pickle
import os
def customerinput():
    l=[]
    print("Enter the following details of the customer:- ")
    accountno=int(input("Enter Account Number of the customer: "))
    name=input("Enter the name of the customer:")
    mob=int(input("Enter mobile no: "))
    email=input("Enter Email-ID of the customer: ")
    address=input("Enter Address: ")
    balance=float(input("Enter balance of the customer: "))
    l=[accountno,name,mob,email,address,balance]
    f=open("customer.dat","ab")
    pickle.dump(l,f)
    print("Record added successfully...")
    f.close()
def customeroutput():
    f=open("customer.dat","rb")
    if os.stat("customer.dat").st_size !=0:
        print("All Customer details are as follows:")
    else:
        print ("File is empty.")
    try:
        while True:
            l=pickle.load(f)
            print(l)
    except:
        f.close()
def customersearch():
    customeraccountno=int(input("Enter the Account no. whose record is to be searched: "))
    f=open("customer.dat","rb")
    found=False
    try:
        while True:
            l=pickle.load(f)
            if l[0]==customeraccountno:
                print("The given Account no record is: \n",l)
                found=True
    except EOFError:
        if found==False:
            print("No such Account no exists in database.")
        else:
            print("Customer found and the details as shown as above.")
            f.close()
def customerupdate():
    customeraccountno=int(input("Enter the customer Account no whose record to be update: "))
    f1=open("customer.dat","rb+")
    f2=open("customer1.dat","wb")
    found=False
    try:
        while True:
            l=pickle.load(f1)
            if l[0]==customeraccountno:
                l[0]=int(input("Enter new Accountno: "))
                l[1]=input("Enter the new Customer Name: ")
                l[2]=int(input("Enter new Mobile Number: "))
                l[3]=input("Enter new Email-ID address: ")
                l[4]=input("Enter new address: ")
                l[5]=float(input("Enter new balance: "))
                pickle.dump(l,f2)
                print(l)
                found=True
            else:
                pickle.dump(l,f2)
    except EOFError:
        if found==False:
            print("No such Account no exist.")
            f1.close()
            f2.close()
        else:
            f1.close()
            f2.close()
            print("Customer found and updated as above given information.")
    os.remove("customer.dat")
    os.rename("customer1.dat","customer.dat")
def customerdelete():
    customeraccountno=int(input("Enter the Account no of cutomer whose record is to be deleted:"))
    f1=open("customer.dat","rb+")
    f2=open("customer1.dat","wb")
    found=False
    try:
        while True:
            l=[]
            l=pickle.load(f1)
            if l[0]==customeraccountno:
                print("Deleted record is:")
                print(l)
                del l
                found=True
            else:
                pickle.dump(l,f2)
    except EOFError:
        if found==False:
            print("No such account no Exists. ")
            f1.close()
            f2.close()
        else:
            f1.close()
            f2.close()
            print("Customer found and deleted as above...")
    os.remove("customer.dat")
    os.rename("customer1.dat","customer.dat")
print("*******************************************************************************************")
print("                      WELCOME TO BANK RECORDS MANAGEMENT SYSTEM                          ")  
print("*******************************************************************************************")
while True:
    print("Type 1 to insert record")
    print("Type 2 to display record")
    print("Type 3 to search record")
    print("Type 4 to update record")
    print("Type 5 to delete record")
    print("Type 6 to exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        customerinput()
    elif choice==2:
        customeroutput()
    elif choice==3:
        customersearch()
    elif choice==4:
        customerupdate()
    elif choice==5:
        customerdelete()
    elif choice==6:
        break
    else:
        continue
