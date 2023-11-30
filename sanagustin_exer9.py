file1 = open("hmm.in", "r");

# initialize total probabilities dictionaries
totalProbabilities = {}
totalProbabilities2 = {}

# initialize transition probabilities
TS = 0
ST = 0
TT = 0
SS = 0

# computes for the total probability of a state using 
def getTotalProbability(state):
    # get count
    stateCount = int(state[1])
   
    sValue = totalProbabilities[stateCount-1][0] 
    tValue = totalProbabilities[stateCount-1][1] 
    
    if state[0] == "T":
        prob = (TS * sValue) + (TT * tValue)
    else:
        prob = (ST * tValue) + (SS * sValue)
        
    return prob

# computes for the total probability of either E or F
def getTotalProbability2(state):
    # get count
    stateCount = int(state[1])
    
    sValue = totalProbabilities[stateCount][0]
    tValue = totalProbabilities[stateCount][1]
    
    if state[0] == "E":
        prob = (ES * sValue) + (ET * tValue)
    else:
        prob = (FS * sValue) + (FT * tValue)
        
    return prob
    

# gets the probability of a state given another state using bayes rule
def useBayesRule(state, given):
    count = int(state[1])
    # if state is S1, find T1
    if state[0] == "S":
        # compute for the total probability of T[count]
        if totalProbabilities[count][1]:
            tCount = totalProbabilities[count][1]
            sCount = 1 - tCount
            
            # save sCount
            totalProbabilities[count][0] = sCount
        else:
            tState = "T" + str(count)
            totalProbabilities[count][1] = getTotalProbability(tState)
            tCount = totalProbabilities[count][1]
            sCount = 1 - tCount # sCount
            
            # save sCount
            totalProbabilities[count][0] = sCount
        
        # get the value of E[count]
        if totalProbabilities2[count][0]:
            eCount = totalProbabilities2[count][0]
        else:
            eState = "E" + str(count)
            totalProbabilities2[count][0] = getTotalProbability2(eState)
            eCount = totalProbabilities2[count][0]
            
        # compute for the probability of state given another state
        prob = (ES * sCount) / eCount
        return prob
    else: 
        # compute for the total probability of T[count]
        if totalProbabilities[count][1]:
            tCount = totalProbabilities[count][1]
            sCount = 1 - tCount
            
            # save sCount
            totalProbabilities[count][0] = sCount
        else:
            tState = "T" + str(count)
            totalProbabilities[count][1] = getTotalProbability(tState)
            tCount = totalProbabilities[count][1]
            sCount = 1 - tCount # sCount
            
            # save sCount
            totalProbabilities[count][0] = sCount
        
        # get the value of F[count]
        if totalProbabilities2[count][1]:
            fCount = totalProbabilities2[count][1]
        else:
            fState = "F" + str(count)
            totalProbabilities2[count][1] = getTotalProbability2(fState)
            fCount = totalProbabilities2[count][1]
            
        # compute for the probability of state given another state
        prob = (FT * tCount) / fCount
        return prob
        
    
# computes for the probability of a state in a sequence
def probabilityComputer(sequence, state, prevState):
    prevStateCount = 0
    stateCount = 0

    # get count of state with next state    
    # as well as count of state whose next state is nextState
    for i in range(len(sequence) - 1):
        if sequence[i] == prevState:
            prevStateCount += 1
            if sequence[i+1] == state:
                stateCount += 1
    
    # compute for the probability
    probability = stateCount / prevStateCount
    return probability
    
    
# get all probabilities of states given a sequence
def getProbabilityOfInitialState(sequence):
    firstChar = sequence[0]
    if firstChar == "S":
        S0 = 1
    else:
        S0 = 0
    return S0

# no of strings
noOfStrings = int(file1.readline().strip())

# get string sequences
sequences = []
for i in range(noOfStrings):
    sequences.append(file1.readline().strip())

# get possible values for each state
possibleValues1 = file1.readline().strip().split(" ");

# possible observable measurement values
possibleValues2 = file1.readline().strip().split(" ");

# get probabilities
probabilities1 = file1.readline().strip().split(" ");
ES = float(probabilities1[0])
FS = float(probabilities1[1])

probabilities2 = file1.readline().strip().split(" ");
ET = float(probabilities2[0])
FT = float(probabilities2[1])

# get # of cases
noOfCases = int(file1.readline().strip());

# inputs
input1 = file1.readline().strip()
input2 = file1.readline().strip()
input3 = file1.readline().strip()

file1.close()

# compute values of these probabilities
state1 = input1.split(" ")[0]
given1 = input1.split(" ")[2]
state2 = input2.split(" ")[0]
given2 = input2.split(" ")[2]
state3 = input3.split(" ")[0]
given3 = input3.split(" ")[2]

# save here the output
output = {}
for i in range(1, noOfStrings + 1):
    output[i] = []

# solves for the missing values in the input given a sequence
def inputSolver(sequence, count):
    global totalProbabilities, totalProbabilities2, output
    global TS, SS, TT, ST 
    
    # find s0 and t0 for the current sequence
    first_char = sequence[0]

    if first_char == "S":
        s0 = 1
        t0 = 0
    else:
        t0 = 1
        s0 = 0

    # get probabilities of different values first
    S0 = getProbabilityOfInitialState(sequence)
    if S0 == 1:
        T0 = 0
    else:
        T0 = 1
        
    # total probabilities of S and T
    totalProbabilities = {}
    for i in range(noOfCases + 1):
        totalProbabilities[i] = [None, None]
    
    # total probabilities of E and F 
    totalProbabilities2 = {}

    for i in range(1, noOfCases + 1):
        totalProbabilities2[i] = [None, None]

    # save S0 and T0 probabilities 
    totalProbabilities[0][0] = S0
    totalProbabilities[0][1] = T0

    # get transition probabilities from the sequence
    TS = probabilityComputer(sequence, "T", "S")
    ST = probabilityComputer(sequence, "S", "T")
    TT = probabilityComputer(sequence, "T", "T")
    SS = probabilityComputer(sequence, "S", "S")

    # get probabilities using bayes rule
    firstProb = useBayesRule(state1, given1)
    secondProb = useBayesRule(state2, given2)
    thirdProb = useBayesRule(state3, given3)

    # save probabilities
    output[count].append(firstProb)
    output[count].append(secondProb)
    output[count].append(thirdProb)
    
# solve for the inputs for a sequence using inputSolver
for i in range(1, noOfStrings + 1):
    inputSolver(sequences[i-1], i)
print(output[1])
print(output[2])