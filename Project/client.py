import tkinter as tk
from functools import partial
import socket


serverSocket = 0
clientSocket = 0


def action(text):
	var = text.get("1.0", "end-1c")
	# print(var)
	global clientSocket
	var = var.encode()
	clientSocket.sendto(var,('localhost', 12000))
	# message, clientAddress = serverSocket.recvfrom(2048)
	# print(message)


# def server(text):
# 	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 	serverSocket.bind(('', 12000))
# 	# while(True):
# 		# message, clientAddress = serverSocket.recvfrom(2048)
# 	# text.set(message)
# 		# print(message)

def client():
	serverName = 'localhost'
	serverPort = 12000
	global clientSocket
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
