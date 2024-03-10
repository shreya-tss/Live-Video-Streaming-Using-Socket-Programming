from tkinter import *
import pymysql
from datetime import datetime
import ctypes

# Connect to MySQL server
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='tomriddle@31',  # Enter your MySQL password here
    database='registration'   # Enter the name of your database
)

# Create a cursor object
cursor = conn.cursor()

# Create a table for storing user information
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    dob DATE NOT NULL
)
"""
cursor.execute(create_table_query)

# Function to insert user data into the database
def insert_user(name, username, password, dob):
    insert_query = """
    INSERT INTO users (name, username, password, dob)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (name, username, password, dob))
    conn.commit()


def redirect_to_login():
    # Function to redirect to the login page
    top.destroy()
    import LogIn  # Assuming you have a module named LogIn for the login page

def callback():
    name = n.get().strip()
    username = u.get().strip()
    password = p.get().strip()
    dob = Dob.get().strip()

    # Validate date format
    try:
        dob_date = datetime.strptime(dob, "%d/%m/%Y").strftime('%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please enter in DD/MM/YYYY format.")
        return

    # Insert user data into the database
    try:
        insert_user(name, username, password, dob_date)
        print("User registered successfully.")
    except Exception as e:
        print("Error occurred while registering user:", e)

# Set up GUI
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)
res = str(width) + 'x' + str(height)

top = Tk()
top.configure(background="WHITE")
top.geometry(res)
top.title('Instance')
top.iconbitmap('icon.ico')

message2 = Label(top, text="Create an account", fg="#FF5800", bg="WHITE", font=("Comfortaa", 30))
message2.grid(row=1)

user1 = Label(top, text="Name ", bg="WHITE", fg="#FF5800", font=("Comfortaa", 15))
user1.grid(row=2)
n = Entry(top, relief=GROOVE, bd=2)
n.grid(row=3)

message1 = Label(top, text="Username ", bg="WHITE", fg="#FF5800", font=("Comfortaa", 15))
message1.grid(row=4, pady=5)
u = Entry(top, relief=GROOVE, bd=2)
u.grid(row=5)

message1 = Label(top, text="Password ", bg="WHITE", fg="#FF5800", font=("Comfortaa", 15))
message1.grid(row=6)
p = Entry(top, relief=GROOVE, bd=2, show="*")
p.grid(row=7)

message1 = Label(top, text="Date Of Birth (DD/MM/YYYY)", bg="WHITE", fg="#FF5800", font=("Comfortaa", 15))
message1.grid(row=8)
Dob = Entry(top, relief=GROOVE, bd=2)
Dob.grid(row=9)

B1 = Button(top, text="REGISTER", relief=FLAT, bg="#FF5800", fg="WHITE", highlightcolor="WHITE",
            width=50, height=2, font=("Comfortaa"), command=callback)
B1.grid(row=10, pady=5)

# Button to redirect to login page
B2 = Button(top, text="Already have an account? Login here", relief=FLAT, bg="#FF5800", fg="WHITE",
            highlightcolor="BLACK", width=50, height=2, font=("Comfortaa"), command=redirect_to_login)
B2.grid(row=11, pady=5)

top.mainloop()
