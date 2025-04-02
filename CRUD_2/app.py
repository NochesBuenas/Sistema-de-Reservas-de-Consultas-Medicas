from flask import Flask, render_template, request, jsonify, redirect, url_for
import database as db
from citas import Citas

app = Flask(__name__)

@app.route('/')
def home():
    connection = db.dbConnection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM citas")
    citas = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', citas=citas)

@app.route('/citas', methods=['POST'])
def addDate():
    name = request.form['name']
    document = request.form['document']
    phone = request.form['phone']
    direction = request.form['direction']
    date = request.form['date']
    doctor = request.form['doctor']

    if name and document and phone and direction and date and doctor:
        connection = db.dbConnection()
        cursor = connection.cursor()
        query = "INSERT INTO citas (name, document, phone, direction, date, doctor) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (name, document, phone, direction, date, doctor))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('home'))
    return jsonify({"message": "Error al guardar"}), 400

@app.route('/delete/<string:citas_name>')
def delete(citas_name):
    connection = db.dbConnection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM citas WHERE name=%s", (citas_name,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('home'))

@app.route('/edit/<string:citas_name>', methods=['POST'])
def edit(citas_name):
    name = request.form['name']
    document = request.form['document']
    phone = request.form['phone']
    direction = request.form['direction']
    date = request.form['date']
    doctor = request.form['doctor']

    if name and document and phone and direction and date and doctor:
        connection = db.dbConnection()
        cursor = connection.cursor()
        query = "UPDATE citas SET name=%s, document=%s, phone=%s, direction=%s, date=%s, doctor=%s WHERE name=%s"
        cursor.execute(query, (name, document, phone, direction, date, doctor, citas_name))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('home'))    
    return jsonify({"message": "Error al actualizar"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
