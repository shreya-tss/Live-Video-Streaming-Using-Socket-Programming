from tkinter import *
import os

def client():
    os.system(r'python "C:/Users/shrey/Downloads/instance-master (1)/instance-master/GUI/Client.py"')

def server():
    os.system(r'python "C:/Users/shrey/Downloads/instance-master (1)/instance-master/GUI/Server.py"')

def run():
    root = Tk()
    root.title("Select Mode")
    root.configure(background="DARK BLUE")

    # Adjust window size and position
    window_width = 600
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Add image and icon (replace with actual paths)
    root.image = PhotoImage(file="C:/Users/shrey/Downloads/instance-master (1)/instance-master/GUI/Intro.gif")
    root.iconbitmap("C:/Users/shrey/Downloads/instance-master (1)/instance-master/GUI/icon.ico")

    # Display image
    messageimg1 = Label(root, image=root.image)
    messageimg1.pack()

    # Prompt message
    message = Label(root, text="What would you like to do today?", fg="#FF5800", bg="WHITE", font=("Comfortaa", 20))
    message.pack(pady=10)

    # Buttons for client and server modes
    B1 = Button(root, text="CLIENT", relief=FLAT, bg="#FF5800", fg="WHITE", width=50, height=2, font=("Comfortaa"), command=client)
    B1.pack(pady=10)

    B2 = Button(root, text="SERVER", relief=FLAT, bg="#FF5800", fg="WHITE", width=50, height=2, font=("Comfortaa"), command=server)
    B2.pack(pady=10)

    root.mainloop()

run()
