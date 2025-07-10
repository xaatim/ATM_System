
from Model.db import connection, cursor as sql

def update_balance(newBalance:float,card_no:int):
  sql.execute("UPDATE users SET balance = ? where card_number = ?",(newBalance,card_no,))
  connection.commit()

  
def show_balance(card_no:int):
  rows = sql.execute("SELECT balance FROM users where card_number = ?",(card_no,)).fetchone()
  
  return rows[0]


def card_validation(card_no:int):
  print(f"entered card number is:{card_no}",)
  result = sql.execute("SELECT card_number FROM users where card_number = ?",(card_no,)).fetchone()
  if result == None:
    print(f'this card no ({card_no}) is not registered ')
    return
  
def pin_validation(pin_no:int):
  result = sql.execute("SELECT pin FROM users where pin = ?",(pin_no,)).fetchone()
  if result == None:
    print(f'invalid credentials')
    return  False



