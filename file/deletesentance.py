#write a program to delete a sentence from the specified position in a file.


try:
    with open('firstfile', 'r') as fr:
        lines = fr.readlines()
        ptr = 1
        with open('firstfile', 'w') as fw:
            for line in lines:
                if ptr !=1:
                    fw.write(line)
                ptr += 1
    print("Deleted")

except:
    print("Error")