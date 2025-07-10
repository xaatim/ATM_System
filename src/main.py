## requriements: 
    # balance checking capability 
    # deposit capability
    # withdrawin capability
import sys
import os
import requests
import time
import itertools
from threading import Thread
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.Queries import card_validation,update_balance,pin_validation,show_balance
from Model.db import connection
from server import app

def run_flask_server():
    import logging
    import contextlib
    log = logging.getLogger('werkzeug')
    log.disabled = True
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    app.logger.disabled = True
    app.logger.setLevel(logging.ERROR)

    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)


Thread(target=run_flask_server,daemon=True).start()
print("Flask server is running in the background...")


def wait_for_nfc(server_url="http://192.168.0.140:5000/nfc", timeout=30, poll_interval=0.1):
      spinner = itertools.cycle(['-', '/', '|', '\\'])
      
      print('Insert Your Card ',end="")
      while True:
          try:
              res = requests.get(server_url)
              if res.status_code == 200:
                  content = res.json()
                  if content.get('content') and content['content'].get('card_number'):
                      return content['content']['card_number'] 
                    
          except requests.exceptions.RequestException:
              break
            
          sys.stdout.write(next(spinner))
          sys.stdout.flush() 
          time.sleep(poll_interval)
          sys.stdout.write('\b') 
          
      raise TimeoutError("No NFC card detected within the timeout period.")

is_running = True

try:
    card_no = wait_for_nfc() 
except TimeoutError:
    print("Error: No NFC card detected. Exiting.")
    sys.exit(1)

def cleanup():
    requests.delete('http://192.168.0.140:5000/nfc')
    connection.close()
    
def main():

    
  def deposit ():
      
    user_input = input('Enter the ammount to be deposited: ')
    if user_input.isalpha():
      print('invalid input')
      return
    
    deposit = float(user_input)
    if deposit < 0 : 
      print('negative numbers are not valid')
      return
    
    print(f'you have deposited: ${deposit} into your account')
    total = show_balance(card_no) + deposit
    update_balance(total,card_no)
    print(f'your current balance is ${total}')
  

  def withdraw():

      user_input = input('enter the ammount to be withdrawn: ')
      
      if user_input.isalpha():
        print('invalid input')
        return
        
      money_to_be_withdrawn = float(user_input)
      if money_to_be_withdrawn < 0 : 
        print('negative numbers are not valid')
        return
      print(f'you have withdrawn ${money_to_be_withdrawn}')
      if money_to_be_withdrawn>show_balance(card_no):
        print('insuffecient fund')
        return
      total = show_balance(card_no) - money_to_be_withdrawn
      update_balance(total,card_no)
      print(f'your current balance is ${total}')

  def grettings():
    print('-----------------------------------')
    print('|           Banking Program       |','')
    print('-----------------------------------','\n')
    print('1. witdraw money')
    print('2. deposit money')
    print('3. check your balance')
    print('-----------------------------------')
    print()

  def Auth():
    print('-----------------------------------')
    print('|           Banking Program       |','')
    print('-----------------------------------','\n')
    card_validation(card_no)
    
    pin_input = input('insert your pin number(6 digits): ') 
    if pin_input.isalpha():
        print('invalid input')
        sys.exit(1)
    pin_no = int(pin_input)
    validation = pin_validation(pin_no)
    if validation == False:
      sys.exit(1)
      
  Auth()
  while is_running:
    
    grettings()
  
    choice = input('enter your choice: ')
    
    match choice:
      case '1':
        withdraw()
        
      case '2':
        deposit()
        
      case '3':
        print(f'your balance is ${show_balance(card_no)}')
        
      case _:
        print(f'{choice} is invalid')
        
    should_continue = input('do you want to continue(y/n): ')
    match should_continue.upper(): 
      case 'Y':
        continue
      case 'N':
        break
      case _:
        break
  
if __name__ == '__main__':
  try:
    print()
    main()
    cleanup()
  except (KeyboardInterrupt , SystemExit):
    cleanup()
    