import socket

# Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

# Binding to socket
# Host will be replaced/substituted with IP, if changed and not running on host
serversocket.bind((host, port))

# Starting TCP listener
serversocket.listen(3)

while True:
	# Starting the connection
	clientsocket, address = serversocket.accept()

	print("received connection from " % str(address))

	message = 'hello! thank you for connecting to the server' + "\r\n"
	clientsocket.send(message.encode('ascii'))

	clientsocket.close()
