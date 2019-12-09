"""
    this is a submission for question 3. information:
    name - Guy Wolf
    ID - 212055966
"""

#the question has a problem in it - there is no total value to fill. I therefore added a global value named "total" with exactly that
weights = [1,2,3,4,5]
total = 10


def choicesGeneric(values, order):
    weightsNum = len(weights)
    ret = [0 for i in range(weightsNum)]
    toFill = total

    #sort all agents by their values
    toSort = [(i,order(values[i], weights[i])) for i in range(weightsNum)]
    toSort.sort(key=lambda x : x[1], reverse = True)
    totalValue = 0

    #iterate over all agents by order
    for val in toSort:
        #if the agent can be added to the bag add it
        if weights[val[0]] <= toFill:
            ret[val[0]] = 1
            toFill -= weights[val[0]]
            totalValue += values[val[0]]
    return (ret, totalValue) 

def choicesAFull(values):
    return choicesGeneric(values, lambda value,weight : value)

def choicesBFull(values):
    return choicesGeneric(values, lambda value,weight : value/weight)

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

def paymentsAMemo(values, choices):
    #calculate the total leftover of the bag
    assignedWeights = [weights[i] for i in range(len(choices)) if choices[i] == 1]
    leftover = total - sum(assignedWeights)

    #sort the choices based on weights, reversed
    choicesOrganized = [(i, weights[i]) for i in range(len(choices)) if choices[i] == 1]
    choicesOrganized.sort(key = lambda x: x[1], reverse = True)

    #sort the non choices based on value, reversed
    notChoicesOrg = [(i, values[i]) for i in range(len(choices)) if choices[i] == 0]
    notChoicesOrg.sort(key = lambda x: x[1], reverse = True)

    res = [0 for _ in range(len(choices))]
    j = 0
    for i in range(len(choicesOrganized)):
        #get to the first index where the choice at i can be replaced with the choice at j
        while weights[notChoicesOrg[j][0]] > choicesOrganized[i][1] + leftover:
            j += 1
            #if the length is maximal
            if j == len(notChoicesOrg):
                return res
        #the required payment is the value of said index - the minimum value to declare and win
        res[choicesOrganized[i][0]] = values[notChoicesOrg[j][0]]
    return res

def paymentsBMemo(values, choices):
    #calculate the total leftover of the bag
    assignedWeights = [weights[i] for i in range(len(choices)) if choices[i] == 1]
    leftover = total - sum(assignedWeights)

    #sort the choices based on weights, reversed
    choicesOrganized = [(i, weights[i]) for i in range(len(choices)) if choices[i] == 1]
    choicesOrganized.sort(key = lambda x: x[1], reverse = True)

    #sort the non choices based on value, reversed
    notChoicesOrg = [(i, values[i]/weights[i]) for i in range(len(choices)) if choices[i] == 0]
    notChoicesOrg.sort(key = lambda x: x[1], reverse = True)

    res = [0 for _ in range(len(choices))]
    for i in range(len(choicesOrganized)):
        #get to the first index where the choice at i can be replaced with the choice at j
        for val in notChoicesOrg:
            if weights[val[0]] <= choicesOrganized[i][1] + leftover:
                #the required payment is the value of said index - the minimum value to declare and win
                res[choicesOrganized[i][0]] = values[val[0]]
    return res

def paymentsA(values):
    return paymentsAMemo(values, choicesA(values))

def paymentsB(values):
    return paymentsBMemo(values, choicesB(values))

def payments(values):
    fullChoices = choicesFull(values)
    if fullChoices[1] == 0:
        return paymentsAMemo(values, fullChoices[0])
    return paymentsBMemo(values, fullChoices[0])

#testing code
values = [1,2,3,4,5]

print(choices(values))
print(payments(values))
