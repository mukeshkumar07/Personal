import requests
import socket
import ssl
from contextlib import redirect_stdout



#r = requests.get('https://maoqavip.intranet.mckinsey.com')
#print (r)

f = open ("notepad1.txt")
num_line = sum (1 for line in f)
f.close()

with open("notepad1.txt", "r") as ins:
    for line in ins:
        hostname = line.strip()
        #a = socket.gethostbyname(line.strip())
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((hostname, 443))
            cert = s.getpeercert()
        #print (cert.values())
        issued_to = cert['subjectAltName']

        #subject = dict(x[0] for x in cert['subject'])
        #for x in cert:
        #    print (x, cert[x])
        #issued_to = subject['commonName']

        with open('certout.txt', 'a') as op:
             with redirect_stdout(op):
                 print (hostname , "> > > > > " , issued_to)