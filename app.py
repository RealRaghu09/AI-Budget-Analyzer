from flask import Flask, render_template, request, jsonify
from Model import MyModel

app = Flask(__name__)
gemini_model = MyModel()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_prompt = request.form['prompt']
    response = gemini_model.generate_response(user_prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3130)