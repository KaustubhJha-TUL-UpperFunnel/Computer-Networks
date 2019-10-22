import tkinter as tk
# from functools import partial
import socket


serverSocket = 0
clientSocket = 0


def send_message(text):
	global clientSocket
	var = text.get("1.0", "end-1c")
	print(type(var))
	var = var.encode()
	clientSocket.sendto(var,('localhost', 12000))
	print(var)


def client():
	global clientSocket
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print("client created")

root = tk.Tk()
root.title("Working of Checksum")
root.geometry("400x400")


text = tk.Text(root, bg = "grey", bd = 3)
text.place(relwidth = 0.5, relheight = 0.3, relx = 0.25, rely = 0.25)

c_client = tk.Button(root, text = "Create Client", command = client)
c_client.place(relwidth = 0.2, relheight = 0.1, relx = 0.7, rely = 0.1)

c_sendMessage = tk.Button(root, text = "Send Message", command = lambda: send_message(text))
c_sendMessage.place(relx = 0.375, rely = 0.6)


root.mainloop()