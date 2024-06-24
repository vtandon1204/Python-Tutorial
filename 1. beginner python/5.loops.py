# FOR LOOPS
for x in range(0,11,5): #(start, stop, step) --> (int x=0,x<11,x++)
    print(x)
    
# WHILE LOOPS
# while condition == True:
#     do this
#     break
loop = True
while loop:
    name=input('enter something: ')
    print(name)
    if name=='stop':
        loop = False
        # break