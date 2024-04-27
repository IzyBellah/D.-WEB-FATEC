from flask import Flask, render_template

# Inicialização do Flask
app = Flask(__name__) 

# Rotas

@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/Quem somos.html")
def Quemsomos():
    return render_template("Quem somos.html")

@app.route("/Contato.html")
def Contato():
    return render_template("Contato.html")



# Execução do aplicativo
if __name__ == "__main__":
    app.run(debug=True)  # Modo de desenvolvedor
 
 