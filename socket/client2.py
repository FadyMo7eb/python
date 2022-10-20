import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),13000))
data=s.recv(2048)
if len(data):
    print("cleint is start to on \n ")
    print(data.decode("utf-8"))
    data="iam here"
    while len(data):
        massage=input("enter your data : ").encode("utf-8")
        s.sendall(massage)
        data=s.recv(2048)
        print(data.decode("utf-8"))
        if massage or data =="quit":
            s.close()

