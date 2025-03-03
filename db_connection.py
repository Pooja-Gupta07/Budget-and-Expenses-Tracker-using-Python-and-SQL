import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="expense_tracker"
)
# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Check if connection is successful
if conn.is_connected():
    print("Connected to MySQL Database!")

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
    
cursor.close()
conn.close()
print("MySQL Connection Closed.")
