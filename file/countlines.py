#write a program to count the no:of lines in a file.

with open('firstfile','r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)