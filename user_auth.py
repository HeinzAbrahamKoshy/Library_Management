##
import os
import sys
import time
import datetime
import mysql.connector as mysql
from datetime import date,timedelta
import admin_fn
current_user=0
current_admin=0
# fine column added
#books_borrowed column added
user_details = [
    {'user_id': 1000, 'user_name': 'def_0', 'pass': 'def_0','fine':0,'books_borrowed':0},
    {'user_id': 1001, 'user_name': 'def_1', 'pass': 'def_1','fine':0,'books_borrowed':0},
    {'user_id': 1002, 'user_name': 'def_2', 'pass': 'def_2','fine':0,'books_borrowed':0},
    {'user_id': 1003, 'user_name': 'def_3', 'pass': 'def_3','fine':0,'books_borrowed':0},
    {'user_id': 1004, 'user_name': 'def_4', 'pass': 'def_4','fine':0,'books_borrowed':0}
]

admin_details = [
    {'admin_id': 2000, 'admin_pass': 'admin_0'},
    {'admin_id': 2001, 'admin_pass': 'admin_1'},
    {'admin_id': 2002, 'admin_pass': 'admin_2'},
    {'admin_id': 2003, 'admin_pass': 'admin_3'},
    {'admin_id': 2004, 'admin_pass': 'admin_4'}
]
#available_books column added
#status ,borrow date,return date column removed
#total book couln added
book_details = [
    {'book_id': 3000, 'book_name': 'book_0','available_books':2,'total_books':3},
    {'book_id': 3001, 'book_name': 'book_1','available_books':1,'total_books':3},
    {'book_id': 3002, 'book_name': 'book_2', 'available_books':3,'total_books':3},
    {'book_id': 3003, 'book_name': 'book_3', 'available_books':1,'total_books':3},
    {'book_id': 3004, 'book_name': 'book_4', 'available_books':2,'total_books':3}
]
#status column added
#R-Returned
#B-Borrowed
borrow_details=[
    {'book_id':3000,'user_id':1000,'borrow_date':date(20,12,12),'due_date':date(20,12,22),'return_date':date(20,12,22),'fine':0,'status':'R'},
    {'book_id':3001,'user_id':1001,'borrow_date':date(20,12,12),'due_date':date(20,12,22),'return_date':date(20,12,22),'fine':0,'status':'R'},
    {'book_id':3001,'user_id':1001,'borrow_date':date(20,12,12),'due_date':date(20,12,22),'return_date':date(20,12,22),'fine':0,'status':'R'},
    {'book_id':3003,'user_id':1003,'borrow_date':date(20,12,12),'due_date':date(20,12,22),'return_date':date(20,12,22),'fine':0,'status':'R'},
    {'book_id':3003,'user_id':1003,'borrow_date':date(20,12,12),'due_date':date(20,12,22),'return_date':date(20,12,22),'fine':0,'status':'R'},
    {'book_id':3004,'user_id':1004,'borrow_date':date(20,12,12),'due_date':date(20,12,22),'return_date':date(20,12,22),'fine':0,'status':'R'}
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
            print('')
            success=False
            max_id=0
            while(success==False):
                new_username=input('Enter new username:')
                new_pass=input('Enter new pass:')
                for i in user_details:
                    if(i['user_name']==new_username):
                        input("User exists(Press ENTER to try again.)")
                        max_id=i['user_id']
                        success=True
            user_details.append({'user_id': max_id, 'user_name': new_username, 'pass': new_pass,'fine':0,'books_borrowed':0})        
            input('Created User(Press ENTER to exit.)')
            os.system('cls')

            user_auth()
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
                    user_book_functions()
                    break
            if(auth==False):
                print('User not found...')
                input('Please Try Again.(Press Enter)')
                os.system('cls')
        else:
            input('Please press correct input(Press ENTER to try again)')        
            os.system('cls')
            user_auth()

def admin_auth():
    global admin
    global current_admin
    global auth
    while(auth is False):
        print("----Admin Authentication:----",end="\n")   
        id=int(input("Enter Adminstrator ID:"))
        pwd=input("Enter Administrator password:")
        for i in admin_details:
                
                if(i['admin_id']==id and i['admin_pass']==pwd):
                    auth=True
                    print(f"Admin no:{id} has been given access to Library")
                    current_admin=id
                    input("Press ENTER")
                    time.sleep(2)
                    os.system('cls')
                    admin_funtion()
                    break
        if(auth==False):
            print('Admin not found...')
            input('Please Try Again.(Press Enter)')
            os.system('cls')


def user_book_functions(ch=None):
    global module_choice
   # global current_admin
    global current_user
    global book_details
    global user_details
    global book_details
    my_details=None
    for i in user_details:
        if(i['user_name']==current_user):
            my_details=i
   # print("Hello {'USER '+current_user if module_choice==2 else 'ADMIN NO:'+current_admin} to the Library.")
    print("---USER LIBRARY---")
    print("1.View All Books")
    print("2.Borrow a book")
    print("3.Return Books") 
    print("4.User Status")
    print("5.Exit")
    ch=int(input("Enter:"))
    if(ch==1):
        heading=book_details[0].keys()
        print(' ** '.join(heading).upper())
        for i in book_details:
            print('\t'.join(str(i[key]) for key in heading))
        input("Press Enter to go Back.")
        time.sleep(1)
        os.system('cls')
        user_book_functions()
    elif(ch==2):        
        heading=book_details[0].keys()
        print(' ** '.join(heading).upper())
        for i in book_details:
            if(i['available_books']>0):
                print('\t'.join(str(i[key]) for key in heading))
        found=False
        books_taken_now=0
        while(found==False):
            borrow_ch=input('Do you wish to borrow books(y/n):').lower()     ## MAXIMUM THREE BOOKS
            if(borrow_ch=='y'):
                max_books=3
                count_borrow=3-my_details['books_borrowed']
                print(f"You can borrow {count_borrow} more books.")

                while(my_details['books_borrowed']<=max_books):
                    exit_selection=input('Enter Book id(press X to Exit):').lower() ### BOOK ID ENTERED HERE
                    if(exit_selection=='x'):
                        found=True
                        break
                    borrow_book_id=int(exit_selection)
                    for i in book_details:
                        if(borrow_book_id==i['book_id'] and i['available_books']>0):
                            books_taken_now+=1
                            found=True
                            print("Book Borrowed.")
                            # update user_details table
                            my_details['books_borrowed']+=1
                            
                            # update borrow book table
                            borrow_details.append({'book_id':borrow_book_id,'user_id':current_user,'borrow_date':date.today(),'due_date':date.today()+timedelta(days=10),'return_date':None,'fine':0,'status':'B'})
                            for j in book_details:
                                if(j['book_id']==borrow_book_id):
                                    j['available_books']-=1
                    if(found==False):
                        input("Book not Found . Please Try again.(Press ENTER)")
                if(my_details['books_borrowed']==max_books):
                    print(f"You have borrowed maximum number of books:{max_books}")
                    print('Return books to borrow.')
                    found=True
                        
                        
            else:
                found=True 
                input('Press ENTER to return.') 
                os.system('cls')
                user_book_functions()
        print('')
        print("----Current User Status:----")
        print(f"Total number of books taken:{my_details['books_borrowed']}")
        print("")

        user_status_headings=borrow_details[0].keys()
        print(' ** '.join(user_status_headings).upper())
        for i in range(my_details['books_borrowed']):
            for j in borrow_details:
                if(j['user_id']==current_user and j['status']=='B'):
                    print(" ** ".join(str(j[key]) for key in j))
        print('')
        input("Press Enter to return.")            
        time.sleep(1)
        os.system('cls')


        user_book_functions()        
    elif(ch==3):
        user_borrow=False
        for i in borrow_details:
            if(i['user_name']==current_user and i['status']=='B'):
                user_borrow=True
        if(user_borrow==False):
                input("No books to return(Press ENTER to return)")   
                os.system('cls')
                user_book_functions()
        print("---- Books with User:----")
        print(f"Number of books taken:{my_details['books_borrowed']}")
        print("")
        user_status_headings=borrow_details[0].keys()
        print(' ** '.join(user_status_headings).upper())


        for i in range(my_details['books_borrowed']):
            for j in borrow_details:
                if(j['user_id']==current_user and j['status']=='B'):
                    print(" ** ".join(str(j[key]) for key in j))
        print('')
        found_=False
        due=None
        while(found_==False):
            return_book_id=int(input("Which Book would you like to return:(Book id)"))
            for j in borrow_details:
                if(j['user_id']==current_user and j['book_id']==return_book_id):
                    found_=True
                    user_borrow=True
                    due=j['due_date']
                    #update user_details table
                    my_details['books_borrowed']-=1
                    #update status in borrow_details table
                    j['status']='R'
                    #update available_books in book_details table
                    for j1 in book_details:
                        if(j1['book_id']==return_book_id):
                            j1['available_books']+=1
            if(user_borrow==False):
                input("No books to return(Press ENTER to return)")   
                os.system('cls')
                user_book_functions()             

            elif(found_==False):
                input("Book is not Found.Please try again.(Press ENTER)")        

        print(f"Book {return_book_id} is returned.")
        # fine: 10 per day 
        late_days=(datetime.date.today()-due).days
        #print(late_days)
        fine =10*late_days if late_days>0 else 0
        print(f"Fine:{fine}")
        if (fine>0):
            print(f"Late by {late_days} days.")
        else:
            print("No fine pending")
        my_details['fine']=fine

        input("Press ENTER to exit")            
        time.sleep(1)
        os.system('cls')
        user_book_functions()

    elif(ch==4):
        print('')
        print("----Current User Status:----")
        print(f"Total number of books taken:{my_details['books_borrowed']}")
        print("")
        user_borrow=False
        for i in borrow_details:
            if(i['user_name']==current_user and i['status']=='B'):
                user_borrow=True
        if(user_borrow==False):
                input("No books in hand.(Press ENTER to return)")   
                os.system('cls')
                user_book_functions()
        user_status_headings=borrow_details[0].keys()
        print(' ** '.join(user_status_headings).upper())

        for i in range(my_details['books_borrowed']):
            for j in borrow_details:
                if(j['user_id']==current_user):
                    print(" ** ".join(str(j[key]) for key in j))
        print('')
        input("Press Enter to return.")                 
    elif(ch==5):
        main()
    else:
        input('Please ENTER correct input(Press ENTER to continue)')    
        os.system('cls')
        user_book_functions()
def admin_funtion():
    global admin_details
    global user_details
    global book_details
    global borrow_details
    global current_admin

    print('---ADMINISTRATOR FUNCTIONS---')
    print('1.Users Table')
    print('2.Books Table')
    print('3.Borrow Table')
    print('4.Exit')
    ch=int(input('Enter:'))
    if (ch==1):
        heading=user_details[0].keys()
        print(' ** '.join(heading).upper())
        for i in user_details:
            print(' ** '.join(str(i[key]) for key in heading))
        print('')
        print('1.Delete User')
        print('2.Return')
        ch1_ch=int(input('Enter:'))
        if(ch1_ch==1):
            
            user_flag=0
            while(user_flag==0):
                del_user_id=int(input('Enter user id to delete:'))
                for i in user_details:
                    if(del_user_id==i['user_id']):
                        user_flag=1
                        user_details.remove(i)
                        input('Removed..(Press ENTER)')
                        time.sleep(1)
                        os.system('cls')
                        admin_funtion()
                if(user_flag==0):
                    input('User not found.please try again(Press ENTER)') 
                     
        else:
            input('Returning..(Press ENTER)')
            time.sleep(1)
            os.system('cls')
            admin_funtion()

        input('Press ENTER to return')
        time.sleep(1)
        os.system('cls')
        admin_funtion()

    elif(ch==2):
        heading=book_details[0].keys()    
        print(' ** '.join(heading).upper())
        for i in book_details:
            print(' ** '.join(str(i[key]) for key in heading))
        print('')
        print('1.Add Book')
        print('2.Delete Book')
        print('3.Return')
        ch2_ch=int(input('Enter:'))
        if(ch2_ch!=1 and ch2_ch!=2):
            input('Returning..(Press ENTER)')
            time.sleep(1)
            os.system('cls')
            admin_funtion()    
            
        else:
            if(ch2_ch==1):
                new_book_id=int(input("Enter new bookid:"))
                new_id_flag=0
                for i in book_details:
                    if(i['book_id']==new_book_id):
                        new_id_flag=1
                        i['total_books']+=1
                        i['available_books']+=1
                        print('book added')
                if(new_id_flag==0):
                    b_name=input('Enter Book name:')
                    book_details.append({'book_id': new_book_id, 'book_name': b_name, 'available_books':1,'total_books':1})        
                    input('Book Added.(Press ENTER)')
                    time.sleep(1)
                    os.system('cls')
                    admin_funtion()
            elif(ch==2):
                book_flag=0
                while(book_flag==0):
                    del_book_id=int(input('Enter book id to delete:'))
                    for i in book_details:
                        if(del_book_id==i['book_id']):
                            book_flag=1
                            book_details.remove(i)
                            input('Removed..(Press ENTER)')
                            time.sleep(1)
                            os.system('cls')
                            admin_funtion()
                    if(book_flag==0):
                        input('Book not found.please try again(Press ENTER)')


        input('Press ENTER to return')
        time.sleep(1)
        os.system('cls')
        admin_funtion()
    elif(ch==3) :
        if(borrow_details==[]):
            input("Nothing to to display.(press ENTER to return)")
            os.system('cls')
            admin_funtion()
        heading=borrow_details[0].keys()
        print(' ** '.join(heading).upper())
        for i in borrow_details:
            print(' ** '.join(str(i[key]) for key in i))
        print('Returned Book id:')
        L=[]
        for i in borrow_details:
            if(i['status']=='R'):
                print(i['book_id'])
                L.append(i['book_id'])
        
        print('1.Delete Returned Books from Borrow table')
        print('2.Return')
        ch3_ch=int(input('ENTER:'))
        print('')
        if(ch3_ch==1):
            for i in borrow_details:
                if(i['book_id'] in L and i['status']=='R' and i['fine']==0):
                    borrow_details.remove(i)
            print("Removed Books.")

        input('Press ENTER to return')
        time.sleep(1)
        os.system('cls')
        admin_funtion()
    else:
        print('Exiting Admin Page..')
        time.sleep(1)
        os.system('cls')
        main()


def main():
    print("~~~ Welcome to Library Management System ~~~")            
    print('1.Admin Authentication')
    print('2.User Authentication')
    print("3.Exit")
    module_choice=int(input('Enter:'))
    if(module_choice==1): 
        time.sleep(1)
        os.system('cls')
        admin_auth()
    elif(module_choice==2):
        time.sleep(1)
        os.system('cls')
        user_auth()
    elif(module_choice==3):
        exit()    
    else:
        input("Please enter correct input(Press Enter)")
        os.system('cls')
        main()

main()        
