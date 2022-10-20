import socket
#################################################################################### UDP server #####################################################################
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((socket.gethostname(),12000))
print(" server is start to use ")
while True :
    data,clientadd=s.recvfrom(2048)
    m=data.decode('utf-8')
    print(m)
    s.sendto((m.upper().encode("utf-8")),clientadd)