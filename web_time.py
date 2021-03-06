from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    localtime = time.localtime(time.time())
    return 'Hello Continuous Deployment, the time and date is'+str(time.asctime(localtime))


if __name__ == '__main__':
    app.run()
