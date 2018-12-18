class StackMachine:
    def __init__(self):
        self.__Stack = []
        self.__Address = {}
        self.CurrentLine = 0

    def Execute(self, inputs):
        self.CurrentLine += 1

        if (inputs[0] == "push"):
            self.__Stack.append(int(inputs[1]))
            return

        elif(inputs[0] == "pop"):
            if(len(self.__Stack) == 0):
                raise IndexError("Invalid Memory Access")
            else:
                return self.__Stack.pop()

        elif(inputs[0] == "add"):
            if(len(self.__Stack) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                sum = self.__Stack.pop() + self.__Stack.pop()
                self.__Stack.append(sum)
                return

        elif(inputs[0] == "sub"):
            if(len(self.__Stack) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                sub = self.__Stack.pop() - self.__Stack.pop()
                self.__Stack.append(sub)
                return

        elif(inputs[0] == "mul"):
            if(len(self.__Stack) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                mult = self.__Stack.pop() * self.__Stack.pop()
                self.__Stack.append(mult)
                return

        elif(inputs[0] == "div"):
            if(len(self.__Stack) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                div = self.__Stack.pop() / self.__Stack.pop()
                self.__Stack.append(div)
                return

        elif(inputs[0] == "mod"):
            if(len(self.__Stack) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                mod = self.__Stack.pop() % self.__Stack.pop()
                self.__Stack.append(mod)
                return

        elif(inputs[0] == "skip"):
            if(len(self.__Stack) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                skipped = self.__Stack.pop()
                newLoc = self.__Stack.pop()
                if(skipped == 0):
                    self.CurrentLine += newLoc
                return

        elif(inputs[0] == "save"):
            if(len(self.__Stack) == 0):
                raise IndexError("Invalid Memory Access")
            else:
                token = self.__Stack.pop()
                address = int(inputs[1])
                self.__Address[address] = token
                return

        elif(inputs[0] == "get"):
            address = int(inputs[1])
            if(address in self.__Address):
                token = self.__Address[address]
                self.__Stack.append(token)
                return
            else:
                raise IndexError("Invalid Memory Access")
