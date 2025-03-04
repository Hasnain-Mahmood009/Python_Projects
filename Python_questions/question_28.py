# Write a Python program to find local IP addresses using Python's stdlib.
import socket
def get_host_name():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip
print(get_host_name())