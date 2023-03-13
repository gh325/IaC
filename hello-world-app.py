from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return 'Hello World (POST)'
    else:
        return 'Hello World (GET)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
