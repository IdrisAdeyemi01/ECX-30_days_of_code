#day 1
def is_perfect_square(number):
     #function_name: is_perfect_square
     #parameter: number: enter number as input
     #returns: True if the number is  a perfect square and False if it isnt
  
  try:    
   root  =  int(number)**(1/2)
   if root % 1 == 0:
      return True
   else:
      return False
  except ValueError:
      print("Enter numbers only")
number = input("Enter number you want to check: ")
print(is_perfect_square(9))