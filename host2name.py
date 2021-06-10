import socket
from contextlib import redirect_stdout

#a = socket.gethostbyname('home.intranet.mckinsey.com')

f = open ("hostname.txt")
num_line = sum (1 for line in f)
f.close()

with open("hostname.txt", "r") as ins:
    for line in ins:
        a = socket.gethostbyname(line.strip())
        with open('host2ip.txt', 'a') as op:
            with redirect_stdout(op):
                print (a)
