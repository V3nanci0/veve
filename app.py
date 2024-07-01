from config import *
from model import *


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/listar_flores")
def listar_flores():
    with db_session:

        flores = Flor.select()
        return render_template("listar_flores.html", flores=flores)


@app.route("/form_adicionar_flor")
def form_adicionar_flor():
    return render_template("form_adicionar_flor.html")


@app.route("/adicionar_flor")
def adicionar_flor():

    flor = request.args.get("flor")
    nomeCientifico = request.args.get("nomeCientifico")
    genero = request.args.get("genero")
    epocaFloraçao = request.args.get("epocaFloraçao")
    nativa = request.args.get("nativa")
    reino = request.args.get("reino")

    with db_session:
        p = Flor(**request.args)
        commit()
        return redirect("listar_flores")

'''
run:
$ flask run
'''
