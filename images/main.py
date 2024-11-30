from flask import Flask,render_template, request


import requests

app = Flask(__name__)

def get_weather_data(city:str):
    """
    Funcion que espera el nombre de la ciudad por parametro, para luego realizar un get a openweather
    para consultar el clima de la ciudad ingresada
    """
    API_KEY = '36a0a33a2625429cd189d51f7ed9c489'
    idioma = 'es'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}'
    r = requests.get(url).json()
    return r

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index1.html', ciudad='', humedad='',presion='', descripcion='', icon = '',cod = '')

    ciudad= request.form.get('txtCiudad')
    if ciudad:
        data=get_weather_data(ciudad) #lo que trae el api
        cod=data.get('cod')
        if cod != 200:
            return render_template('index1.html', ciudad='', humedad='',presion='', descripcion='', icon = '' , cod = cod)
        
        humedad=data.get('main').get('humidity')
        presion=data.get('main').get('pressure')
        descripcion=data.get('weather')[0].get('description')
        icon=data.get('weather')[0].get('icon')
        return render_template('index1.html', ciudad=ciudad, humedad=humedad,presion=presion, descripcion=descripcion, icon = icon , cod = cod)
    else:
        return render_template('index1.html', ciudad='', humedad='',presion='', descripcion='', icon = '',cod = '')

#  ruta para la hoja de vida
@app.route('/jose_chancay_curriculum.html')
def jose_chancay_curriculum():
    return render_template('jose_chancay_curriculum.html')


@app.route('/paginaarriba.html')
def paginaarriba():
    return render_template('paginaarriba.html')

@app.route('/paginaderecha.html')
def paginaderecha():
    return render_template('paginaderecha.html')

@app.route('/paginaizquierda.html')
def paginaizquierda():
    return render_template('paginaizquierda.html')


if __name__ == "__main__":
    app.run(debug=True)
    
    
    




