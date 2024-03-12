import socket
import cv2
import pickle
import struct
import tkinter as tk
from tkinter import messagebox

def connect_to_server():
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip_entry.get(), port))
        messagebox.showinfo("Client", f"Connected to server at {server_ip_entry.get()}:{port}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to server: {e}")
        return

    data = b""
    payload_size = struct.calcsize("Q")

    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(4*1024)
            if not packet:
                break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]
        while len(data) < msg_size:
            data += client_socket.recv(4*1024)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        cv2.imshow("Receiving...", frame)
        key = cv2.waitKey(10)
        if key == 13:
            break

    client_socket.close()

port = 10050
client_socket = None

root = tk.Tk()
root.title("Server IP Input")
root.iconbitmap("C:/Users/shrey/Downloads/instance-master/GUI/icon.ico")

# Adjust window size and position
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Add image (replace with actual path)
image = tk.PhotoImage(file="C:/Users/shrey/Downloads/instance-master/GUI/Intro.gif")
label_image = tk.Label(root, image=image)
label_image.pack()

# Prompt message
message = tk.Label(root, text="Enter server IP address:", fg="#FF5800", font=("Comfortaa", 20))
message.pack(pady=10)

# Entry for server IP address
server_ip_entry = tk.Entry(root, font=("Comfortaa", 16), width=25)
server_ip_entry.pack()

# Connect to server button
connect_button = tk.Button(root, text="Connect to Server", command=connect_to_server)
connect_button.pack(pady=10)

root.mainloop()



import cv2
import socket
import struct
import pickle
import errno
import time

# Server configuration
SERVER_IP = "192.168.0.103"
SERVER_PORT = 1234

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set socket timeout to avoid blocking indefinitely
client_socket.settimeout(5)  # Timeout of 5 seconds

# Receive frame from server
while True:
    try:
        print("Waiting for data from the server...")
        # Receive frame data
        data, addr = client_socket.recvfrom(65507)
        print("Received data from the server")

        # Deserialize frame length and frame data
        frame_length, frame_data = struct.unpack("Q", data[:8])[0], data[8:]
        print("Received frame length:", frame_length)

        # Deserialize frame data
        frame = pickle.loads(frame_data)

        # Display frame
        cv2.imshow('Client', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except socket.timeout:
        print("Timeout occurred. No data received from the server.")
        continue

    except socket.error as e:
        if e.errno == errno.WSAEINVAL:
            print("WinError 10022: An invalid argument was supplied. Continuing...")
            continue
        elif e.errno == errno.WSAETIMEDOUT:
            print("Socket timeout error. Continuing...")
            continue
        else:
            print("Socket error:", e)
            break

    except Exception as e:
        print("An error occurred:", e)
        break

# Close the socket
client_socket.close()
cv2.destroyAllWindows()
