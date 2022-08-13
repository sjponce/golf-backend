from flask import Flask, jsonify, request,send_file
from flask_cors import CORS, cross_origin
from decimal import Decimal, ROUND_HALF_UP
import random
import math

app = Flask(__name__)
CORS(app)
@app.route('/hello', methods=["GET"])

def hello():
    name = request.args.get('name')

    if name is None:
        text = 'Hello!'
    else:
        text = 'Hello ' + name + '!'
    return jsonify({"message": text})

@app.route('/generate', methods=["GET"])
@cross_origin()
def generate():
    
    # Prob A
    probPocoVientoAArray = [
        float(request.args.get('probPocoVientoA_1')),
        float(request.args.get('probPocoVientoA_2')),
        float(request.args.get('probPocoVientoA_3')),
        float(request.args.get('probPocoVientoA_4')),
        float(request.args.get('probPocoVientoA_5')),
        float(request.args.get('probPocoVientoA_6')),
        float(request.args.get('probPocoVientoA_7')),
        float(request.args.get('probPocoVientoA_8')),
        float(request.args.get('probPocoVientoA_9')),
    ]

    probMuchoVientoAArray = [
        float(request.args.get('probMuchoVientoA_1')),
        float(request.args.get('probMuchoVientoA_2')),
        float(request.args.get('probMuchoVientoA_3')),
        float(request.args.get('probMuchoVientoA_4')),
        float(request.args.get('probMuchoVientoA_5')),
        float(request.args.get('probMuchoVientoA_6')),
        float(request.args.get('probMuchoVientoA_7')),
        float(request.args.get('probMuchoVientoA_8')),
        float(request.args.get('probMuchoVientoA_9')),
    ]

    # Prob B
    probPocoVientoBArray = [
        float(request.args.get('probPocoVientoB_1')),
        float(request.args.get('probPocoVientoB_2')),
        float(request.args.get('probPocoVientoB_3')),
        float(request.args.get('probPocoVientoB_4')),
        float(request.args.get('probPocoVientoB_5')),
        float(request.args.get('probPocoVientoB_6')),
        float(request.args.get('probPocoVientoB_7')),
        float(request.args.get('probPocoVientoB_8')),
        float(request.args.get('probPocoVientoB_9')),
    ]

    probMuchoVientoBArray = [
        float(request.args.get('probMuchoVientoB_1')),
        float(request.args.get('probMuchoVientoB_2')),
        float(request.args.get('probMuchoVientoB_3')),
        float(request.args.get('probMuchoVientoB_4')),
        float(request.args.get('probMuchoVientoB_5')),
        float(request.args.get('probMuchoVientoB_6')),
        float(request.args.get('probMuchoVientoB_7')),
        float(request.args.get('probMuchoVientoB_8')),
        float(request.args.get('probMuchoVientoB_9')),
    ]

    # Prob C
    probPocoVientoCArray = [
        float(request.args.get('probPocoVientoC_1')),
        float(request.args.get('probPocoVientoC_2')),
        float(request.args.get('probPocoVientoC_3')),
        float(request.args.get('probPocoVientoC_4')),
        float(request.args.get('probPocoVientoC_5')),
        float(request.args.get('probPocoVientoC_6')),
        float(request.args.get('probPocoVientoC_7')),
        float(request.args.get('probPocoVientoC_8')),
        float(request.args.get('probPocoVientoC_9')),
    ]

    probMuchoVientoCArray = [
        float(request.args.get('probMuchoVientoC_1')),
        float(request.args.get('probMuchoVientoC_2')),
        float(request.args.get('probMuchoVientoC_3')),
        float(request.args.get('probMuchoVientoC_4')),
        float(request.args.get('probMuchoVientoC_5')),
        float(request.args.get('probMuchoVientoC_6')),
        float(request.args.get('probMuchoVientoC_7')),
        float(request.args.get('probMuchoVientoC_8')),
        float(request.args.get('probMuchoVientoC_9')),
    ]

    # Prob viento

    probMuchoVientoArray = [
        float(request.args.get('probMuchoVientoH_1')),
        float(request.args.get('probMuchoVientoH_2')),
        float(request.args.get('probMuchoVientoH_3')),
        float(request.args.get('probMuchoVientoH_4')),
        float(request.args.get('probMuchoVientoH_5')),
        float(request.args.get('probMuchoVientoH_6')),
        float(request.args.get('probMuchoVientoH_7')),
        float(request.args.get('probMuchoVientoH_8')),
        float(request.args.get('probMuchoVientoH_9')),
        float(request.args.get('probMuchoVientoH_10')),
        float(request.args.get('probMuchoVientoH_11')),
        float(request.args.get('probMuchoVientoH_12')),
        float(request.args.get('probMuchoVientoH_13')),
        float(request.args.get('probMuchoVientoH_14')),
        float(request.args.get('probMuchoVientoH_15')),
        float(request.args.get('probMuchoVientoH_16')),
        float(request.args.get('probMuchoVientoH_17')),
        float(request.args.get('probMuchoVientoH_18')),
    ]

    # Simulaciones
    cantSet = int(request.args.get('cantSet'))
    cantidadSimulaciones = int(request.args.get('cantidadSimulaciones'))

    # Cantidad de partidos
    partidos = []
    for i in range(0, cantidadSimulaciones):
        partidos.append(None)
        sets = []

        for j in range(0, cantSet):
            sets.append([])
            # Datos
            vientoHoyoSetArray = []
            numeroGolpesAList = []
            numeroGolpesBList = []
            numeroGolpesCList = []
            # Rnds
            rndMuchoVientoHoyoArray = []
            rndNumeroGolpesAList = []
            rndNumeroGolpesBList = []
            rndNumeroGolpesCList = []

            for k in range(0, 18):
                # Calculo de viento por hoyo del set
                rndMuchoVientoHoyo = random.uniform(0, 1)
                rndMuchoVientoHoyoArray.append(rndMuchoVientoHoyo)

                if probMuchoVientoArray[k] > rndMuchoVientoHoyo:
                    vientoHoyoSet = 'Poco viento'
                else:
                    vientoHoyoSet = 'Mucho viento'
                vientoHoyoSetArray.append(vientoHoyoSet)

                # Calculo jugador A
                rndNumeroGolpesA = random.uniform(0, 1)
                rndNumeroGolpesAList.append(rndNumeroGolpesA)

                if vientoHoyoSet == 'Poco viento':
                    probArr = probPocoVientoAArray
                else:
                    probArr = probMuchoVientoAArray

                acumProb = 0
                for l in range(0, 9):
                    acumProb += probArr[l]
                    numeroGolpesA = l
                    if  acumProb > rndNumeroGolpesA:
                        break

                numeroGolpesAList.append(numeroGolpesA)

                # Calculo jugador B
                rndNumeroGolpesB = random.uniform(0, 1)
                rndNumeroGolpesBList.append(rndNumeroGolpesB)

                if vientoHoyoSet == 'Poco viento':
                    probArr = probPocoVientoBArray
                else:
                    probArr = probMuchoVientoBArray

                acumProb = 0
                for l in range(0, 9):
                    acumProb += probArr[l]
                    numeroGolpesB = l
                    if  acumProb > rndNumeroGolpesB:
                        break

                numeroGolpesBList.append(numeroGolpesB)

                # Calculo jugador C
                rndNumeroGolpesC = random.uniform(0, 1)
                rndNumeroGolpesCList.append(rndNumeroGolpesC)

                if vientoHoyoSet == 'Poco viento':
                    probArr = probPocoVientoCArray
                else:
                    probArr = probMuchoVientoCArray

                acumProb = 0
                for l in range(0, 9):
                    acumProb += probArr[l]
                    numeroGolpesC = l
                    if  acumProb > rndNumeroGolpesC:
                        break

                numeroGolpesCList.append(numeroGolpesC)
            # Creacion de set
            fila = {
                "rndNumeroGolpesAList": rndNumeroGolpesAList,
                "numeroGolpesAList": numeroGolpesAList,
                "rndNumeroGolpesBList": rndNumeroGolpesBList,
                "numeroGolpesBList": numeroGolpesBList,
                "rndNumeroGolpesCList": rndNumeroGolpesCList,
                "numeroGolpesCList": numeroGolpesCList,
            }
            sets[j].append(fila)
        partidos[i] = sets
        print(i)
    return jsonify({"partidos": partidos})

if __name__ == '__main__':
    app.run()