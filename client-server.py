import socket
import sys 



# Get the hostname
hostname = socket.gethostname() 

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


address = ("localhost", 80)

sock.connect(address)

# Take input
message = input('-> ') 

while message.lower().strip() != 'exit':

        sock.sendall(message.encode())
        data = sock.recv(1024).decode()

        print(f'From {hostname}: ' + data)
        
        message = input(" -> ")
        

        print(sys.stderr, 'closing socket')

sock.close()
