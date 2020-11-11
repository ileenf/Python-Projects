numbers = input()
if numbers != '/exit' and numbers != '/help':
   nums = numbers.split()
   nums = [int(x) for x in nums]
check = True
 
 
while numbers!='/exit':
      
   if check:
       numbers = input()
       nums = numbers.split()
       nums = [int(x) for x in nums]
 
   if numbers == '':
       check = True
       continue
   else:
       print(sum(nums))
       check = False
      
   numbers = input()
   if numbers == '/exit':
       break
   elif numbers == '/help':
       print('The program calculates the sum of numbers')
   nums = numbers.split()
   nums = [int(x) for x in nums]
      
print('Bye!')
