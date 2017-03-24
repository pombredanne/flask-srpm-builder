from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def default():
    return "Hello World!"

@app.route("/payload", methods=["POST"])
def p():
    print request.json
    return "", 200

if __name__ == "__main__":
    app.run()
