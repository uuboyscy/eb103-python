from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_get')
def hello_get():
    age = request.args.get('age')
    name = request.args.get('name')
    if name == None:
        return 'Who are you'
    return '<h1>Hello %s, your age is %s.</h1>'%(name, age)

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    outStr = """
    <html>
    <form action="/hello_post" method="POST">
        <label>What is your name?</label>
        <br>
        <input type="textbox" name="username">
        <button type="submit">Submit</button>
    </form>
    <div>
    %s
    </div>
    </html>
    """
    if request.method == 'GET':
        return outStr%('')
    else:
        username = request.form.get('username')
        return outStr%(username)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')