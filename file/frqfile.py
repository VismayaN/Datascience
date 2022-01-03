#write a program to count the frequencies of each word from a file.


from collections import Counter
def word_count():
        with open('firstfile') as f:
                return Counter(f.read().split())
print("Number of input words in the file :",word_count())