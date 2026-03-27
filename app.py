from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import openai
import random
import re
import logging
import jwt
import datetime

load_dotenv()

app = Flask(__name__)


@app.route('/status2', methods=['GET'])
def status():
    return jsonify({'status': 'ON'})

if __name__ == '__main__':
    app.run(port=8080)
    app.run(debug=True)
