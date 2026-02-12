"""Example of flask main file."""
from flask import Flask
app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    with open("/etc/hostname" ,"r") as f:
        hostname=f.read().strip()
    return f"Response received from pod: {hostname}"


if __name__ == '__main__':
    app.run()
