from flask import Flask, render_template
#importamos la bibloteca flask

#Creamos la aplicacion
#app = Flask(__name__)
app = Flask("Calidos Ceramica")


"""
ESTE EJEMPLO DE RUTAS ES CON PYTHON, SON TEXTOS PLANOS
#definimos la ruta inicial 
@app.route('/')
def principal():
    return 'Bienvenido a mi primer sitio web'

#podemnos definir varias rutas
@app.route('/contacto')
def contacto():
    return "Esta es la pagina de contacto"

"""


#vamos a crear rutas mostrando plantillas usando HTML
@app.route('/')
def principal():
    return render_template('Calidos Ceramica.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/personalizados')
def personalizados():
    return render_template('personalizados.html')

@app.route('/home')
def home():
    return render_template('home.html')



#Para poder ver esta aplicacion en la web
if __name__ == '__main__':
    app.run(debug=True) #para que corra la app
#al poner "debug" (depuracion) estamos dando a entender que seguimos en proceso de desarrollo de la web
#por lo tanto esta instruccion lo que va a hacer es reiniciarse automaticamene cada vez que haya un cambio 
#para que se guarde

#para iniciar es python .\index.py
#para detener el sv hacemos ctrl + c y luego escribir cls
