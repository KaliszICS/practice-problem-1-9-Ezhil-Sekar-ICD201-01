

def q1(): 
  #Write Assignment code here
  print('"Hello World"')

def q2(): 
  #Write Assignment code here
  user = input("Input a word: ")
  print(user.lower())
  print(user.upper())

def q3(): 
  #Write Assignment code here
  user = input("Input a word that is at least 5 letters long: ")
  char_at_3 = user[3:4] 
  char_at_5 = user[5:6]  
  print(char_at_3, char_at_5)

def q4(): 
  #Write Assignment code here
  user = input("Input a word: ")
  print(user.index("o"))

def q5(): 
  #Write Assignment code here
  user = input("Input a word: ")
  print(len(user))



#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
q3()
q4()
q5()
