import os
import sqlite3

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'database.db')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()
