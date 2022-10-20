import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
print("-------------------------------------")
print("[+] wating for response")
print("-------------------------------------")

while True :
    client , add = s.accept()
    client.send(bytes("hello ya client","utf-8"))
    msg=client.recv(1024)
    print(msg.decode("utf-8"))