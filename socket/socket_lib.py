import socket

import binascii                                  # it compressd and decombress the vlaues

from urllib.parse import urlparse                # it swears the ip you write 

s=socket.gethostname()                           # return the machine name or the adapter

r=socket.gethostbyname("google.com")             # return the ip for the wepsite or domain name 

k=socket.gethostbyname_ex('google.com')          # Return a triple (hostname, aliaslist, ipaddrlist) where hostname is the host’s primary host name, aliaslist is a (possibly empty) list of alternative host names for the same address, and ipaddrlist is a list of IPv4 addresses for the same interface on the same host (often but not always a single address). gethostbyname_ex() does not support IPv6 name resolution, and getaddrinfo() should be used instead for IPv4/v6 dual stack support.

ss=socket.getfqdn("google.com")                  # Return a fully qualified domain name for name

kk=socket.gethostbyaddr("google.com")      # Return a triple (hostname, aliaslist, ipaddrlist)   it need the ip or the name 

kk=socket.gethostbyaddr(socket.gethostbyname("google.com"))

parsed_url = urlparse('http://www.gooogle.com') # urlparse("scheme://netloc/path;parameters?query#fragment")

port = socket.getservbyname(parsed_url.scheme) # get the port by name

port = socket.getservbyname('https')

port = socket.getservbyport(80)               # get the name by port 

proto_num = socket.getprotobyname('udp')      # print the protocol number 

ss=socket.getaddrinfo("www.google.com",port=80)   #    return  (family, type, proto, canonname, sockaddr)  Translate the host/port argument into a sequence of 5-tuples that contain all the necessary arguments for creating a socket connected to that service and for ipv4 and ipv6 

kr=socket.inet_aton('192.168.1.2')            # (for only ipv4) Convert an IPv4 address from dotted-quad string format (for example, ‘123.45.67.89’) to 32-bit packed binary format, as a bytes object four characters in length. This is useful when conversing with a program that uses the standard C library and needs objects of type struct in_addr, which is the C type for the 32-bit packed binary this function returns.

packed=binascii.hexlify(kr)                   # Return the hexadecimal representation of the binary data. Every byte of data is converted into the corresponding 2-digit hex representation. The returned bytes object is therefore twice as long as the length of data.

ssk=socket.inet_ntoa(kr)                  # (for only ipv4) Convert a 32-bit packed IPv4 address (a bytes-like object four bytes in length) to its standard dotted-quad string representation (for example, ‘123.45.67.89’). This is useful when conversing with a program that uses the standard C library and needs objects of type struct in_addr, which is the C type for the 32-bit packed binary data this function takes as an argument.

kkr=socket.inet_pton(socket.AF_INET,"192.168.1.2")  # like inet_aton but it for ( ipv6 and ipv4 )

soo=socket.inet_pton(socket.AF_INET6,'2002:ac10:10a:1234:21e:52ff:fe74:40e') # ex: ipv6

kks=binascii.hexlify(kkr)

kkl=binascii.hexlify(soo)

loki=socket.inet_ntop(socket.AF_INET,kkr)        #     (address_family, ip_string) like binascii

loklok=socket.inet_ntop(socket.AF_INET6,soo)     #     (address_family, packed_ip) like binascii

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)               # (family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None) to creat a socket object

sock.bind(("loopback",10000))                    # (HOST, PORT)  to make bind 

sock.listen(12)                                  # Enable a server to accept connections

data="FADY,IS,HERE"

connection, client_address = sock.accept()   # separate into tow variables (connections,ipaddress)                                 # accept the connection and return (socket object, address info) ... NOTE : laddr means local address and raddr means remote address of the socket. Depending on the context of the process or application, one address becomes the remote to the other socket

connection.recv(1234)                         # Receive data from the socket. The return value is a bytes object representing the data received

connection.sendall(data)                    # send all datat Unlike send(), this method continues to send data from bytes until either all data has been sent or an error occurs.

connection.close()                          # close the connection for client 

sock.connect((("loopback",10000)))          # to connect the server ( for client )

sock.close()                                # close connection for the -- client --

sock_creat=socket.create_connection(("loopback",1000)) # Connect to a <<TCP>>  service ((for client)) listening on the internet address (a 2-tuple (host, port)), and return the socket object. This is a higher-level function than socket.connect():

"""

def get_constants(prefix):
    return {
getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)
        }
families = get_constants('AF_')

types = get_constants('SOCK_')

protocols = get_constants('IPPROTO_')


print('Family :', families[sock.family])    this                    creat_connection()
print('Type :', types[sock.type])                 methods      with
print('Protocol:', protocols[sock.proto]) >> num          only

"""
sock.getsockname()                          # to get what in the bind 

sock.recvfrom(1024)                         #  (return bytes) ** udp ** Receive data from the socket. The return value is a pair (bytes, address) where bytes is a bytes object representing the data received and address is the address of the socket sending the data

sock.sendto(data,("loopback",1234))         #   (return bytes) ** udp ** Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by address.

