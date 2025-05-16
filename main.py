from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # يسمح بطلبات CORS من أي دومين (مهم إذا استخدمت من WordPress)

@app.route('/')
def index():
    return "✅ AI Backend is running!"

@app.route('/segment', methods=['POST'])
def segment():
    # كود وهمي تجريبي للرد فقط - في المرحلة القادمة نربط نموذج SAM هنا
    return jsonify({
        "status": "success",
        "message": "AI segmentation endpoint ready!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
