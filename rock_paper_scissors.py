import random
lst= ['rock', 'paper', 'scissors']
 
scores = {}
 
file = open('rating.txt', 'r')

for line in file:
  name, score = line.split()
  scores[name] = int(score)
user_name = input("Enter your name: ")
print(f'Hello, {user_name}')

while True:
  player = input()
  computer = random.choice(lst)
  
   if player == '!exit':
      print('Bye!')
      break
  if player == "!rating":
      print(f'Your rating: {scores[user_name]}')
  if player not in lst:
      print('Invalid input')
    
  if player == 'scissors':
      if computer == 'rock':
          print('Sorry, but the computer chose rock')
      elif computer == 'paper':
          print('Well done. The computer chose paper and failed')
          scores[user_name] += 100
      else:
          print('There is a draw (scissors)')
          scores[user_name] += 50
          
  if player == 'paper':
      if computer == 'rock':
          print('Well done. The computer chose rock and failed')
          scores[user_name] += 100
      elif computer == 'scissors':
          print('Sorry, but the computer chose scissors')
      else:
          print('There is a draw (paper)')
          scores[user_name] += 50
          
  if player == 'rock':
      if computer == 'scissors':
          print('Well done. The computer chose scissors and failed')
          scores[user_name] += 100
      elif computer == 'paper':
          print('Sorry, but the computer chose paper')
      else:
          print('There is a draw (rock)')
          scores[user_name] += 50
