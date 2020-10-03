from datetime import datetime as dt
from time import time
import socket

def scan_port(target_host,port_range):
    print(f"Scanning {target_host} Please Wait")
    start = time()
    print("**" * 30)
    try:
        ip = socket.gethostbyname(target_host)
        count=0
        for port in range(int(port_range[0]),
        int(port_range[-1])+1):
            s = socket.socket(socket.AF_INET,
            socket.SOCK_STREAM)
            s.settimeout(1.0)
            response = s.connect_ex((ip,port))
            if response == 0:
                count+=1
                try:
                    print(f"\nPort : {port} \nStatus : Open \nService : {socket.getservbyport(port)}\n")
                except OSError:
                    print(f"\nPort : {port} \nStatus : open \nService : Unknown\n")
            else:
                print(f"\nPort : {port}\nStatus :  close\n")
    except NameError:
        print("Sorry to say, but something went wrong")
    print("**" * 30)
    print(f"Total {count} Open Port in range {port_range} Scanned in {round((time() - start),3)} Seconds")

def search_port(target_host):
    port_range=[1,65353]
    print(f"Scanning {target_host} Please Wait")
    start = time()
    print("**" * 30)
    try:
        ip = socket.gethostbyname(target_host)
        count=0
        for port in range(int(port_range[0]),
        int(port_range[-1])+1):
            s = socket.socket(socket.AF_INET,
            socket.SOCK_STREAM)
            s.settimeout(1.0)
            response = s.connect_ex((ip,port))
            if response == 0:
                count+=1
                try:
                    print(f"\nPort : {port}\nStatus : Open\nService : {socket.getservbyport(port)}\n")
                except OSError:
                    print(f"\nPort : {port}\nStatus : open\nService : Unknown\n")

    except NameError:
        print("Sorry to say, but something went wrong")
    print("**" * 30)
    print(f"Total {count} Open Port Scanned in {round((time() - start),3)} Seconds")

print("1: Search a range of Port")
print("2: Scan All Port")
option=int(input("Please Choose: "))
print("\n\n")

if(option==1):
    target_host = input("Please Enter target_host IP/URL: ")
    port_range = input("Please Enter Port range (x-y): ").split("-")
    if(target_host=="" or port_range==""):
        print("Missing required fields")
    else:
        scan_port(target_host,port_range)
elif(option==2):
    target_host = input("Please Enter target_host IP/URL: ")
    if(target_host==""):
        print("Missing required fields")
    else:
        search_port(target_host)
else:
    print("Invalid Option")