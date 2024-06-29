f = open("D:\\technical\\AI & ML\\1. Python\\1. beginner python\\file.txt","r")
# w : write mode
# a : append mode
# r : read mode
# r+ : opens file with both read and write mode
# w+ : opens file with both read and write mode
 
# f.write("\nI'm Vaibhav Tandon")
# f.close()

# print(f.read())
# f.close()
f_out = open("D:\\technical\\AI & ML\\1. Python\\1. beginner python\\file_word_count.txt","w")
for line in f:
    tokens = line.split(' ') 
    # seperators as space in between the words and return a list(array) of words
    f_out.write(line+" word count: "+str(len(tokens))+'\n')
    # print('\n')
    # print(len(tokens))
    
    
f.close()
f_out.close()
