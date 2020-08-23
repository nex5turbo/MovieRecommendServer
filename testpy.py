from sys import argv
from sys import stdout

inputData = int(argv[1])

if(inputData > 10):
    print("hello upper than 10")
    stdout.flush()

else:
    print("hello lower than 10")
    stdout.flush()
