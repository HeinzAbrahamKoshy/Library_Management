
##
import os

import time
import datetime
import mysql.connector as mysql
from datetime import date,timedelta

current_user=0
current_admin=0
con=mysql.connect(host='localhost', user='root',password='root',database='library')

print(con)
db='library'

c=con.cursor()


auth=False
def user_auth():
    global auth
    auth=False
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
                c.execute('SELECT user_name FROM user_details where user_name=%s',(new_username,))
                check_if_username_exist=c.fetchone()

                if(check_if_username_exist):
                        input("User exists(Press ENTER to try again.)")
                else:
                    success=True
                    c.execute('INSERT INTO user_details(user_name,pass) VALUES (%s,%s)',(new_username,new_pass))
                    con.commit()
                    input('Created User(Press ENTER to exit.)')
                    os.system('cls')

                    user_auth()
        elif(user_choice==2):    
            usr=input("Enter Username:")

            pwd=input("Enter password:")

            c.execute('SELECT user_name,pass FROM user_details where user_name=%s',(usr,))
            result=c.fetchone()
            if(result):
                u,p=result
                if(p==pwd):
                    print(f"{usr} has been given access to Library")
                    c.execute('SELECT user_id FROM user_details WHERE user_name=%s',(usr,))
                    r=c.fetchone()
                    current_user=r[0]
                    auth=True
                    input("Press ENTER")
                    time.sleep(2)
                    os.system('cls')
                    user_book_functions()
                else:
                    print('INCORRECT PASSWORD...')
                    input('Please Try Again.(Press Enter)')
                    os.system('cls')
                
            else:
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
    auth=False
    while(auth is False):
        print("----Admin Authentication:----",end="\n")   
        id=int(input("Enter Adminstrator ID:"))
        pwd=input("Enter Administrator password:")

        c.execute('SELECT admin_id,admin_pass FROM admin_details WHERE admin_id=%s',(id,))
        result=c.fetchone()
        if(result):
            u,p=result
            if(p==pwd):
                auth=True
                print(f"Admin no:{id} has been given access to Library")
                current_admin=id
                input("Press ENTER")
                time.sleep(2)
                os.system('cls')
                admin_funtion()
                break
            else:
                print('INCORRECT PASSWORD..')
                input("Press ENTER")
                time.sleep(2)
                os.system('cls')
        else:
            print('Admin not found...')
            input('Please Try Again.(Press Enter)')
            os.system('cls')


def user_book_functions():
    global module_choice
   # global current_admin
    global current_user
    global book_details
    global user_details
    global book_details
    my_details=None
    c.execute('SELECT * FROM user_details WHERE user_name=%s',(current_user,))
    my_details=c.fetchone()
    ch=0
   # print("Hello {'USER '+current_user if module_choice==2 else 'ADMIN NO:'+current_admin} to the Library.")
    print("---USER LIBRARY---")
    print("1.View All Books")
    print("2.Borrow a book")
    print("3.Return Books") 
    print("4.User Status")
    print("5.Exit")
    ch=int(input("Enter:"))
    if(ch==1):
        c.execute('SELECT * FROM book_details')
        result=c.fetchall()
        heading=[i[0] for i in c.description]
        print(' ** '.join(heading).upper())
        for i in result:
            print(' ** '.join(str(val) for val in i ))
        input("Press Enter to go Back.")
        time.sleep(1)
        os.system('cls')
        user_book_functions()
    elif(ch==2):        
        c.execute('SELECT * FROM book_details WHERE available_books>0')
       
        result=c.fetchall()
        if(result):
            heading=[i[0] for i in c.description]
            print(' ** '.join(heading).upper())
            for i in result:
                print('  **  '.join(str(val) for val in i))
            found=False
            books_taken_now=0
        else:
            print('NO BOOKS AVAILABLE TO BORROW..') 
            input("Press Enter to go Back.")
            time.sleep(1)
            os.system('cls')
            user_book_functions() 
        while(found==False):
            borrow_ch=input('Do you wish to borrow books(y/n):').lower()     ## MAXIMUM THREE BOOKS
            if(borrow_ch=='y'):
                max_books=3
                c.execute('SELECT books_borrowed FROM user_details WHERE user_id=%s',(current_user,))
                r=c.fetchone()
                r1=r[0]
                count_borrow=max_books-r1

                while(count_borrow>0):
                    print(f"You can borrow {count_borrow} more books.")
                    exit_selection=input('Enter Book id(press X to Exit):').lower() ### BOOK ID ENTERED HERE
                    if(exit_selection=='x'):
                        found=True
                        break
                    borrow_book_id=int(exit_selection)
                    c.execute("SELECT * FROM borrow_details WHERE book_id=%s and status='B' and user_id=%s",(borrow_book_id,current_user))
                    r=c.fetchall()
                    if not r:

                        c.execute('SELECT * FROM book_details WHERE available_books>0 and book_id=%s',(borrow_book_id,))
                        cur_book=c.fetchone()
                        if(cur_book):
                            books_taken_now+=1
                            found=True
                            count_borrow-=1
                            print("Book Borrowed.")
                            today_date=date.today()
                            due_date=date.today()+timedelta(days=10)

                            c.execute("INSERT INTO borrow_details(book_id,user_id,borrow_date,due_date,status) VALUES(%s,%s,%s,%s,'B')",(borrow_book_id,current_user,today_date,due_date))
                            c.execute('UPDATE book_details SET available_books=available_books-1 WHERE book_id=%s',(borrow_book_id,))
                            c.execute('UPDATE user_details SET books_borrowed=books_borrowed+1 WHERE user_id=%s',(current_user,))
                            con.commit()
                        else:
                            input("Book not Found . Please Try again.(Press ENTER)")
                    else:
                        print('Book has already been borrowed.')

                    
                if(count_borrow==0):
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
        c.execute('SELECT books_borrowed FROM user_details WHERE user_id=%s',(current_user,))
        r=c.fetchone()
        book_count=r[0]
        print(f"Total number of books taken:{book_count}")
        print("")
        c.execute("SELECT * FROM borrow_details WHERE user_id=%s and status='B'",(current_user,))
        result=c.fetchall()
        user_status_headings=[i[0] for i in c.description]
        print(' ** '.join(user_status_headings).upper())
        for j in result:
               print(" ** ".join(str(key) for key in j))
        print('')
        input("Press Enter to return.")            
        time.sleep(1)
        os.system('cls')


        user_book_functions()        
    elif(ch==3):
        user_borrow=False
        c.execute('SELECT * FROM borrow_details WHERE user_id=%s and status="B"',(current_user,))
        result=c.fetchall()
        found_=False
        due=None
        return_book_id=None
        if(result):
            user_borrow=True
            print("---- Books with User:----")
            c.execute("SELECT books_borrowed FROM user_details WHERE user_id=%s",(current_user,))
            r=c.fetchone()
            book_count=r[0]
            print(f"Total number of books taken:{book_count}")
            c.execute("SELECT * FROM borrow_details WHERE user_id=%s and status='B'",(current_user,))
            result=c.fetchall()
            user_status_headings=[i[0] for i in c.description]
            print(' ** '.join(user_status_headings).upper())

            for j in result:
                    print(" ** ".join(str(key) for key in j))
            print('')

            
            while(found_==False and book_count<=3):
                return_book_id=int(input("Which Book would you like to return:(Book id)"))
                c.execute("SELECT * FROM borrow_details WHERE user_id=%s AND book_id=%s and status='B'",(current_user,return_book_id))
                result=c.fetchall()
                if(result):
                    found_=True
                    user_borrow=True
                    c.execute("SELECT due_date FROM borrow_details WHERE user_id=%s and book_id=%s and status='B'",(current_user,return_book_id))
                    r=c.fetchone()
                    due=r[0]
                    c.execute('UPDATE user_details SET books_borrowed=books_borrowed-1 WHERE user_id=%s',(current_user,))
                    con.commit()
                    today_date=datetime.date.today()
                    c.execute("UPDATE borrow_details SET status='R',return_date =%s WHERE user_id=%s and book_id=%s",(today_date,current_user,return_book_id))
                    con.commit()
                    c.execute('UPDATE book_details SET available_books=available_books+1 WHERE book_id=%s',(return_book_id,))
                    con.commit()
                else:
                    input("Book is not Found.Please try again.(Press ENTER)")
                
        else:
            input("No books to return(Press ENTER to return)")   
            os.system('cls')
            user_book_functions()
                 

        print(f"Book {return_book_id} is returned.")
        # fine: 10 per day 
        late_days=(datetime.date.today()-due).days
        #print(late_days)
        fine =10*late_days if late_days>0 else 0
        print(f"Fine:{fine}")
        if (fine>0):
            print(f"Late by {late_days} days.")
            c.execute('UPDATE user_details SET fine=fine+%s WHERE user_id=%s',(fine,current_user))
            con.commit()
        else:
            print("No fine pending")
        
        input("Press ENTER to exit")            
        time.sleep(1)
        os.system('cls')
        user_book_functions()

    elif(ch==4):

        print('')
        print("----Current User Status:----")
        c.execute("SELECT books_borrowed FROM user_details WHERE user_id=%s",(current_user,))
        r=c.fetchone()
        
        if(r[0]>0):
            book_count=r[0]
            print(f"Total number of books taken:{book_count}")
            print("")
            
            c.execute("SELECT * FROM borrow_details WHERE user_id=%s and status='B'",(current_user,))
            result=c.fetchall()
            user_status_headings=[i[0] for i in c.description]
            print(' ** '.join(user_status_headings).upper())

            for i in result:
                print(" ** ".join(str(key) for key in i))
            print('')
            input("Press Enter to return.")
            os.system('cls')
            user_book_functions()
        else:
            input("No books in hand.(Press ENTER to return)")   
            os.system('cls')
            user_book_functions()
        
                         
    elif(ch==5):
        os.system('cls')
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
        c.execute("SELECT * FROM user_details")
        result=c.fetchall()
        if(result):
            heading=[i[0] for i in c.description]
            print(' ** '.join(heading).upper())
            for j in result:
                print(" ** ".join(str(key) for key in j))
            print('')
    
            print('1.Delete User')
            print('2.Return')          
            ch1_ch=int(input('Enter:'))
            if(ch1_ch==1):
               
                del_user_id=int(input('Enter user id to delete:'))
                c.execute('SELECT user_id FROM user_details WHERE user_id=%s',(del_user_id,))
                r=c.fetchone()
                if(r):
                    del_user_id=r[0]
                    c.execute('DELETE FROM user_details WHERE user_id=%s',(del_user_id,))
                    #c.execute('DELETE FROM borrow_details WHERE user_id=%s,(del_user_id)')
                    con.commit()
                    input('Removed..(Press ENTER)')
                    time.sleep(1)
                    os.system('cls')
                    admin_funtion()
                else:
                    input('User not found.please try again(Press ENTER)') 
            
            else:
                input('Returning..(Press ENTER)')
                time.sleep(1)
                os.system('cls')
                admin_funtion()

        else:
            print('No users.')
            input('Press Enter to return')
            os.system('cls')
            admin_funtion()

        input('Press ENTER to return')
        time.sleep(1)
        os.system('cls')
        admin_funtion()

    elif(ch==2):
        c.execute("SELECT * FROM book_details")
        result=c.fetchall()
        if(result):
            heading=[i[0] for i in c.description]   
            print(' ** '.join(heading).upper())
            for j in result:
                print(' ** '.join(str(key) for key in j))
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
                    c.execute('SELECT book_id FROM book_details WHERE book_id=%s',(new_book_id,))
                    r=c.fetchone()
                    if(r):
                        new_id_flag=1
                        c.execute('UPDATE book_details SET total_books=total_books+1,available_books=available_books+1 WHERE book_id=%s',(new_book_id,))
                        con.commit()
                        print(f'BOOK Exists.Available books for bookid {new_book_id} has been incremented..')
                        input('(Press ENTER)')
                        os.system('cls')
                        admin_funtion()
                    else:
                        b_name=input('Enter Book name:')
                        c.execute('INSERT INTO book_details(book_name) VALUES (%s)',(b_name,))
                        input('Book Added.(Press ENTER)')
                        con.commit()
                        os.system('cls')
                        admin_funtion()
                    
                elif(ch==2):
                    book_flag=0
                    while(book_flag==0):
                        del_book_id=int(input('Enter book id to delete:'))
                        c.execute('SELECT book_id FROM book_details WHERE book_id=%s',(del_book_id,))
                        r=c.fetchone()
                        if(r):
                            book_flag=1
                            c.execute('DELETE FROM book_details WHERE  book_id=%s',(del_book_id,))
                            con.commit()
                            input('Removed..(Press ENTER)')
                            time.sleep(1)
                            os.system('cls')
                            admin_funtion()
                        else:
                            input('Book not found.please try again(Press ENTER)')
                        
        else:
            print("No Books to show..")
            input("Press ENTER to return")
            os.system('cls')
            admin_funtion()   
        
        input('Press ENTER to return')
        time.sleep(1)
        os.system('cls')
        admin_funtion()
    elif(ch==3) :

        c.execute('SELECT * FROM borrow_details')
        result=c.fetchall()
        if(result):
            heading=[i[0] for i in c.description]
            print(' ** '.join(heading).upper())
            for i in result:
                print(' ** '.join(str(key) for key in i))
            print('Returned Books:')
            c.execute("SELECT book_id FROM borrow_details")
                
        else:
            input("Nothing to to display.(press ENTER to return)")
            os.system('cls')
            admin_funtion()

           
        print('1.Delete Returned Books from Borrow table')
        print('2.Return')
        ch3_ch=int(input('ENTER:'))
        print('')
        c.fetchall()    # uread results error correction
        if(ch3_ch==1):
            c.execute("DELETE FROM borrow_details WHERE status='R' and fine=0")
            con.commit()
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
    global current_user,current_admin
    current_user=0
    current_admin=0
    module_choice=0
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
