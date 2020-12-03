from flask import Flask, request

app = Flask(__name__)

if __name__ == "__main__":
    app.run()


@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/api/v1/devices/<device_id>", methods={"GET", "POST"})
def get_device_info(device_id):
    if request.method == "GET":
        return "GET %s" % device_id
    return "POST %s" % device_id
