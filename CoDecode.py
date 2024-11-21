# If the string has 3 characters or less, the string is reversed. If it has more than 3, then the first letter of the string is shifted to the last place and three random characters are appended at the beginning and end of the string.
import string
import random

def reverse(str1):
  str2 = ""
  for i in range(0, len(str1)):
    str2 = str2 + str1[len(str1)-(i+1)]
  return str2

def create_random_string():
 random_str = (random.choices(string.ascii_lowercase, k=3))
 f_random_str = "".join(random_str)
 return f_random_str

def code(str1):
  if len(str1) <= 3:
    return reverse(str1)
  else:
    newstr = ""
    for x in str1[1:len(str1)]:
      newstr = newstr + x
    str2 = newstr + str1[0]
    str3 = create_random_string() + str2 + create_random_string()
    return str3
    
def decode(str1):
  if(len(str1)<4):
    return(reverse(str1))
  else:
    str2 = str1[-4] + str1[3:-4]
    '''
    str2 = str1[3:len(str1)-3]
    str2 = str2[-1] + str2[:-1]
    ''' 
  return str2

for i in range(100):
  choice = int(input("Code = 0 \nDecode = 1\n"))
  input_string = input("Enter the String: ")
  string_list = input_string.split(" ")
  match choice:
    case 0: 
      for string_word in string_list:
        print(code(string_word), end = " ")
    case 1: 
      for string_word in string_list:
        print(decode(string_word), end = " ")
    case _:
      print("Wrong Input!")
  loop_input = input("\nContinue? (0): ")
  if (loop_input == "0"):
    break 
