from flask import Flask, jsonify, Response
from flask_cors import CORS, cross_origin
from lifxlan import LifxLAN
import sys
app = Flask(__name__)
CORS(app)

@app.route("/")
def status():
    num_lights = None
    if len(sys.argv) == 2:
        num_lights = int(sys.argv[1])

    # instantiate LifxLAN client, num_lights may be None (unknown).
    # In fact, you don't need to provide LifxLAN with the number of bulbs at all.
    # lifx = LifxLAN() works just as well. Knowing the number of bulbs in advance 
    # simply makes initial bulb discovery faster.
    lifx = LifxLAN(num_lights)

    devices = lifx.get_lights()
    power_states = {}

    for d in devices:
        power_states[ d.get_label() ] = d.get_power() > 0

    return jsonify(power_states)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
