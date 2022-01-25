from http import server
import socket
import os

if __name__=="__main__":
    ip="127.0.0.1" 
    port= 1234

    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f"connection established- {address[0]}:{address[1]}")

        string=client.recv(1024)
        string=string.decode("utf-8")
        text=client.recv(1024)
        text=text.decode("utf-8")
        if string=="1":
            f=open("test.txt","a")
            f.close()
        elif string=="2":
            if os.path.exists("test.txt"):
                os.remove("test.txt")
            else:
                print("The file does not exist")
        elif string=="3" or text=="3":
            f=open("test.txt","a")
            f.write(string)
            f.close()
        elif string=="4":
            f=open("test.txt","r")
            if f.mode=="r":
                contents=f.read()
                print(contents)
            f.close()
        else:
            exit()
    
        client.close()
        exit()
