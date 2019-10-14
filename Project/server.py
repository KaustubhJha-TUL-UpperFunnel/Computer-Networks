# from socket import *
# serverPort = 12005
# serverSocket = socket(AF_INET,SOCK_STREAM)
# serverSocket.bind(('127.0.0.1',serverPort))
# serverSocket.listen(1)
# print 'The server is ready to receive'
# while 1:
# 		connectionSocket, addr = serverSocket.accept()
# 		message = connectionSocket.recv(1024*5)
# 		print message
# 		temp = list(message.split())
# 		try:
# 			name=temp[1][1:]
# 			f = open(name)
# 			contents = f.read()
# 			connectionSocket.send('HTTP/1.1 200 OK\r\n')
# 			connectionSocket.send('Content-Type: text/html\r\n')
# 			connectionSocket.send('\r\n')
# 			connectionSocket.send(contents)
# 			connectionSocket.close()
# 		except:
# 			f = open("test.html")
# 			contents = f.read()
# 			connectionSocket.send('HTTP/1.1 404 Not Found\r\n')
# 			connectionSocket.send('Content-Type: text/html\r\n')
# 			connectionSocket.send('\r\n')
# 			connectionSocket.send(contents)
# 			connectionSocket.close()

import tkinter as tk
from functools import partial
import socket


global serverSocket
global clientSocket


def action(text):
	var = text.get("1.0", "end-1c")
	print(var)
	clientSocket.sendto(var,('localhost', 12000))
	message, clientAddress = serverSocket.recvfrom(2048)
	print(message)


def server(text):
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	serverSocket.bind(('', 12000))
	print("server created")
	flag = True
	while (flag):
		message, clientAddress = serverSocket.recvfrom(2048)
		message = message.decode()
		print(message)
		if(message == "bye"):
			flag = False

def client():
	serverName = 'localhost'
	serverPort = 12000
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

root = tk.Tk()
root.title("Working of Checksum")
root.geometry("400x400")


text = tk.Text(root, bg = "grey", bd = 3)
action_arg = partial(action, text)
c_server = tk.Button(root, text = "Create Server", command = lambda: server(text))
c_client = tk.Button(root, text = "Create Client", command = client)
c_sendMessage = tk.Button(root, text = "Send Message", command = lambda: action(text))


c_server.place(relwidth = 0.2, relheight = 0.1, relx = 0.1, rely = 0.1)
c_client.place(relwidth = 0.2, relheight = 0.1, relx = 0.7, rely = 0.1)
text.place(relwidth = 0.5, relheight = 0.3, relx = 0.25, rely = 0.25)
c_sendMessage.place(relx = 0.375, rely = 0.6)
root.mainloop()