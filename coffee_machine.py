class CoffeeMachine():
   money = 550
   water = 400
   milk = 540
   beans = 120
   cups = 9
    
   def remaining(self):
       if self.money != 0:
           print('''
           The coffee machine has:
           {0} of water
           {1} of milk
           {2} of coffee beans
           {3} of disposable cups
           ${4} of money'''.format(self.water, self.milk, self.beans, self.cups, self.money))
       else:
           print('''
           The coffee machine has:
           {0} of water
           {1} of milk
           {2} of coffee beans
           {3} of disposable cups
           0 of money'''.format(self.water, self.milk, self.beans, self.cups))
          
   def buy(self):
       coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
      
       if coffee == '1':
           if self.water < 250:
               print('Sorry, not enough water!')
          
           elif self.beans < 16:
               print('Sorry, not enough coffee beans!')
              
           else:
               print('I have enough resources, making you a coffee!')
               self.water -= 250
               self.beans -= 16
               self.money += 4
               self.cups -= 1
  
       elif coffee == '2':
           if self.water < 350:
               print('Sorry, not enough water!')  
              
           elif self.milk < 75:
               print('Sorry, not enough milk!')
              
           elif self.beans < 20:
               print('Sorry, not enough coffee beans!')
              
           else:
               print('I have enough resources, making you a coffee!')
               self.water -= 350
               self.milk -= 75
               self.beans -= 20
               self.money += 7
               self.cups -= 1
       elif coffee == '3':
           if self.water < 200:
               print('Sorry, not enough water!')
              
           elif self.milk < 100:
               print('Sorry, not enough milk!')
              
           elif self.beans < 12:
               print('Sorry, not enough coffee beans!')
              
           else:
               print('I have enough resources, making you a coffee!')
               self.water -= 200
               self.milk -= 100
               self.beans -= 12
               self.money += 6
               self.cups -= 1
          
       elif coffee == 'back':
           return
   def fill(self):
       self.water += int(input('Write how many ml of water do you want to add:'))
       self.milk += int(input('Write how many ml of milk do you want to add:'))
       self.beans += int(input('Write how many grams of coffee beans do you want to add:'))
       self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))
       
   def take(self):
       print('I gave you ${}'.format(self.money))
       self.money = 0
      
   def __init__(self):
      
       while True:
           action = input('Write action (buy, fill, take, remaining, exit):')
           if action == 'remaining':
               self.remaining()
           elif action == 'buy':
               self.buy()
           elif action == 'fill':
               self.fill()
           elif action == 'take':
               self.take()
           elif action == 'exit':
               break
          
coffee = CoffeeMachine()
