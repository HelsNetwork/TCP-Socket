import socket
import sys


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ("127.0.0.0", 80)
print (sys.stderr, 'starting up on %s port %s' % address)

sock.bind(address)

# listen on port 80
sock.listen(1)
conn, addr = sock.accept()

with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print("Received data: {}".format(data))
            if not data:
                break
            conn.sendall(data)
