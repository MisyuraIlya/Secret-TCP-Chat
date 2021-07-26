from socket import *


client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1",3333))

while True:
    data = input("Client: ")
    client.sendall(data.encode())

    if data == "exit":
        client.close()
        break

    data = client.recv(2048).decode()
    print ("Server: {0}".format(data))