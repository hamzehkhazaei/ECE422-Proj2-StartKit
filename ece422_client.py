"""
HTTP client simulator. It simulate a number of concurrent users and calculate the response time for each request.
"""

import requests
import time
import threading

swarm_master_ip = '10.2.9.108'  # ip address of the Swarm master node
think_time = 1  # the user think time (seconds) in between consequent requests
no_users = 3  # number of concurrent users sending request to the server


class MyThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name + str(self.counter))
        workload(self.name + str(self.counter))


def workload(user):
    while True:
        t0 = time.time()
        requests.get('http://' + swarm_master_ip + ':8000/')
        t1 = time.time()
        time.sleep(think_time)
        print("Response Time for " + user + " = " + str(t1 - t0))


if __name__ == "__main__":
    threads = []
    for i in range(no_users):
        threads.append(MyThread("User", i))

    for i in range(no_users):
        threads[i].start()

    for i in range(no_users):
        threads[i].join()
