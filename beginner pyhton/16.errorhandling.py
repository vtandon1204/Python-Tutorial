# Try & Except block of code
text = input('Username: ')
try:
    num = int(text) # it puts a constraint that the text should be integer/ numerical value only
    print(num)
except:
    # this 'except' block of code will run if the 'try' block of code returns an error
    print('invalid username')
