from flask import Flask
from redis import Redis
import random
import time

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


def func():
    output = 1000
    t0 = time.time()
    difficulty = random.randint(1000000, 2000000)
    for i in range(difficulty):
        output = output * difficulty
        output = output / (difficulty - 1)
    compute_time = time.time() - t0
    return compute_time


@app.route('/')
def hello():
    count = redis.incr('hits')
    computation_time = func()
    return 'Hello There! I have been seen {} times. I have solved the problem in {} seconds.\n'.format(count,
                                                                                                       computation_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
