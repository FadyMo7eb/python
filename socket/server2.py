import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),13000))
s.listen(14)
while True :
    print("server is start to use\n")
    con,(ip,port)=s.accept()
    try:
        print(f"client is on now on add {ip} and port is {port} \n")
        data=' WELCOME TO SERVER '
        con.sendall(data.encode("utf-8"))
        while True :
            data=con.recv(2048)
            print(data.decode("utf-8"))
            if data :
                msg=input("enter your massage ").encode("utf-8")
                s.sendall(msg.upper())
            else:
                break
    finally:
        con.close()