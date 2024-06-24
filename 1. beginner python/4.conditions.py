# CONDITIONAL STATEMENTS (if / elif / else)

# if condition == True:
#     do this
# Note: identation in python is very important, otherwise the code will not work

age=input('enter your age: ')
print(type(age))
if int(age) >= 18:
    print('you are an adult')
else:
    print('you are a child')
# Note: colon is important for a block of code (i.e after a if-else statement or loop)
# print(type(age))
    
height = input('enter the height: ')
if int(height) <= 1:
    print('you cannot ride, under 1m')
elif int(height) >= 3:
    print('you cannot ride, over 3m')
else: 
    print('you can ride')

# CHAINED CONDITIONALS (and/or)
x=2
y=3
if x==y and x+y==5: # both conditions should be True
    print('ran for AND')
if x==y or x+y==5: # either of conditions should be True
    print('ran for OR')
if not(x==y and x+y==5): # the negation of condition 
    print('ran for negation AND')

# NESTED CONDITIONALS STATEMENTS 
x=1
y=4
if x==2:
    if y==3:
        print('x=2 and y=3')
    else:
        print('x=2 and y!=3')
else:
    print('x!=2')