from wakeonlan import send_magic_packet
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/wake_up', methods=['POST'])
def send_packet():
    try:
        json_data = request.json
        send_magic_packet(json_data['mac'])
        return jsonify({'status': 200})
    except (KeyError, TypeError) as err:
        return jsonify({'status': 400, 'message': str(err)})


@app.route('/try_connect', methods=['POST', 'GET'])
def try_connect():
    return jsonify({'status': 200})


if __name__ == '__main__':
    app.run()
