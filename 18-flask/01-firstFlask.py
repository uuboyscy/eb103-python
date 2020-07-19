from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask 123!'

@app.route('/allen')
def hello_allen():
    return 'Hello Allen'

@app.route('/Ted')
def hello_ted():
    return 'Hello Ted'

@app.route('/hello/<username>')
def hello(username):
    return 'Hello %s'%(username)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')