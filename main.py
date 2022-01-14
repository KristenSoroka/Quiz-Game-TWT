print("Welcome to my Taylor Swift quiz!")

playing = input("Do you want to play?(yes/no) ").lower()
print(playing)

#if statement checking if the person wants to playing
#the if statement reads: if the playing variable is NOT EQUAL to yes then quit the program.
if playing != "yes":
  quit()
else:
  print("Okay! let's play!")

#start of quiz questions code

# Q1
ans = int(input("What is Taylor's favorite number? "))
if ans == 13:
  print("Correct!")
else: 
  print("Incorrect!")

# Q2
ans = int(input("How many cats does she own? "))
if ans == 3:
  print("Correct!")
else: 
  print("Incorrect!")

# Q3
ans = input("Finish this lyric: 'Darling, I\'m a nightmare...' ").lower()
if ans == "dressed like a daydream":
  print("Correct!")
else: 
  print("Incorrect!")

#Q4
ans = input("What is Taylor's middle name? ").capitalize()
if ans == "Alison":
  print("Correct!")
else: 
  print("Incorrect!")

