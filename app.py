import os
from flask import Flask, jsonify   # giữ các import hiện có

app = Flask(__name__)
# Lấy SECRET_KEY từ biến môi trường; KHÔNG hardcode secret
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')

