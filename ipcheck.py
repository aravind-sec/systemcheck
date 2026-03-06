import socket
domain = input("Enter a domain name: ")
print(f"IP address of {domain} is: {socket.gethostbyname(domain)}")