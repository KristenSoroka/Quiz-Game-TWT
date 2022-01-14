print("Welcome to my Taylor Swift quiz!")

playing = input("Do you want to play?(yes/no) ").lower()
score = 0
total_points = 5

#if statement checking if the person wants to playing
#the if statement reads: if the playing variable is NOT EQUAL to yes then quit the program.
if playing != "yes":
  quit()
else:
  print("Okay! let's play!")

#start of quiz questions code

# Q1
ans = int(input("Question 1: What is Taylor's favorite number? (1pt) "))
if ans == 13:
  print("Correct!")
  score += 1
else: 
  print("Incorrect! The correct answer is 13")

# Q2
ans = int(input("Question 2: How many cats does she own? (1pt) "))
if ans == 3:
  print("Correct!")
  score += 1
else: 
  print("Incorrect! The correct answer is 3")

# Q3
ans = input("Question 3: Finish this lyric: 'Darling, I\'m a nightmare...' (2pts) ").lower()
if ans == "dressed like a daydream":
  print("Correct!")
  score += 2
else: 
  print("Incorrect! The correct answer is 'dressed like a daydream'")

#Q4
ans = input("Question 4: What is Taylor's middle name? (1pt) ").capitalize()
if ans == "Alison":
  print("Correct!")
  score += 1
else: 
  print("Incorrect! The correct answer is Alison")


print(f"You scored {score} / {total_points} pts")