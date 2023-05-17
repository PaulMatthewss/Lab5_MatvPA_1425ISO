import sqlalchemy as db
import datetime

engine = db.create_engine('sqlite:///model.db')

connection = engine.connect()

metadata = db.MetaData()

wins = db.Table('wins', metadata,
    db.Column('who_wins', db.Text),
    db.Column('When_wins', db.DateTime))

metadata.create_all(engine)