# Live Video Streaming using Socket Programming 
Its a TCP based client server video sharing interface
The client connects to the server and a non audio based live video is aired of the server
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
  
  
