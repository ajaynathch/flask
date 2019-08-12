from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World 123</h1>"

@app.route("/login")
def login():
    return "<h1>Login Page</h1>"

@app.route("/logout")
def login():
    return "<h1>Logout1 Page</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0' ,port=80)
