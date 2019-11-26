from flask import Flask, render_template
import datetime
import requests

# Wir legen das App Objekt an, mit dem wir die Webanwendung konfigurieren können
app = Flask(__name__)

counter = 0

# Wir definieren eine Route via Dekorator, das mit dem @
@app.route("/")

def index():
    global counter
    counter += 1
    return render_template("index.html", htmlzaehler=counter)

@app.route("/about")
def about():
    datum = datetime.datetime.now()
    user = requests.get('https://jsonplaceholder.typicode.com/users/1').json()["name"]
    return render_template("about.html", datumsanzeige=datum, useranzeige=user)

@app.route("/portfolio")
def portfolio():
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()["title"]
    return render_template("portfolio.html", anzeigetodos=todo)

@app.route("/portfolio/boogle")
def boogle():
    return render_template("boogle.html")

@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/portfolio/shop")
def shop():
    return render_template("shop/index.html")

@app.route("/portfolio/hans")
def hans():
    return render_template("hans/index.html")

@app.route("/portfolio/simpleshop")
def simpleshop():
    return render_template("simpleshop.html")

# Wenn dieses Modul das Hauptmodul ist, dann starten wir Flask
if __name__ == '__main__':
    app.run()
