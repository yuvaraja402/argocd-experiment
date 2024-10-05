from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def dublin_time():
    # Set the timezone to Dublin
    dublin_tz = pytz.timezone('Europe/Dublin')
    dublin_time = datetime.now(dublin_tz)

    # Format the datetime as a 12-hour format with AM/PM
    formatted_time = dublin_time.strftime('%Y-%m-%d %I:%M:%S %p')

    # Return the JSON response
    return jsonify({"Dublin_datetime": formatted_time})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
