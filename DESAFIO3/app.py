from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    nome = request.form['nome']
    email = request.form['email']
    comentario = request.form['comentario']
 
    return 'Formulário enviado com sucesso!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    
    