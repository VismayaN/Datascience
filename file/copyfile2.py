#write a program to copy a text file to another file.

f=open('firstfile')
s=open('secondfile','a')
for x in f.readlines():
    s.write(x)
f.close()
s.close()
print('copied successfully!!')