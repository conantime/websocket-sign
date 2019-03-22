from flask import Flask, render_template,request,jsonify
from flask_socketio import SocketIO,emit,send
import base64
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
imgArr = []

@app.route('/')
def hello_world():
    return render_template('qrcode.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

@socketio.on('myevent')
def test(event):
    # emit('connect', {'data':imgArr},namespace='/')
    # send({'data': imgArr}, namespace='/',json=True)
    pass

@socketio.on('sendImg')
def sendImg():
    pass

@app.route('/saveImg', methods=['GET','POST'])
def getImg():
    ImgBase64 = request.get_data()
    img = str(ImgBase64, encoding="utf-8")
    print(type(img))
    print(img)
    imgArr.append(img)
    # print(base64.b64decode(img))
    data = {"data": "ok"}
    socketio.emit('sendImg', {'data': imgArr}, namespace='/')
    return jsonify(data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
