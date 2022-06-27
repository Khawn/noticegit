a = 1 
if a < 1000:
    b = a  + 1
    a += 1
    print(a ,'is a')
else :
    print('fall')

c = [i for i in range(10)]
print(c)

d = '1'
print(type(int(d)))

e = 'spliet test'
print(e.upper().split(' '))

print('你好')

name = input('your name :')

print(name)

import pandas as pd
df = pd.read_csv(flict.txt,sep=',')
df.head(5)
