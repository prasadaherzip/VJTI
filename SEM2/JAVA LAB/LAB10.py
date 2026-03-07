import sqlite3
import threading


# Function to insert data into database
def insert_student(name, marks):
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO students VALUES (?, ?)", (name, marks))

        conn.commit()
        conn.close()

        print(f"{name} inserted successfully")

    except Exception as e:
        print("Database Error:", e)


# Thread task
def thread_task(name, marks):
    insert_student(name, marks)


# Create database and table
try:
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS students(name TEXT, marks INTEGER)"
    )

    conn.commit()
    conn.close()

except Exception as e:
    print("Table Creation Error:", e)


# Creating threads
t1 = threading.Thread(target=thread_task, args=("Rahul", 85))
t2 = threading.Thread(target=thread_task, args=("Priya", 90))
t3 = threading.Thread(target=thread_task, args=("Amit", 78))

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for threads to finish
t1.join()
t2.join()
t3.join()

print("All database operations completed.")