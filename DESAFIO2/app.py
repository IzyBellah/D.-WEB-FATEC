from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static',
static_folder='static') 


@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/Quem somos.html")
def Quemsomos():
    return render_template("Quem somos.html")

@app.route("/Contato.html")
def Contato():
    return render_template("Contato.html")


if __name__ == "__main__":
    app.run(debug=True) 

