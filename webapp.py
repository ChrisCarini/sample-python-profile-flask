import time
from datetime import datetime

from flask import Flask
from flask_script import Manager
from werkzeug.middleware.profiler import ProfilerMiddleware

# Create and configure the application instance
app = Flask(__name__)

# Let's add some profiling goodness
app.config['PROFILE'] = True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, profile_dir='./perf_test/')


# Sample endpoint w/ some artificial latency added
@app.route('/')
def index():
    """ Just a test endpoint """
    result = '{} - start\n'.format(datetime.now())
    for x in range(1, 11):
        result += '{} - {}^2 = {}\n'.format(datetime.now(), x, get_pow_2(x))
    result += '{} - end\n'.format(datetime.now())
    return result


def get_pow_2(num):
    """ Get the square of a number, artificially slowing it down by 1ms"""
    time.sleep(0.1)
    value1 = pow_wrapper(num, 2) / 2
    value2 = pow_wrapper(num, 2) / 2
    return value1 + value2


def pow_wrapper(num, power):
    """ Artificially slow down pow() """
    time.sleep(0.2)
    return pow(num, power)


manager = Manager(app)

if __name__ == '__main__':
    manager.run()
