from sqlalchemy.sql.expression import true
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
import create_base


Base = declarative_base()


class Link(Base):
    __tablename__ = 'link'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    short = Column(String(8), nullable=False)


def conn(user, passs, name):
    try:
        engine = create_engine("postgresql+psycopg2://" + user + ":" + passs + "@localhost/" + name)
        engine.connect()
    except:
        create_base.create(user, passs, name)
        engine = create_engine("postgresql+psycopg2://" + user + ":" + passs + "@localhost/" + name)
        engine.connect()
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

    return engine


def append_val(engine, lf, ls):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    link = Link(name=lf, short=ls)
    session.add(link)
    session.commit()


def findl(engine, sl):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        link = session.query(Link).filter(Link.name == sl).all()
        return True
    except:
        return False


def finds(engine, sl):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        link = session.query(Link).filter(Link.short == sl).all()
        return True
    except:
        return False


def find(engine, sl):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        link = session.query(Link).filter(Link.short == sl).all()
        return link[0].name
    except:
        return "this code isn't in the database"