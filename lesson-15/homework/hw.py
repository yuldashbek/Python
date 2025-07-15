import pyodbc
import sqlalchemy
import sqlite3

conn = sqlite3.connect("my_database.db")  # This creates 'my_database.db'
cursor = conn.cursor()

# Step 2: Create the Roster table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
''')

# Step 3: Save changes and close connection
conn.commit()
conn.close()

print("Database and 'Roster' table created successfully.")

# Connect to the existing database
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Insert the given rows into the Roster table
data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted into 'Roster' table successfully.")

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Update Jadzia Dax to Ezri Dax
cursor.execute("""
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'
""")

# Commit and close
conn.commit()
conn.close()

print("Name updated from 'Jadzia Dax' to 'Ezri Dax' successfully.")

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Select Name and Age where Species is 'Bajoran'
cursor.execute("""
    SELECT Name, Age
    FROM Roster
    WHERE Species = 'Bajoran'
""")

# Fetch and display results
results = cursor.fetchall()
for name, age in results:
    print(f"Name: {name}, Age: {age}")

conn.close()
