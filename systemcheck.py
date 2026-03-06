from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def info():
    return {
        "visitor_ip": request.remote_addr,
        "browser": request.headers.get("User-Agent")
    }

app.run()