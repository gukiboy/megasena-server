#!venv/bin/python
from flask import Flask
from flask import request
import random
from apscheduler.schedulers.background import BackgroundScheduler
import time
import threading
import uuid
import jsonpickle
from datetime import datetime

app = Flask(__name__)

scheduler = BackgroundScheduler()
pickedNumber = None
scheduler.start()

def pickNewNumber(lottery_name):
    global pickedNumber
    pickedNumber = random.randint(0,500)
    print('['+lottery_name+'] aconteceu!')
    print('['+str(pickedNumber) + '] sorteado!')
    print('Parabens aos vencedores')

@app.route('/')
def index():
    return str(pickedNumber)

# Schedule lottery to happen at an specific date.
# The lottery should be identifiable, so users may
# register on it to try and win the prize.
@app.route('/schedule-lottery', methods=['POST'])
def schedule_lottery():
    my_json = request.get_json()
    print('Sorteio ['+my_json['name']+'] acontecera:')
    lottery_datetime = datetime.fromtimestamp(my_json['time'])
    print(lottery_datetime.strftime('%Y-%m-%d %H:%M:%S'))
    scheduler.add_job(pickNewNumber,
                      'date',
                      run_date=lottery_datetime,
                      args=[my_json['name']])
    return 'Json postado'

if __name__ == '__main__':
    app.run(host='10.0.0.105', debug=True)
