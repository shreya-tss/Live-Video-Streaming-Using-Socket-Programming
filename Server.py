import socket
import cv2
import pickle
import struct
import ssl

certfile = "C:\CSE 4th sem\cn_pro.crt"
keyfile = "C:\CSE 4th sem\cn_pro.key"
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)

# Server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 10050
socket_address = (host_ip, port)
print('Socket created')
server_socket.bind(socket_address)
print('Socket bind complete')
server_socket.listen(5)
print('Socket now listening')

while True:
    client_socket, addr = server_socket.accept()
    print('Connection from:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0)  # Change to the appropriate video source if needed
        while vid.isOpened():
            ret, frame = vid.read()
            if not ret:
                print("Error: Failed to capture frame")
                break

            # Serialize frame
            frame_data = pickle.dumps(frame)
            # Pack frame size and data
            message = struct.pack("Q", len(frame_data)) + frame_data

            # Send frame
            try:
                client_socket.sendall(message)
            except socket.error as e:
                print("Error sending frame:", e)
                break

            cv2.imshow('Sending...', frame)
            key = cv2.waitKey(10)
            if key == 13:
                client_socket.close()
                break

        vid.release()

cv2.destroyAllWindows() 


import cv2
import socket
import struct
import pickle

certfile = "C:\CSE 4th sem\cn_pro.crt"
keyfile = "C:\CSE 4th sem\cn_pro.key"
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)

# Server configuration
SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print("Server started, waiting for client...")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Serialize frame
    data = pickle.dumps(frame)

    # Send frame data over UDP in chunks
    for i in range(0, len(data), 65507):
        chunk = data[i:i+65507]
        print("Sending chunk of size:", len(chunk))
        server_socket.sendto(struct.pack("Q", len(chunk)), (SERVER_IP, SERVER_PORT))
        server_socket.sendto(chunk, (SERVER_IP, SERVER_PORT))
        print("Chunk sent")

    cv2.imshow('Server', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close socket
cap.release()
server_socket.close()
cv2.destroyAllWindows()
