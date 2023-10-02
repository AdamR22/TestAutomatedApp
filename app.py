from flask import Flask

app = Flask(__name__)

@app.route("/")
def test_route():
    return "Hello from test app", 200


if __name__ == "__main__":
    app.run()
