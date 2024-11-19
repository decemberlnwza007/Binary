from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert_to_binary', methods=['POST'])
def convert_to_binary():
    input_text = request.form['text']

    binary_raw = ' ' . join(format(ord(char), '08b') for char in input_text)

    return jsonify({'binary': binary_raw})

@app.route('/convert_to_text', methods=['POST'])
def convert_to_text():
    binary_input = request.form['binary']

    text = ' ' . join(chr(int(b, 2)) for b in binary_input.split(' ')) 

    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)