import random
        
Welcome_note = "\033[34mWELCOME TO THE GAME OF ODD EVEN\033[0m"

print(Welcome_note.center(500))

allowed_strings = {"even", "odd"}

def Users_input_among_odd_even():
  user_input = str(input("Enter 'Even' or 'Odd': ")).lower()
  if user_input in allowed_strings:
   return user_input
  else:
   raise ValueError("\033[31mNot an allowed string. Exiting the program.\033[0m")

chosen_string = Users_input_among_odd_even()

print(f"Users Choose : {chosen_string}")

allowed_integers = {1,2,3,4,5,6}

def Users_input_Between_1_and_6():
  users_input = int(input("Enter any Number B/w 1 to 6 : "))
  if users_input in allowed_integers:
   return users_input
  else:
   raise ValueError("\033[31mNot an allowed integer. Exiting the program.\033[0m")

users_call = Users_input_Between_1_and_6()

Computers_call = random.randint(1, 6)

print(f'Number Selected By Computer : ',Computers_call)

sum = users_call + Computers_call

print(f'Sum is : ',sum)

if sum % 2 == 0 :
 result1 = "even"
 print("It's EVEN")
 if chosen_string == result1:
   print("\033[32mCONGRATULATIONS :::: YOU WON\033[0m".center(500))
 else:
   print("\033[31mOOPS ::: YOU LOOSE\033[0m".center(500))

else:
 result2 = "odd"
 print("That's ODD")
 if chosen_string == result2:
   print("\033[32mCONGRATULATIONS :::: YOU WON\033[0m".center(500))
 else:
   print("\033[31mOOPS ::: YOU LOOSE\033[0m".center(500))
