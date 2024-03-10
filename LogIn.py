from tkinter import *
import tkinter
import os, sys, time, pickle
import ctypes
import pymysql

def validate_login(username, password):
    # Connect to the MySQL server
    conn = pymysql.connect(
        host='localhost',
        user='root',  # Change this to your MySQL username
        password='tomriddle@31',  # Change this to your MySQL password
        database='registration'  # Change this to your MySQL database name
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Prepare SQL query to validate login credentials
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

    # Fetch a single row (if any) from the result set
    row = cursor.fetchone()

    # Close cursor and connection
    cursor.close()
    conn.close()

    # Return True if the row exists (valid credentials), otherwise False
    return row is not None

def callback1():
    username, password = user1.get().strip(), e.get().strip()

    if validate_login(username, password):
        # Valid credentials, display "Valid user" message
        valid_user_label = Label(top, text="Valid user", fg="green", bg="WHITE", font=("Comfortaa", 15))
        valid_user_label.grid(row=7, pady=5)

        # Proceed to main application
        top.destroy()
        import Choose  # Assuming Choose is your main application module
        Choose.run(username)
    else:
        # Invalid credentials, display error message
        import Error  # Assuming Error is your error message module
        top.destroy()
        import LogIn

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)
res = str(width) + 'x' + str(height)

top = Tk()
img = PhotoImage(file="Intro.GIF")
top.configure(background="WHITE")
top.geometry(res)
top.title('Instance')
top.iconbitmap('icon.ico')

message1 = Label(image=img, borderwidth=0, bg="WHITE")
message1.grid(row=0, ipadx=500)
message2 = Label(top, text="Enter your credentials", fg="#FF5800", bg="WHITE", font=("Comfortaa", 40))
message2.grid(row=1)

user1 = Label(top, text="Username ", bg="WHITE", fg="#FF5800", font=("Comfortaa", 15))
user1.grid(row=2)
user1 = Entry(top, relief=GROOVE, bd=2)
user1.grid(row=3)

message1 = Label(top, text="Password ", bg="WHITE", fg="#FF5800", font=("Comfortaa", 15))
message1.grid(row=4, pady=5)
e = Entry(top, relief=GROOVE, bd=2, show="*")
e.grid(row=5)

B1 = tkinter.Button(top, text="LOG IN", relief=FLAT, bg="#FF5800", fg="WHITE", highlightcolor="WHITE", width=50,
                    height=2, font=("Comfortaa"), command=callback1)
B1.grid(row=6, pady=16)

top.mainloop()

