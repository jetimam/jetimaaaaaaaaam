import re
import sys

def loan_calculator(amount, months, perc):
   plus = (amount / 100) * perc 
   payment = (amount + plus) / months 
   return payment 

def loan(): 
   print("You just entered the loan calculator!\nPlease enter the amount that you want to loan in euros.")
   ans = int(input())
   if ans>1000000000:
      print("This amount is too big we can not loan this!\n")
      return
   print("Please enter the amount of months you want to reimburse your loan ")
   months = int(input())  
   print("The amount you would need to pay each month is: " + str(loan_calculator(ans, months, (months /12))))

def interest_calculator(amount, year):
   return amount*(pow((1+2/2), 2*year))

def interest(): 
   print("You just entered the compound calculator!\nPlease enter the amount that you want invest in our portfolio.")
   ans = int(input())
   if ans>1000000000:
      print("This amount is too big we can not take this. That's what she said\n")
      interest()
   print("Please enter the amount of years that you want to take into account to see the result of the compounding")
   year = int(input())  
   print("The amount you will have at the end of time period is: " + str(interest_calculator(ans, year) + "euros"))

def refund():
   while True:
      n = int(input('Please enter how old your purchase is in weeks: '))
      if n > 3:
         print('We cannot give refunds on purchases older than 3 weeks, sorry.')
         break
      elif n < 0:
         print('Please enter a valid input.')
         continue
      else:
         print('We will get back to you on that!')
         break

patterns = {
   'make transfer to' : 'transfer made',
   'transfer': {
      'problem' : 'A transfer can take up to 3 days. If you haven\'t received your transfer in 3 days please contact the support.',
      'make' : 'If you wish to make a transfer, please use the syntax: "make transfer to <receiver_name>'
   },
   'loan' : {
      'take' : loan,
      'information' : 'You can only take a loan up to 1.000.000.000 EUR'
   },
   'refund' : {
      'ask for a' : refund,
      'information' : 'You can ask for a refund on spendings that are not older than 3 weeks.'
   },
   'investment' : {
      'information' : "You can invest only less than a 1.000.000.000 EUR. Our compound interest rate is 2%" +
                  ", and it is done twice a year. YUou can use the compound/investment calculator calculate to profit over a certain period",
      'calculator' : interest,
   },
   'compound' : {
      'information' : "You can invest only less than a 1.000.000.000 EUR. Our compound interest rate is 2%" +
                  ", and it is done twice a year. YUou can use the compound/investment calculator calculate to profit over a certain period",
      'calculator' : interest
   }
}

def reg(string):
   return r"(.*)" + re.escape(string) + r"(.*)"

def match(user_input, dict):
   for pattern in dict:
         result = re.match(reg(pattern), user_input)
         if result:
            if type(dict[pattern]) == str:
               print(dict[pattern])
               break
            elif type(dict[pattern]) == type(dict):
               match(user_input, dict[pattern])
            else:
               dict[pattern]()
         # else:
         #    n = input('I\'m sorry, I did not understand that. Would you like to talk to a real person? (y/n)')
         #    if n == 'y':
         #       print('We will get back to you ASAP!')
         #       sys.exit()
         #    else:
         #       break
               
def main_loop():
   while True:
      user_input = input('what do you have to say: ').lower().strip('.!')
      match(user_input, patterns)

if __name__ == "__main__":
   main_loop()