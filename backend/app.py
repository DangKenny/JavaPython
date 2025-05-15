# backend/app.py
# This is a simple Python backend using Flask.
# It provides an API endpoint that returns the current server date and time.

from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import datetime

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS for all routes. This allows your frontend (running on a different port)
# to make requests to this backend. For production, you might want to restrict origins.
CORS(app)

@app.route('/api/time', methods=['GET'])
def get_current_time():
    """
    API endpoint to get the current server time.
    Accessible via a GET request to /api/time.
    """
    now = datetime.datetime.now()
    # Return the current time as a JSON response
    # ISO 8601 format is a standard way to represent dates and times.
    return jsonify({
        'current_time': now.isoformat(),
        'timezone': str(now.astimezone().tzinfo) # Include timezone information
    })

if __name__ == '__main__':
    """
    This block runs when the script is executed directly (e.g., python app.py).
    It starts the Flask development server.
    - host='0.0.0.0' makes the server accessible from any IP address on your network.
    - port=5000 is the port number the server will listen on.
    - debug=True enables debug mode, which is helpful for development.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
