import unittest
from sqlalchemy import select, func
from db_model import Wins, Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
engine = create_engine("sqlite:///test_gameDB.db", echo=True)

Base.metadata.create_all(engine)

import sqlite3
connection = sqlite3.connect(r'test_gameDB.db')
cursor = connection.cursor()

class TestClass(unittest.TestCase):
    def setUp(self):
        self.tie = Wins
    
    def test_numo_rec(self):
        query = "DELETE FROM history"
        cursor.execute(query)
        connection.commit()
        with Session(engine) as session:
            tie = Wins(result = "Ничья")
            session.add_all([tie])
            session.commit()
            tie = Wins(result = "Ничья")
            session.add_all([tie])
            session.commit()
            tie = Wins(result = "Ничья")
            session.add_all([tie])
            session.commit()
        
        query = "SELECT COUNT(*) FROM history;"
        rows = cursor.execute(query).fetchall()
        rows = rows[0]
        self.assertEqual(rows[0], 3)
        
    def test_wright_data(self):
        with Session(engine) as session:
            tie = Wins(result = "Ничья")
            session.add_all([tie])
            session.commit()
            self.assertEqual(tie.result, "Ничья")


if __name__ == '__main__':
    unittest.main()