# While you're here
count = 0

if count < 5:
  print("Hello, I am an if statement and count is", count)

while count < 10:
  print("Hello, I am a while and count is", count)
  count += 1

# Condition
loop_condition = True

while loop_condition:
  print("I am a loop")
  loop_condition = False

# While you're at it
num = 1

while num <= 10:  # Fill in the condition
  # Print num squared
  print(num ** 2)
  # Increment num (make sure to do this!)
  num += 1

# Simple errors
choice = raw_input('Enjoying the course? (y/n)')

while choice!='y' and choice!='n':  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")

# Infinite loops
count = 0

while True: # Add a colon
  print(count)
  # Increment count
  count += 1
  if count >= 10:
    break

# Your own while / else
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print("You win!")
    break
  guesses_left -= 1
else:
  print("You lose.")

# For your health
print("Counting...")

for i in range(20):
  print(i)

# For your hobbies
hobbies = []

# Add your code below!

for num in range(3):
  hobby =  raw_input("Tell me one of your favorite hobbies: ")
  hobbies.append(hobby)

print(hobbies)

# For your strings
thing = "spam!"

for c in thing:
  print(c)

word = "eggs!"

# Your code here!
for c in word:
  print(c)

# For your A
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == "A" or char == "a":
    print("X",)
  else:
    print(char,)


#Don't delete this print statement!
print

# For your lists
numbers  = [7, 9, 12, 54, 99]

print("This list contains: ")

for num in numbers:
  print(num)

# Add your loop below!
for num in numbers:
  print(num**2)

# Looping over a dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print(key, d[key])

# Counting as you go
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
  print(index+1, item)

# Multiple lists
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
    print(max(a, b))

# Change it up
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!' # (It actually is.))
    print('A', f)
else:
    print('A fine selection of fruits!')

# Create your own
    test = ["bleh", "blah", "bloh"]

    for x in test:
      print(
    x)
    else:
    print(
    "ok")