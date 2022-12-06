from time import sleep
import os
import requests

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = ROOT_DIR + '/data/'  # probably a better way to write this


def ping_reddit(sub):
    headers = {
        'user-agent': 'advocator-app/0.0.1'}
    r = requests.get('https://www.reddit.com/r/' + sub +
                     '/top.json?sort=top&t=day&limit=5', headers=headers)
    print(r.json())
    return r.json()


def topic_lookup(resource):
    topic_file = 'topics.txt'
    with open(DATA_DIR + topic_file, 'r') as f:
        topics = f.read().splitlines()
        for t in topics:
            if resource == 'reddit':
                ping_reddit(t)

            if len(topics) > 3:
                print('sleeping....')
                sleep(1)
                print('awake!!!!')


topic_lookup('reddit')
