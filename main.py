# Importing the MySQL connector package
import mysql.connector

# Step 2: Connecting Python to MySQL using the MySQL Connector
# Establishing the connection to MySQL
myDb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="-----",
  db = "pythonSQL"
)
print(myDb)

# Creating a cursor object using the cursor() method
cursor = myDb.cursor()

# Step 4: Program to show all databases on the MySQL server
# Executing the command to show databases
cursor.execute("SHOW DATABASES")

# Fetching all databases and printing them
for db in cursor:
  print(db)

# Step 7: Drop the menagerie database if it exists
cursor.execute("DROP DATABASE IF EXISTS menagerie")

# Step 10: Create the menagerie database
cursor.execute("CREATE DATABASE menagerie")
cursor.execute("USE menagerie")

# Step 11: Show the structure of the pet table
cursor.execute("DESC pet")
# Fetching the description of the table and printing it
structure = cursor.fetchall()
for row in structure:
  print(row)

# Step 14: Display the records in the pet table
cursor.execute("SELECT * FROM pet")
# Fetching all records from the pet table and printing them
records = cursor.fetchall()
for record in records:
  print(record)

# Step 17: Return records of female dogs from the pet table
cursor.execute("SELECT * FROM pet WHERE sex = 'f' AND species = 'dog'")
# Fetching the records of female dogs and printing them
femaleDogs = cursor.fetchall()
for dog in femaleDogs:
  print(dog)

# Step 20: Return the name and birth columns from the pet table
cursor.execute("SELECT name, birth FROM pet")
# Fetching the name and birth columns and printing them
nameBirth = cursor.fetchall()
for item in nameBirth:
  print(item)

# Step 23: Return how many pets each owner has
cursor.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner")
# Fetching the counts of pets per owner and printing them
petCounts = cursor.fetchall()
for count in petCounts:
  print(count)
