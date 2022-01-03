#write a program to compare two files.

import filecmp
f1=open('firstfile','r')
f2=open('secondfile','r')
print(filecmp.cmp('firstfile','secondfile'))