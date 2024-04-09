# .find(): it gives the index where the letter provided is first found.
# Note: if the certian letter is not present in the string the it return -1
string= 'Hello'
print(string.find('o')) 

# .count(): it gives the count of a certain letter in the string 
# Note: if the certian letter is not present in the string the it return 0
print(string.count('l')) 

string1 = input('type something: ')
if string1.count('_')>0:
    print('not good')
else:
    print('good')