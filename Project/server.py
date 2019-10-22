import tkinter as tk
import threading
import socket


global serverSocket
global clientSocket

def recv_message(text, serverSocket):
	message, clientAddress = serverSocket.recvfrom(2048)
	message = str(message.decode())
	text.insert("1.0", message+"\n")
	print(message)
	if(message != "bye"):
		recv_message(text, serverSocket)


def server(text):
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	serverSocket.bind(('localhost', 12000))
	t1 = threading.Thread(target = recv_message, args = [text, serverSocket])
	t1.start()
		


root = tk.Tk()
root.title("Working of Checksum")
root.geometry("400x400")


text = tk.Text(root, bg = "grey", bd = 3)
# action_arg = partial(action, text)
c_server = tk.Button(root, text = "Create Server", command = lambda: server(text))
c_sendMessage = tk.Button(root, text = "Send Message", command = lambda: action(text))


c_server.place(relwidth = 0.2, relheight = 0.1, relx = 0.1, rely = 0.1)
text.place(relwidth = 0.5, relheight = 0.3, relx = 0.25, rely = 0.25)
c_sendMessage.place(relx = 0.375, rely = 0.6)
root.mainloop()