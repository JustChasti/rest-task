import sys
import requests
import json
import random
import string
import time

from sqlalchemy.sql.expression import true
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from coding import get_hash
import config
import base


Base = declarative_base()
url = config.url + 'bl'
shortl = config.url + 'bs'


def add_link(engine):
    data = {}
    try:
        answer = requests.get(url, data=json.dumps(data), headers=config.headers).json()
        for i in answer:
            link = i.get('link')
            if base.findl(engine, link) is False:
                base.append_val(engine, link, get_hash(link))
                print(True, link, get_hash(link))
            else:
                k = 0
                sl = get_hash(link)
                print(False, link, sl)
                while (base.finds(engine, sl) is True) and k < 1000:
                    newlink = "".join([random.choice(string.ascii_letters) for j in range(20)])
                    k += 1
                    print(k, newlink)
                    sl = get_hash(newlink)
                    print(sl)
                base.append_val(engine, link, sl)
    except:
        print('request clear')


def get_links(engine):
    data = {}
    try:
        answer = requests.get(shortl, data=json.dumps(data), headers=config.headers).json()
        out = [] 
        for i in answer:
            out.append({'addres': i.get('addres'), 'link': base.find(engine, i.get('short'))})
        answer = requests.post(shortl, data=json.dumps(out), headers=config.headers)
        print(answer)
    except:
        print('request clear')


def work(timer, engine):
    while True:
        add_link(engine)
        get_links(engine)
        time.sleep(timer)


if __name__ == "__main__":
    engine = base.conn(config.base_user, config.base_pass, config.base_name)
    work(30, engine)
