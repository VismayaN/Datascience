#write a program to append a file with the contents of another file.

fn1 = input("enter first file name: ")
fn2 = input("enter second file name: ")
sourceFile = open(fn1, "r")
data1 = sourceFile.read()
sourceFile.close()
f1= open(fn1, "r")
f2 = open(fn2, "a")
f2.write("\n")
f2.write(data1)
f2.close()


