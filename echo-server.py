import socket
import sys

# Get the hostname
hostname = socket.gethostname()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ("localhost", 80)
print (sys.stderr, 'starting up on %s port %s' % address)

sock.bind(address)

# listen on port 80
sock.listen(2)
conn, addr = sock.accept()

while message.lower().strip() != 'exit':

        with conn:
                print(f"Connected by {hostname}")
        while True:
            data = conn.recv(1024)
            print(f"From {hostname}: " + str(data))   
            data = input(' -> ') 

            
            if not data:
                break
            conn.send(data.encode())  
        sock.close()
