import random
 
print('H A N G M A N')
 
user_choice = input('Type "play" to play the game, "exit" to quit:')
if user_choice == 'play':
   word_bank = ['python', 'java', 'kotlin', 'javascript']
   word = random.choice(word_bank)
      
   length = len(word)
   letters = set(word)
   hyphen = '-'*length
 
   ascii_letter = 'abcdefghijklmnopqrstuvwxyz'
 
   attempts = 8
   tried =[]
   while attempts > 0:  
       print('\n', hyphen)
       letter = input('Input a letter:')
          
       if letter in tried:
           print('You already typed this letter')
      
       elif letter in letters:
           hyphen = ''.join([letter if word[i] == letter else hyphen[i] for i in range(len(hyphen))])
           tried.append(letter)
          
       elif len(letter) > 1:
           print('You should input a single letter')
         
       elif letter not in ascii_letter:
           print('It is not an ASCII lowercase letter')
      
       else:
           attempts -= 1
           tried.append(letter)
           print('No such letter in the word')
          
   if word:
       print("""You guessed the word!
   You survived!""")
   else:
       print('You are hanged!')
          
else:
   user_choice = input('Type "play" to play the game, "exit" to quit:')
