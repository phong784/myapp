from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Ứng dụng chạy tốt — Nếu bạn thấy dòng này, bước 1 hoàn tất!"
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

