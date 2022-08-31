import socket
import sys


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ("localhost", 80)
print (sys.stderr, 'starting up on %s port %s' % address)

sock.bind(address)

# listen on port 80
sock.listen(1)

while True:
    print("Waiting for connection")
    connection, client = sock.accept()

    try:
        print("Connected to client IP: {}".format(client))

        while True:
            data = connection.recv(32)
            print("Received data: {}".format(data))

            if not data:
                break
    finally:
        connection.close()
