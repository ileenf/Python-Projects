expression = input().split('|')
regex = expression[0]
string = expression[1]
 
def func(regex, string):
  
   if len(regex) == 0:
       return True
   else:
       if len(string) == 0:
           return False
       else:
           for i in range(len(regex)):
               if regex[i] == '.':
                   return func(regex[i+1:], string[i+1:])
               elif regex[i] != string[i]:
                   return func(regex, string[i+1:])
               else:
                   regex = regex[i+1:]
                   string = string[i+1:]
                   return func(regex, string)
              
print(func(regex, string))
