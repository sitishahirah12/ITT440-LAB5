import socket
import sys
import json

mydata = {"id": 2018272644, "name": "Shahirah", "age": "21"}
sendData = json.dumps(mydata)

s = socket.socket()
print("Socket created")

port = 8080

s.bind(('', port))
print("Socket binded to %s " %(port))

s.listen(5)
print("Socket is listening")

while True:
	c, addr = s.accept()
	print("Connection with" + str(addr))

	c.sendall(bytes(sendData,encoding="utf-8"))
	buffer = c.recv(1024)
	print(buffer)

c.close()
