import platform
import socket
print("System:", platform.system())
print("Node name:", platform.node())
print("Release:", platform.release())
print("Version:", platform.version())
print("Machine:", platform.machine())
print("Processor:", platform.processor())
print("Hostname:", socket.gethostname())
print("IP Address:", socket.gethostbyname(socket.gethostname()))
