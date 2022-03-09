from flask import Flask, jsonify, request
from distutils.log import debug
from flask import Flask


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/frecuencia', methods = ['GET'])
def obtenerFrecuencia():
    velocidadLuz = 300000
    frecuenciaEspectral = float(request.args.get('frecuenciaEspectral'))
    herz = frecuenciaEspectral*1000000
    gigaHerz = (frecuenciaEspectral/1000)
    longitudOnda = (velocidadLuz/herz)
    if(frecuenciaEspectral>1e15):
        return jsonify({"longitudOnda" : longitudOnda, "Tipo de luz" :"Rayos Cósmicos"})
    elif(frecuenciaEspectral>1e12 and frecuenciaEspectral<=1e15):
        return jsonify({"longitudOnda": longitudOnda, "Tipo de luz" :"Rayos Gamma"})
    elif(frecuenciaEspectral>1e9 and frecuenciaEspectral<=1e12):
        return jsonify({"longitudOnda": longitudOnda, "Tipo de luz" :"Rayos X"})
    elif(frecuenciaEspectral>1e8 and frecuenciaEspectral<=1e9):
         return jsonify({"longitudOnda": longitudOnda, "Tipo de luz" :"Rayos Ultravioleta"})
    elif(frecuenciaEspectral>1e7 and frecuenciaEspectral<=1e8):
         return jsonify({"longitudOnda": longitudOnda, "Tipo de luz" :"Luz Visible"})
    elif(frecuenciaEspectral>1e4 and frecuenciaEspectral<=1e7):
         return jsonify({"longitudOnda": longitudOnda, "Tipo de luz" :"Rayos Infrarrojo"})
    elif(frecuenciaEspectral>1e2 and frecuenciaEspectral<=1e4):
         return jsonify({"longitudOnda": longitudOnda, "Tipo de luz" :"Rayos Microondas"})
    elif(frecuenciaEspectral>1e-3 and frecuenciaEspectral<=1e2):
         return jsonify({"longitudOnda": longitudOnda, "Tipo de luz" :"Ondas de radio"})

#@app.route('/frecuencia/herz', methods = ['GET'])
#def obtenerFrecuencia():

if __name__ == '__main__':
    app.run(debug=True, port=4000)
