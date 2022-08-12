print('Welcome to my MCU Quiz!')
print('You get 10 points for each question.')
print('Can you get 100 points?')
print('')
print('Question 1')
print('Who is the First Avenger?')
print('(A) Captain America')
print('(B) Iron Man')
print('(C) Nick Fury')

score = 0

print()
q1 = input('Your answer? ')
print()

if q1 == 'B':
    print('Correct! +10 points')
    print()
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 2')
print('What is Spider-Man real name?')
print('(A) Ben Parker')
print('(B) Bruce Wayne')
print('(C) Peter Parker')
print()
q2 = input('Your answer? ')
print()

if q2 == 'C':
    print('Correct! +10 points')
    print('')
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 3')
print('Who is the King of Wakanda?')
print('(A) Black Panther')
print('(B) Umbaku')
print('(C) Killmonger')
print()
q3 = input('Your answer? ')
print()

if q3 == 'A':
    print('Correct! +10 points')
    print('')
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 4')
print('Who is Captain Americas Best Friend?')
print('(A) Tony Stark')
print('(B) Bucky Barnes')
print('(C) Captain Marvel')
print()
q2 = input('Your answer? ')
print()

if q2 == 'B':
    print('Correct! +10 points')
    print('')
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 5')
print('Where did Black Widow train?')
print('(A) Red Room')
print('(B) Blue House')
print('(C) Yellow Closet')
print()
q5 = input('Your answer? ')
print()

if q5 == 'A':
    print('Correct! +10 points')
    print('')
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 6')
print('Who is the Strongest Avenger?')
print('(A) Hulk')
print('(B) Captain Marvel')
print('(C) Thor')
print()
q6 = input('Your answer? ')
print()

if q6 == 'C':
    print('Correct! +10 points')
    print('')
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 7')
print('Who is the Weakest Avenger?')
print('(A) Iron Patriot')
print('(B) Falcon')
print('(C) Hawkeye')
print()
q7 = input('Your answer? ')
print()

if q7 == 'C':
    print('Correct! +10 points')
    print('')
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 8')
print('Who is the Smartest Avenger?')
print('(A) Doctor Strange')
print('(B) Bruce Banner')
print('(C) Tony Stark')
print()
q8 = input('Your answer? ')
print()

if q8 == 'A':
    print('Correct! +10 points')
    print('')
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 9')
print('Who is the Strongest Villain?')
print('(A) Ultron')
print('(B) Scarlett Witch')
print('(C) Thanos')
print()
q9 = input('Your answer? ')
print()

if q9 == 'B':
    print('Correct! +10 points')
    print('')
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 10')
print('Is Marvel better than DC?')
print('(A) Yes')
print('(B) I dont know')
print('(C) No')
print()
q10 = input('Your answer? ')
print()

if q10 == 'A':
    print('Correct! +10 points')
    print('')
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print()
print('Congratulations!')
print('You earned ' + str(score) + '/100 points!')
print()