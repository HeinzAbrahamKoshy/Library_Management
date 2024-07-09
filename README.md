# **Library_Management**
Simple Library Management System in Python


## SQL QUERIES
 **_1. CREATE TABLES_**
 + _USER DETAILS TABLE_
   
`create table user_details(user_id INT PRIMARY KEY AUTO_INCREMENT ,user_name VARCHAR(20),pass VARCHAR(20) UNIQUE,fine INTEGER DEFAULT 0,books_borrowed INTEGER DEFAULT 0);`
+ _BOOK DETAILS TABLE_

`create table book_details(book_id INTEGER PRIMARY KEY,book_name VARCHAR(20),available_books INTEGER DEFAULT 0, total_books INTEGER DEFAULT 0);`  

+ _ADMIN DETAILS TABLE_

`create table admin_details(admin_id INTEGER PRIMARY KEY AUTO_INCREMENT ,admin_pass VARCHAR(20) UNIQUE);`

+ _BORROW DETAILS TABLE_

`create table borrow_details(book_id INTEGER,user_id INTEGER,borrow_date DATE DEFAULT NULL,due_date DATE DEFAULT NULL,return_date DATE DEFAULT NULL,fine INTEGER DEFAULT 0,status VARCHAR(20) DEFAULT NULL);`

**_2. DEFAULT INSERTION VALUES_**

+ _USER DETAILS_

```
INSERT INTO user_details (user_id, user_name, pass, fine, books_borrowed) VALUES 
(1000, 'def_0', 'def_0', 0, 0),
(1001, 'def_1', 'def_1', 0, 0),
(1002, 'def_2', 'def_2', 0, 0),
(1003, 'def_3', 'def_3', 0, 0),
(1004, 'def_4', 'def_4', 0, 0);
```
+ _BOOK DETAILS_

```
INSERT INTO book_details (book_id, book_name, available_books, total_books) VALUES 
(3000, 'book_0', 2, 3),
(3001, 'book_1', 1, 3),
(3002, 'book_2', 3, 3),
(3003, 'book_3', 1, 3),
(3004, 'book_4', 2, 3);
```


+ _ADMIN DETAILS_

```
INSERT INTO admin_details (admin_id, admin_pass) VALUES 
(2000, 'admin_0'),
(2001, 'admin_1'),
(2002, 'admin_2'),
(2003, 'admin_3'),
(2004, 'admin_4');
```

+ _BORROW DETAILS_

```
INSERT INTO borrow_details (book_id, user_id, borrow_date, due_date, return_date, fine, status) VALUES 
(3000, 1000, '2020-12-12', '2020-12-22', '2020-12-22', 0, 'R'),
(3001, 1001, '2020-12-12', '2020-12-22', '2020-12-22', 0, 'R'),
(3001, 1001, '2020-12-12', '2020-12-22', '2020-12-22', 0, 'R'),
(3003, 1003, '2020-12-12', '2020-12-22', '2020-12-22', 0, 'R'),
(3003, 1003, '2020-12-12', '2020-12-22', '2020-12-22', 0, 'R'),
(3004, 1004, '2020-12-12', '2020-12-22', '2020-12-22', 0, 'R');
```


