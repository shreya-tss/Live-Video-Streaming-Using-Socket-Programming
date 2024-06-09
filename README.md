# Live Video Streaming using Socket Programming 
Its a TCP based client server video sharing interface
The client connects to the server and a non audio based live video is aired of the server

Client.py
* Establishes a client-side connection to a server, receiving video frames for display via sockets and OpenCV integration.
* Enhances user interaction by providing a graphical interface for inputting the server's IP address, facilitating smoother usability

Server.py
* Incorporates SSL/TLS encryption using certificate and key files for secure communication, ensuring data privacy and integrity.
* Establishes a server-side socket, binding it to the host's IP address and port for listening to incoming connections, facilitating seamless client-server interaction.
* Enables continuous video streaming by capturing frames from a video source, serializing them, and transmitting them over the network to connected clients, with error handling for smooth operation.

# Certificate generation for SSL
### Generate a certificate signing request(CSR)
  openssl genersa -out key.pem -out csr.pem
  openssl req -key key.pem -out csr.pem
### Generate a self signed certificate
  openssl x509 -signkey key.pem -in csr.pem -req -days 365 -out crt.pem
### Generate Certificate Authority(CA) certificate 
  openssl genrsa -out ca-key.pem 2048
  openssl req -new -x509 -days 365 -key ca-key.pem -out ca.pem
### Adding it to the project 
  add ca.pem to the project for establishing a secure connection 
  
  
