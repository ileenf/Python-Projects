import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal', default = 0)
parser.add_argument('--periods', default = 0)
parser.add_argument('--payment', default = 0)
parser.add_argument('--interest', default = 0.0)
 
print('What do you want to calculate?')
payment_type = input('type "n" for number of monthly payments,\ntype "a" for annuity monthly payment amount,\ntype "p" for credit principal:')
 
if payment_type == 'n':
   credit_principal = round(float(input('Enter the credit principal:')))
   monthly_payment = int(input('Enter the monthly payment:'))
   credit_interest = float(input('Enter the credit interest:'))
  
   i = (credit_interest/100)/12
   formula = monthly_payment/(monthly_payment - i * credit_principal)
   result = math.ceil(math.log(formula, i+1))
  
   years = result//12
   months = result % 12
  
   if years == 0 and months == 1:
       print('It will take 1 month to repay this credit!'.format)
      
   elif years == 1 and months == 0:
       print('It will take 1 year to repay this credit!'.format)
     
   elif months == 1:
       print('It will take {} years and 1 month to repay this credit!'.format(years))
      
   elif years == 1:
       print('It will take 1 year and {} month to repay this credit!'.format(months))
      
   else:
       print('It will take {0} years and {1} months to repay this credit!'.format(years, months))
elif payment_type == 'a':
   credit_principal = round(float(input('Enter the credit principal:')))
   periods = int(input('Enter the number of periods:'))
   credit_interest = float(input('Enter the credit interest:'))
  
   i = (credit_interest/100)/12
   p = credit_principal
   n = periods
  
   result = (p * i * math.pow(1+i, n))/(math.pow(1+i, n) - 1)
   result = math.ceil(result)
   print('Your monthly payment = {}!'.format(result))
  
elif payment_type == 'p':
   annuity = math.ceil(float(input('Enter the annuity payment:')))
   periods = int(input('Enter the number of periods:'))
   credit_interest = float(input('Enter the credit interest:'))
   i = (credit_interest/100)/12
   a = annuity
   n = periods
  
   top = i * math.pow(1+i, n)
   bottom = math.pow(1+i, n) - 1
   formula = (top/bottom)
   result = round(a/formula)
   result = int(math.floor(result/100000)*100000)
   print('Your credit principal = {}!'.format(result))
