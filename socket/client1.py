import socket 
############################################################# UDP CLIENT ########################################################################
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
m=input("what is your massage ")
s.sendto(m.encode("utf-8"),(socket.gethostname(),12000))
data,client=s.recvfrom(2048)
f=data.decode()
s.close()
n=input(" the session is close click enter ")