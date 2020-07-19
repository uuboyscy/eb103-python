from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route('/hello_post', methods=['GET', 'POST'])
# def hello_post():
#
#     if request.method == 'GET':
#         return render_template('hello_post.html', username='')
#     else:
#         username = request.form.get('username')
#         return render_template('hello_post.html', username=username)

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    req_method = request.method
    username = '' if req_method == 'GET' else request.form.get('username')
    return render_template('hello_post.html', username=username, req_method=req_method)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')