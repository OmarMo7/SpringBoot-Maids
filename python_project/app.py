from flask import Flask, request, jsonify
import sqlite3
import joblib

app = Flask(__name__)
db_path = 'devices.db'

model = joblib.load('model.joblib')


def get_db():
    conn = sqlite3.connect(db_path)
    return conn


@app.route('/devices', methods=['GET'])
def get_all_devices():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM devices')
    devices = cursor.fetchall()
    conn.close()
    return f"This is all devices{devices}"


@app.route('/devices/<int:device_id>', methods=['GET'])
def get_device_by_id(device_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM devices WHERE id = ?', (device_id,))
    device = cursor.fetchone()
    conn.close()
    return jsonify(device)


@app.route('/devices', methods=['POST'])
def add_new_device():
    try:
        data = request.get_json()  # Get input data from the request
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO devices (battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi, price_range) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (data['battery_power'], data['blue'], data['clock_speed'], data['dual_sim'], data['fc'], data['four_g'], data['int_memory'], data['m_dep'], data['mobile_wt'], data['n_cores'], data['pc'], data['px_height'], data['px_width'], data['ram'], data['sc_h'], data['sc_w'], data['talk_time'], data['three_g'], data['touch_screen'], data['wifi'], data['price_range']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Device added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get input data from the request
        prediction = model.predict([list(data.values())])

        # Insert the predicted device into the database
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO devices (battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi, price_range) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (data['battery_power'], data['blue'], data['clock_speed'], data['dual_sim'], data['fc'], data['four_g'], data['int_memory'], data['m_dep'], data['mobile_wt'], data['n_cores'], data['pc'], data['px_height'], data['px_width'], data['ram'], data['sc_h'], data['sc_w'], data['talk_time'], data['three_g'], data['touch_screen'], data['wifi'], int(prediction[0])))
        conn.commit()
        conn.close()

        return f"The price range is {prediction}"
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    # Listen on all available network interfaces
    app.run(host='0.0.0.0', port=5000)