import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        dob DATE
    )
''')

# Insert some data
cursor.execute('''
    INSERT INTO employees (first_name, last_name, dob)
    VALUES ('John', 'Doe', '1980-01-01')
    VALUES ('Jason', 'Wright', '1986-09-12')
''')

# Commit the transaction
conn.commit()

# Query the database
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()

# Print the query results
for row in rows:
    print(row)

# Close the connection
conn.close()
