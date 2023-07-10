#Q1. What is a database? Differentiate between SQL and NoSQL databases.

 """ database is structured and orgnized collection of information that can be accessible and update as per our requirment
 sql(Structured Query Language) use structured and relational data models while nosql(Not only Structured Query Language) are flexible and various data models."""

#Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

 """DDL stands for Data Definition Language. 
 It is a subset of SQL (Structured Query Language) used to define and manage the structure of a database.
DDL statements are used to create.modify, and delete database objects such as tables, indexes, views, and constraints. """


"""1. CREATE: The CREATE statement is used to create database objects such as tables, views, indexes, or schemas. For example, to create a table named "Employees" with columns for employee ID, name, and department:

```
CREATE TABLE Employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Department VARCHAR(50)
);
```

2. DROP: The DROP statement is used to delete existing database objects. For example, to delete the "Employees" table:

```
DROP TABLE Employees;
```

3. ALTER: The ALTER statement is used to modify the structure of an existing database object. It can be used to add, modify, or drop columns, constraints, or indexes. For example, to add a new column named "Salary" to the "Employees" table:

```
ALTER TABLE Employees
ADD Salary DECIMAL(10,2);
```

4. TRUNCATE: The TRUNCATE statement is used to remove all data from a table while keeping its structure intact. It is faster than the DELETE statement as it does not generate individual delete logs. For example, to remove all data from the "Employees" table:

```
TRUNCATE TABLE Employees;
"""




#Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.


"""DML stands for Data Manipulation Language. It is a subset of SQL (Structured Query Language) used to retrieve, insert, update, and delete data within a database.
 DML statements are used to interact with the data stored in database objects such as tables. 

The SELECT statement is used to retrieve data from one or more tables in the database.
 It allows you to specify the columns and conditions to filter the data.

 INSERT: The INSERT statement is used to add new data into a table.
 It allows you to specify the values for the columns or retrieve data from another table.

 INSERT INTO Employees (EmployeeID, Name, Department)
VALUES (1, 'John Doe', 'IT');

 The UPDATE statement is used to modify existing data in a table.
It allows you to specify the columns to be updated and the new values based on certain conditions.

UPDATE Employees
SET Department = 'HR'
WHERE EmployeeID = 1;

The DELETE statement is used to remove data from a table based on certain conditions.
It allows you to specify the rows to be deleted.

DELETE FROM Employees
WHERE EmployeeID = 1;
"""


#Q4. What is DQL? Explain SELECT with an example.

"""DQL stands for Data Query Language. It is a subset of SQL (Structured Query Language) 
used specifically for querying and retrieving data from a database.

SELECT FirstName, LastName, Age
FROM Employees
WHERE Department = 'IT' AND Age > 30;
 """


 #Q5. Explain Primary Key and Foreign Key.


 """Primary Key:
A primary key is a column or a set of columns in a database table that uniquely identifies each record within the table. 
It provides a way to ensure data integrity and enforce uniqueness. Here are some key points about primary keys:
Each table can have only one primary key.
The primary key must have a unique value for each record in the table.
The primary key column(s) cannot contain null values.
Primary keys are often used as the basis for relationships between tables.


A foreign key is a column or a set of columns in a database table that establishes a link or relationship between two tables. It refers to the primary key of another table, creating a relationship between the two tables. Some key points about foreign keys are:
A foreign key in one table refers to the primary key in another table.
It helps maintain referential integrity by ensuring that the values in the foreign key column(s) match the values in the primary key column of the referenced table.
Foreign keys allow the establishment of relationships between tables, enabling data consistency and integrity."""





#Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.

import mysql.connector

# Establish a connection to MySQL
cnx = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cursor = cnx.cursor()

# Execute a SQL query
query = "SELECT * FROM your_table"
cursor.execute(query)

# Fetch all the rows from the query result
rows = cursor.fetchall()

# Process the data
for row in rows:
    # Access the data using row[index]
    print(row)

# Close the cursor and connection
cursor.close()
cnx.close()

"""The cursor() method is called on the connection object cnx to create a cursor object.
 The cursor is responsible for executing SQL queries and managing the result set.
The execute() method is used to execute an SQL query passed as a parameter. """


