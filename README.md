Install
-------

    pip install lifxlan
    pip install flask
    pip install flask-cors


Usage
-----

To serve the current power status of the bulb:

    python status.py

To toggle the bulb at given times using `sunwait`:

    crontab -e
    00 03 * * * /home/pi/bin/sunwait/sunwait sun up +20 51.5388020N 0.9076440W; python /home/pi/lifx/broadcast_off.py
    00 15 * * * /home/pi/bin/sunwait/sunwait sun down -20 51.5388020N 0.9076440W; python /home/pi/lifx/broadcast_on.py
