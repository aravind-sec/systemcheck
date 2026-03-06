from flask import Flask
import platform
import socket
app = Flask(__name__)

@app.route("/")
def system_info():
    return {
        "system": platform.system(),
        "version": platform.version(),
        "processor": platform.processor(),
        "Node name": platform.node(),
        "Hostname": socket.gethostname(),
        "Domain name": socket.getfqdn(),
        "Release": platform.release(),
        "Machine": platform.machine(),
        "IP Address": socket.gethostbyname(socket.gethostname())
    }

app.run()

