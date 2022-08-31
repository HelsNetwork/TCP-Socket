import socket
import sys 



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


address = ("localhost", 80)

sock.connect(address)

try:
    # Send data
    message = 'Hello, World'
    byte_string = message.encode("utf-8")

    print (sys.stderr, "sending'%s'" %message)

    sock.sendall(byte_string)
    data = sock.recv(1024)

    
    # Look for the response
    
finally:
    print(sys.stderr, 'closing socket')
    sock.close()
