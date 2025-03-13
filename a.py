import sys
def printName(name):
    print(name)
if len(sys.argv)>1:
    print(sys.argv[1])
else:
    printName("Ram")

