
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key='llave_secreta'

@app.route('/')
def root():

    if('visitas' in session):
        # Si visitas existe en la sesión, incrementarla en uno
        session['visitas'] = session.get('visitas') + 1
    else:
        # Si no existe, crearla con el valor de 1
        session['visitas'] = 1

    if('resets' not in session):
        session['resets'] = 0

    return render_template('index.html', visitas=session.get('visitas'),resets=session.get('resets'))

@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear()
    return redirect("/")


@app.route('/suma2')
def suma2():
    session['visitas'] = session.get('visitas') + 1
    return redirect("/")

@app.route('/reset')
def reset():
    session.pop('visitas',0)
    session['resets'] = session.get('resets') + 1
    return redirect("/")

@app.route('/suma', methods=['POST'])
def suma():
    cantidad=int(request.form["cantidad"])
    print(cantidad)
    session['visitas'] = session.get('visitas') + cantidad -1
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
