print('Welcome to my Comic Quiz!')
print('You get 10 points for each question.')
print('Can you get 100 points?')
print('')
print('Question 1')
print('Who is the First Marvel Comic Superhero?')
print('(A) The Human Torch')
print('(B) Iron Man')
print('(C) Spider-Man')

score = 0

print()
q1 = input('Your answer? ')
print()

if q1 == 'A':
    print('Correct! +10 points')
    print()
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 2')
print('Who has not been a Fantastic Four Member?')
print('(A) She-Hulk')
print('(B) Daredevil')
print('(C) Spider-Man')
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

print('Question 3')
print('Which of the following is not an era of Marvel Comics?')
print('(A) Diamond Age')
print('(B) Silver Age')
print('(C) Bronze Age')
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
print('When was the first Marvel Comic published?')
print('(A) 1929')
print('(B) 1939')
print('(C) 1949')
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
print('When was the first Avengers Comic Published?')
print('(A) 1963')
print('(B) 1964')
print('(C) 1965')
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
print('When was the first X-Men Comic Published?')
print('(A) 1961')
print('(B) 1962')
print('(C) 1963')
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
print('Which hero did Stan Lee create?')
print('(A) Wolverine')
print('(B) Iron Man')
print('(C) Captain America')
print()
q7 = input('Your answer? ')
print()

if q7 == 'B':
    print('Correct! +10 points')
    print('')
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 8')
print('Who is the Stan Lees favorite character?')
print('(A) Spider-Man')
print('(B) Silver Surfer')
print('(C) Hulk')
print()
q8 = input('Your answer? ')
print()

if q8 == 'B':
    print('Correct! +10 points')
    print('')
    score = score + 10 
else :
    print('Incorrect answer')
    print()

print('Question 9')
print('Who Founded Marvel Comics?')
print('(A) Stan Lee')
print('(B) Martin Goodman')
print('(C) Steve Ditko')
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