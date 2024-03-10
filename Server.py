import cv2
import socket
import struct
import pickle

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
