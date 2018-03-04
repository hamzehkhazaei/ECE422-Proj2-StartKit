
"""
A simple web application; return the number of time it has been visited and also the amount of time that took to
run the difficult function.
"""

from flask import Flask
from redis import Redis
import random
import time

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


def difficult_function():
    output = 1
    t0 = time.time()
    difficulty = random.randint(1000000, 2000000)
    for i in range(difficulty):
        output = output * difficulty
        output = output / (difficulty - 1)
    t1 = time.time()
    compute_time = t1 - t0
    return compute_time


@app.route('/')
def hello():
    count = redis.incr('hits')
    computation_time = difficult_function()
    return 'Hello There! I have been seen {} times. I have solved the problem in {} seconds.\n'.format(count,
                                                                                                       computation_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
