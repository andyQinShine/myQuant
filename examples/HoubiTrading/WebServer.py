# encoding: UTF-8
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from examples.HoubiTrading.runOnlineBacktesting import runOnlinBackTesting
import json
import thread
from threading import Lock

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'
app.config['JSON_AS_ASCII'] = False
socketIo = SocketIO(app)
backTest = None

thread_g = None
thread_lock = Lock()


@app.route('/')
def index():
    return render_template('web/index.html')


# @socketIo.on('client_event')
# def client_msg(msg):
#     # log = backTest.getLogger()
#     # emit('server_response', {'data': json.dumps(log, ensure_ascii=False)})
#     emit('sever_response', {'data': msg['data']})


@socketIo.on('connect', namespace='/test')
def connected_msg():
    global thread_g
    with thread_lock:
        if thread_g is None:
            thread_g = socketIo.start_background_task(target=getLogger)

    # logQue = backTest.getLogger()
    # item = logQue.get()
    # json_data = json.dumps(item, ensure_ascii=False)
    # socketIo.emit('logger', {'data': json_data}, namespace='/test')


# 后台线程 产生数据，即刻推送至前端
def getLogger():
    logQue = backTest.getLogger()
    while True:
        socketIo.sleep(3)
        item = logQue.get()
        json_data = json.dumps(item, ensure_ascii=False)
        socketIo.emit('logger', {'data': json_data}, namespace='/test')


if __name__ == '__main__':
    backTest = runOnlinBackTesting()
    backTest.doInit()
    thread.start_new_thread(backTest.start, ("Thread-1", "2", ))
    socketIo.run(app, host='0.0.0.0')


