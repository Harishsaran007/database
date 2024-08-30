import sqlite3

# Connect to a database or create one
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL

)
''')

# Insert a record
def insert_student(name, age, grade):
    cursor.execute('''
    INSERT INTO students (name, age, grade) 
    VALUES (?, ?, ?)
    ''', (name, age, grade))
    conn.commit()

# Retrieve all records
def get_students():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Update a record
def update_student(id, name, age, grade):
    cursor.execute('''
    UPDATE students
    SET name = ?, age = ?, grade = ?
    WHERE id = ?
    ''', (name, age, grade, id))
    conn.commit()

# Delete a record
def delete_student(id):
    cursor.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()

# Main logic to test functionality
if __name__ == '__main__':
    insert_student('John Doe', 20, 'A')
    insert_student('Jane Smith', 22, 'B')

    print("Students:")
    get_students()

    update_student(1, 'John Doe', 21, 'A+')

    print("After update:")
    get_students()

    delete_student(2)

    print("After deletion:")
    get_students()

# Close the connection to the database
conn.close()
