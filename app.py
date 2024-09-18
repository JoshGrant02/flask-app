from datetime import datetime
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def hello_world():
        return send_file('homepage.html')

@app.route("/getTime")
def get_time():
        return f'{datetime.now()}'

if __name__ == "__main__":
        app.run()