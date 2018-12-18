import prog4_1 as p1
import prog4_2 as p2
import sys

def main():
    print("Assignment #4-3, Brian Rafferty, bprafferty03@gmail.com")
    executableContents = []
    stack = p2.StackMachine()

    file = open(sys.argv[1], 'r')
    fileContents = [x.strip() for x in file.readlines()]
    numLines = len(fileContents)

    for index in range(0, numLines):
        checkLine = fileContents[index]
        try:
            executableContents.append(p1.Tokenize(checkLine))
        except ValueError as error:
            print("Error on line " + str(index+1) + ": " + str(error))
            return

    for index in range(0, numLines):
        checkLine = fileContents[index]
        if(not p1.Parse(executableContents[index])):
            print("Parse error on line "+ str(index+1) + ": " + str(fileContents[index]))
            return

    inputLength = len(executableContents)
    while(stack.CurrentLine < inputLength):
        if(stack.CurrentLine < 0):
            print("Trying to execute invalid line: " + stack.CurrentLine)
            return
        try:
            callStack = stack.Execute(executableContents[stack.CurrentLine])
            if(callStack != None):
                print(callStack)
        except IndexError:
            print("Line " + str(stack.CurrentLine) + ": " + fileContents[stack.CurrentLine - 1] + " caused Invalid Memory Access")
            return

    print("Program terminated correctly")


if __name__ == "__main__":
    main()
