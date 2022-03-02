from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey! this is Betrand and DevOps is the future'


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
