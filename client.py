from asyncio.windows_events import NULL
from http import server
import socket

if __name__=="__main__":
    ip="127.0.0.1"
    port= 1234

    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip,port))

    print("\n1.create file")
    print("2.delete file")
    print("3.edit file")
    print("4.read file\n")

    string=input("Enter input:")
    if string=="3":
        text=input("Enter the content:")
        server.send(bytes(text,"utf-8"))
        server.send(bytes(string,"utf-8"))
    else:
        server.send(bytes(string,"utf-8"))

