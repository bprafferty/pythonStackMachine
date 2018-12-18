
allTokens = ['push', 'pop', 'add', 'sub',
            'mul', 'div', 'mod', 'skip',
            'save', 'get']

duoTokens = ['push', 'save', 'get']

soloTokens = ['pop', 'add', 'sub', 'mul',
            'div', 'mod', 'skip']



def Tokenize(str):

    inputs = str.split()
    numTokens = len(inputs)

    for i in range(0, numTokens):
        token = inputs[i]
        if(numCheck(token) is False and not token in allTokens):
            raise ValueError("Unexpected Token: " + token)

    return inputs

def numCheck(secondToken):
    try:
        int(secondToken)
        return True
    except ValueError:
        return False


def Parse(inputs):

    numTokens = len(inputs)

    if(numTokens == 1 and inputs[0] in soloTokens):
        return True
    elif(numTokens == 2 and inputs[0] in duoTokens and numCheck(inputs[1]) is True):
        return True

    return False
