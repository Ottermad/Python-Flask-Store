from flask import (
	Flask)
import requests

app = Flask(__name__)

if __name__ == "__main__":
	app.run(debug=True)