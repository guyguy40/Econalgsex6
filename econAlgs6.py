"""
    this is a submission for question 3. information:
    name - Guy Wolf
    ID - 212055966
"""

#the question has a problem in it - there is no total value to fill. I therefore added a global value named "total" with exactly that

"""
    IMPORTANT:
    I had a pretty tough week so this is an upload which is complete only for algorithm A without much documentation, which is the bare minimum to pass.
    This was made so that I could submit by 8PM.
    By tommorow in class I will update the github repo to include a full documented solution.
"""

weights = [1,2,3,4,5]
total = 10

def choicesAFull(values):
    weightsNum = len(weights)
    ret = [0 for i in range(weightsNum)]
    toFill = total
    toSort = [(i,values[i]) for i in range(weightsNum)]
    toSort.sort(key=lambda x : x[1], reverse = True)
    totalValue = 0
    for val in toSort:
        if weights[val[0]] <= toFill:
            ret[val[0]] = 1
            toFill -= weights[val[0]]
            totalValue += values[val[0]]
    return (ret, totalValue)  

def choicesBFull(values):
    pass

def choicesA(values):
    return choicesAFull(values)[0]

def choicesB(values):
    return choicesBFull(values)[0]

def choicesFull(values):
    ARes = choicesAFull(values)
    BRes = choicesBFull(values)
    if ARes[1] >= BRes[1]:
        return (ARes[0],0)
    return (Bres[0],1)

def choices(values):
    return choicesFull(values)[0]

def paymentsAMemo(value, choices):
    PassValue = -float("inf")
    for i in range(len(choices)):
        if choices[i] == 0:
            if values[i] > passValue:
                passValue = values[i]
    return [passValue if choice == 1 else 0 for choice in choices]

def paymentsBMemo(values, choices):
    pass

def paymentsA(values):
    return paymentsAMemo(values, choicesA(values))

def paymentsB(values):
    return paymentsBMemo(values, choicesB(values))

def payments(values):
    fullChoices = choicesFull(values)
    if fullChoices[1] == 0:
        return paymentsAMemo(values, fullChoices[0])
    return paymentsBMemo(values, fullChoices[0])


