#
import os
import time
import datetime
import mysql.connector as mysql
current_user=0
current_admin=0
user_details = [
    {'user_id': 1000, 'user_name': 'default_0', 'pass': 'default_0'},
    {'user_id': 1001, 'user_name': 'default_1', 'pass': 'default_1'},
    {'user_id': 1002, 'user_name': 'default_2', 'pass': 'default_2'},
    {'user_id': 1003, 'user_name': 'default_3', 'pass': 'default_3'},
    {'user_id': 1004, 'user_name': 'default_4', 'pass': 'default_4'}
]

admin_details = [
    {'admin_id': 2000, 'admin_pass': 'admin_0'},
    {'admin_id': 2001, 'admin_pass': 'admin_1'},
    {'admin_id': 2002, 'admin_pass': 'admin_2'},
    {'admin_id': 2003, 'admin_pass': 'admin_3'},
    {'admin_id': 2004, 'admin_pass': 'admin_4'}
]

book_details = [
    {'book_id': 3000, 'book_name': 'book_0', 'borrow_date': None, 'return_date': None, 'Status': 'not_borrowed'},
    {'book_id': 3001, 'book_name': 'book_1', 'borrow_date': None, 'return_date': None, 'Status': 'not_borrowed'},
    {'book_id': 3002, 'book_name': 'book_2', 'borrow_date': None, 'return_date': None, 'Status': 'not_borrowed'},
    {'book_id': 3003, 'book_name': 'book_3', 'borrow_date': None, 'return_date': None, 'Status': 'not_borrowed'},
    {'book_id': 3004, 'book_name': 'book_4', 'borrow_date': None, 'return_date': None, 'Status': 'not_borrowed'}
]

auth=False
def user_auth():
    global auth
    global current_user
    while auth is False:
        print("----User Authentication:----",end="\n")
        print("1.New User")
        print('2.Login')
        user_choice=int(input("Enter:"))
        if(user_choice==1):
            print("not ready")
        elif(user_choice==2):    
            usr=input("Enter Username:")

            pwd=input("Enter password:")

            for i in user_details:
                if(i['user_name']==usr and i['pass']==pwd):
                    auth=True
                    print(f"{usr} has been given access to Library")
                    current_user=usr
                    input("Press ENTER")
                    time.sleep(2)
                    os.system('cls')
                    break
            if(auth==False):
                print('User not found...')
                input('Please Try Again.(Press Enter)')
                os.system('cls')

def admin_auth():
    global admin
    global current_admin
    print("----Admin Authentication:----",end="\n")   
    admin_id=input("Enter Adminstrator ID:")
    admin_pwd=input("Enter Administrator password:")
    for i in user_details:
            if(i['admin_id']==admin_id and i['admin_pass']==admin_pwd):
                auth=True
                print(f"Admin no:{admin_id} has been given access to Library")
                current_admin=admin_id
                input("Press ENTER")
                time.sleep(2)
                os.system('cls')
                break
    if(auth==False):
        print('Admin not found...')
        input('Please Try Again.(Press Enter)')
        os.system('cls')

def book_functions():
    global module_choice
    global current_admin
    global current_user

    print(f"Hello {'USER '+current_user if module_choice==2 else 'ADMIN NO:'+current_admin} to the Library.")
    




print("~~~ Welcome to Library Management System ~~~")            
print('1.Admin Authentication')
print('2.User Authentication')
module_choice=int(input('Enter:'))
if(module_choice==1): 
    time.sleep(1)
    os.system('cls')
    admin_auth()
elif(module_choice==2):
    time.sleep(1)
    os.system('cls')
    user_auth()