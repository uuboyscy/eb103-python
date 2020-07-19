from flask import Flask, request, jsonify
import poker

app = Flask(__name__, static_url_path='/test', static_folder='./static')

@app.route('/poker')
def plyer():
    player_num = int(request.args.get('n'))
    tmpdict = poker.poker(player_num)
    return jsonify(tmpdict)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')