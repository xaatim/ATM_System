## requriements: 
    # balance checking capability 
    # deposit capability
    # withdrawin capability

is_running = True

def main():
  def balance():
    with open('balance.txt') as b:
      balance = b.read()
      # x = [float(element) for element in balance]
      # total = sum(x)
      
      return float(balance)
    
  def deposit ():
      with open('balance.txt','a') as b:
        user_input = input('Enter the ammount to be deposited: ')
        if user_input.isalpha():
          print('invalid input')
          return
        deposit = float(user_input)
        if deposit < 0 : 
          print('negative numbers are not valid')
          return
        print(f'you have deposited: ${deposit} into your account')
        total = balance() + deposit
        with open('balance.txt','w'):

          b.writelines(f'{float(total)}\n')
      print(f'your current balance is ${total}')
  

  def withdraw():
    with open('balance.txt','a') as b:
      user_input = input('enter the ammount to be withdrawn: ')
      
      if user_input.isalpha():
        print('invalid input')
        return
        
      money_to_be_withdrawn = float(user_input)
      if money_to_be_withdrawn < 0 : 
        print('negative numbers are not valid')
        return
      print(f'you have withdrawn ${money_to_be_withdrawn}')
      if money_to_be_withdrawn>balance():
        print('insuffecient fund')
        return
      total = balance() - money_to_be_withdrawn
      with open('balance.txt','w'):
        pass
      b.writelines(f'{float(total)}\n')
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
    
  while is_running:
    
    grettings()
    
    choice = input('enter your choice: ')
    
    match choice:
      case '1':
        withdraw()
        
      case '2':
        deposit()
        
      case '3':
        print(f'your balance is ${balance()}')
        
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
  main()

