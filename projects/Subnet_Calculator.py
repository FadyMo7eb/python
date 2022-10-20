import ipaddress

def ipchecker():
    while True:
        ip=input('enter a valid ip address:\n')
        a=ip.split('.')
        try:
            if ( (len(a)==4) and ( 1<=int(a[0])<=223) and (int(a[0])!=127) and (int(a[0])!=169 or int (a[1])!=254) and (0<= int(a[1])<=255) and (0<=int(a[2]) <=255) and (0<=int(a[3])<=255)):
                print('correct ip address')
                break
        except ValueError:
            print('please enter an integer')
        else:
            if (int(a[0])==127):
                answer=input('this is a loopback ip address do you wish to continue')
                if answer=='yes' or answer=='y':
                    continue
                else:
                    break
            print('bad ip')
            continue
    return ip 

net4 = ipaddress.ip_network('192.0.0.0/24')

net6 = ipaddress.ip_network('2001:db8::0/96')

print(net4.num_addresses)                  # Finding out how many individual addresses are in a network
