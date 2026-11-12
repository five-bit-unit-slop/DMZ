from flask import Flask

from recieve import receive_sensor
from request import health_check

app = Flask(__name__)

app.add_url_rule("/sensor", view_func=receive_sensor, methods=["POST"])
app.add_url_rule("/health", view_func=health_check, methods=["GET"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)