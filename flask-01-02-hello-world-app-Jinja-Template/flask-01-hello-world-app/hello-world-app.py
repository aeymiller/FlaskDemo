from flask import Flask

app = Flask(__name__)

@app.route("/")
def default():
  return "Welcome to my website"

@app.route("/home")
def home():
    return "Welcome home!"

@app.route("/profile/<user>")
def profile(user):
    return "Welcome {} to your profile".format(user)

if __name__ == "__main__":
    app.run(port=3000)