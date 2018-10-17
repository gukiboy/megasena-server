#!venv/bin/python
from flask import Flask
import random
import sched
import time
import threading

app = Flask(__name__)

pickedNumber = None
scheduler = sched.scheduler(time.time, time.sleep)

def pickNewNumber():
    global pickedNumber
    pickedNumber = random.randint(0,10)
    print(str(pickedNumber) + ' was picked!')

@app.route('/')
def index():
    return str(pickedNumber)

scheduler.enter(10,1,pickNewNumber, ())
scheduler.enter(50,1,pickNewNumber, ())

t = threading.Thread(target=scheduler.run)
t.start()


if __name__ == '__main__':
    app.run(host='10.0.0.105', debug=True)
