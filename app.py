from flask import Flask
from flash_wtf.csrf import CSRFProject

app = Flask(__name__)

csrf = CSRFProject(app)

@app.route("/")
def pagina_inicial():
    return "DAYVISON"

if __name__ == '__main__':
    app.run()