import re
import sys

def test():
   print('test')

patterns = {
   'make transfer to' : 'transfer made',
   'transfer': {
      'problem' : 'A transfer can take up to 3 days. If you haven\'t received your transfer in 3 days please contact the support.',
      'make' : 'If you wish to make a transfer, please use the syntax: "make transfer to <receiver_name>'
   },
   'hello world' : test
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
               
def main_loop():
   while True:
      user_input = input('what do you have to say: ').lower().strip('.!')
      if re.match(reg('goodbye'), user_input):
         print('hope we were of use')
         sys.exit()
      match(user_input, patterns)




if __name__ == "__main__":
   main_loop()


   # IDK 