from flask import Flask, render_template, jsonify

app = Flask(__name__)


driver_details = {
    "name": "John Doe",
    "track_route": "Sample track route data"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/driver-details')
def get_driver_details():
    return jsonify(driver_details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
