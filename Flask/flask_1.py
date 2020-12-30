from flask import Flask, render_template, request


app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        name = request.form['name'].title()
        pidarasas = ["Лукашенко", "Ермошина", "Караев", "Путин", "Басков", "Чемоданова"]
        if name in pidarasas:
            return render_template("pidory.html", name=name)
        else:
            return render_template("freedom.html", name=name)


@app.route("/info")
def info():
    return "<h1>INFO</h1>"


if __name__ == "__main__":
    app.run(debug=True)
