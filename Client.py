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
