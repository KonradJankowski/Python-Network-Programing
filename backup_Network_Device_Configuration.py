import getpass
import telnetlib

user = input('Enter your telnet username: ')
password = getpass.getpass()

f = open('myswitches')

for IP in f:
    IP=IP.strip() #remove spaces
    print ('Get running config from Switch ' + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    tn.write(b"terminal length 0\n") #show config in one goal, another way me must put ENTER
    tn.write(b"show run\n")
    tn.write(b'exit\n')

    readoutput = tn.read_all() #telnet session
    saveoutput =  open("switch" + HOST, "w") #save to the file
    saveoutput.write(readoutput.decode('ascii')) # save output from telnet session
    saveoutput.write("\n")
    saveoutput.close # close to the file