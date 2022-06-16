import time
import json
import os


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def read_config():
    path = os.path.abspath(".\config.json")
    with open(path) as f:
        config = json.load(f)
    return config
