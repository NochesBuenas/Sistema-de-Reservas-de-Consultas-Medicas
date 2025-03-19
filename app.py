from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase 
from citas import Citas
from pymongo import MongoClient



app = Flask(__name__)

# client = MongoClient('mongodb://localhost:27017/')
# db = client['Asignacio_Citas']
db = dbase.dbConnecction()


MONGO_URI = "mongodb+srv://kevindavidtabares123:Callese123@cluster1.ky2wm.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

@app.route('/guardar', methods=['POST'])
def guardar():
    # Código para guardar los datos en MongoDB
    return jsonify({"message": "Datos guardados correctamente"})

#Ruta de la aplicación
@app.route('/') #La ruta principal de la aplicación
def home():
    citas = db['citas']
    citasReceived = citas.find() #Apareceran todas las colecciones de la base de datos previamente cargadas
    return render_template('index.html', citas = citasReceived) ##


#Method POST
@app.route('/citas', methods=['POST']) #Que es POST
def addDate():
    citas = db['citas']
    print("Conectando a la colección:", citas)  # 👀 Verificar la conexión

    name = request.form['name']
    document = request.form['document']
    phone = request.form['phone']
    direction = request.form['direction']
    date = request.form['date']
    doctor = request.form['doctor']

    if name and document and phone and direction and date and doctor:
        cita = Citas(name, document, phone, direction, date, doctor)
        citas.insert_one(cita.toDBColletion())
        response = jsonify({
            'name' : name,
            'document' : document,
            'phone' : phone,
            'direction' : direction,
            'date' : date,
            'doctor' : doctor
        }) 
        return redirect(url_for('home'))
    else:
        return notFound()

#Method Delete
@app.route('/delete/<string:citas_name>')#
def delete(citas_name):
    citas = db['citas']
    citas.delete_one({'name': citas_name})
    return redirect(url_for('home'))

#Method Modify/put
@app.route('/edit/<string:citas_name>', methods=['POST']) #
def edit(citas_name):
    citas = db['citas']
    name = request.form['name']
    document = request.form['document']
    phone = request.form['phone']
    direction = request.form['direction']
    date = request.form['date']
    doctor = request.form['doctor']

    if citas is not None and name and document and phone and direction and date and doctor:
        citas.update_one({'name': citas_name}, {'$set': {'name': name, 'document': document, 'phone': phone, 'direction': direction, 'date': date, 'doctor': doctor}})
        response = jsonify({'message': 'Cita ' + citas_name + ' ha sido actualizada'})
        return redirect(url_for('home'))
    else:
        return notFound()



@app.errorhandler(404)
def notFound(error = None):
    message = {
        'message': 'No encontrado' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response #Cuál es el proceso para devolver la respuesta

if __name__ == '__main__':
    app.run(debug=True, port=4000)

    #Hasta aquí es para crear la página
