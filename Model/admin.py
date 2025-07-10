# import sqlite3
# import random
# from faker import Faker
# import os
# current_dir = os.path.dirname(os.path.abspath(__file__))

# db_path = os.path.join(current_dir, 'database.db')


# fake = Faker()

# conn = sqlite3.connect(db_path)
# sql = conn.cursor()

# # Create table if not exists (same as your code)
# sql.execute("""CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     card_number INTEGER,
#     pin INTEGER(6),
#     balance REAL DEFAULT 0.0
# )""")

# # Function to generate unique 4-digit card numbers
# def generate_unique_card_numbers(count):
#     numbers = set()
#     while len(numbers) < count:
#         num = random.randint(1000, 9999)
#         numbers.add(num)
#     return list(numbers)

# card_numbers = generate_unique_card_numbers(100)

# # Insert 100 dummy records
# for i in range(100):
#     name = fake.name()
#     card_number = card_numbers[i]
#     pin = random.randint(100000, 999999)  # 6-digit PIN
#     balance = round(random.uniform(0, 10000), 2)  # Random balance between 0 and 10,000
    
#     sql.execute("INSERT INTO users (name, card_number, pin, balance) VALUES (?, ?, ?, ?)",
#                 (name, card_number, pin, balance))

# # Commit changes and close connection


# results = sql.execute("SELECT card_number,pin FROM users ",).fetchall()

# print('-------------------------')
# print(f"|card_number|\tpin\t|")
# print('-------------------------')

# for result in results:
  
#   print(f"|\t{result[0]}|\t{result[1]}\t|")


# conn.commit()
# conn.close()

# print("Successfully inserted 100 dummy records!")