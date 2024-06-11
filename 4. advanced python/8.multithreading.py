# running multiple instances of a program (threads) in a single core of a multicore system
import threading

def test(id):
    print("program starts %d"% id)
    
# test(1)

thread = [threading.Thread(target=test, args=(i,)) for i in range(10)]
for t in thread:
    t.start()
    
print(thread)
print(id(thread))

#********************************************************************************************************************

import urllib.request

def file_download(url, filname):
    urllib.request.urlretrieve(url, filname )
    
file_download('https://raw.githubusercontent.com/vtandon1204/DSA-Sheet/main/1.%20Basics/C%2B%2B_STL/vectors.cpp', 'vectors.txt')
file_download('https://raw.githubusercontent.com/vtandon1204/DSA-Sheet/main/1.%20Basics/C%2B%2B_STL/set.cpp','sets.txt')
file_download('https://raw.githubusercontent.com/vtandon1204/DSA-Sheet/main/1.%20Basics/C%2B%2B_STL/pairs.cpp','pairs.txt')
# this will manually run this program in different cores of computer

# but i wish to run it in a single core of computer
url_list=['https://raw.githubusercontent.com/vtandon1204/DSA-Sheet/main/1.%20Basics/C%2B%2B_STL/vectors.cpp',
          'https://raw.githubusercontent.com/vtandon1204/DSA-Sheet/main/1.%20Basics/C%2B%2B_STL/set.cpp',
          'https://raw.githubusercontent.com/vtandon1204/DSA-Sheet/main/1.%20Basics/C%2B%2B_STL/pairs.cpp']

file_list = ['vectors.txt','sets.txt','pairs.txt']

thread1= [threading.Thread(target=file_download, args=(url_list[i],file_list[i])) for i in range(len(url_list))]

for t in thread1:
    t.start()
    
#*******************************************************************************************************************

import time
import threading
def test1(id):
    for i in range(10):
        print('test1 %d printing %d %s' %(id,i,time.ctime()))
        time.sleep(1) 

# test1(1)

thread2=[threading.Thread(target=test1, args=(i,)) for i in range (3)]

# sabse pehle har ek id ke liye 0th (i) chlega, fir next id's ke liye 1st (i) chlega and so on
# 0 id --> 0
# 1 id --> 0
# 2 id --> 0
# 0 id --> 1
# 1 id --> 1
# 2 id --> 1

for t in thread2:
    t.start()