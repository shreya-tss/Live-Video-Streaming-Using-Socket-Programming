
import socket
import cv2
import pickle
import struct

# Server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name) #retrieves host IP address and binds socket to it.
print('HOST IP:', host_ip)
port = 10050
socket_address = (host_ip, port)
print('Socket created')
server_socket.bind(socket_address)
print('Socket bind complete')
server_socket.listen(5) #starts listening for incoming connections, with a maximum backlog of five connections.
print('Socket now listening')

while True:
    client_socket, addr = server_socket.accept()
    print('Connection from:', addr) #Accepts incoming client connections using accept(). Blocks until a connection is established.
    
    
    if client_socket:
        vid = cv2.VideoCapture(0)  #Opens a video capture device (cv2.VideoCapture) to capture frames from the webcam (device index 0)
        while vid.isOpened(): #loop to capture frames until video is opened.
            ret, frame = vid.read()
            if not ret:
                print("Error: Failed to capture frame")
                break

            # Serialize frame
            frame_data = pickle.dumps(frame) #Serializes the frame using pickle.dumps()
            message = struct.pack("Q", len(frame_data)) + frame_data #packs it with its size using struct.pack().

            try:
                #Sends the serialized frame over the network to the client using
                client_socket.sendall(message)
            except socket.error as e:
                print("Error sending frame:", e)
                break
            
            #Displays the frame locally using cv2.imshow() with the window title
            cv2.imshow('Sending...', frame)
            key = cv2.waitKey(10)
            if key == 13:
                client_socket.close()
                break

        vid.release()

cv2.destroyAllWindows()