from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_get')
def hello_get():
    age = request.args.get('age')
    name = request.args.get('name')
    if name == None:
        return 'Who are you'
    return '<h1>Hello %s, your age is %s.</h1>'%(name, age)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')