from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html", name="Andreas", lastname="Eymiller")

@app.route("/body/<int:x>/<int:y>")
def body(x,y):
    return render_template("body.html", x=x , y=y, sum= x+y)

if __name__ == "__main__":
    app.run(port=3000)