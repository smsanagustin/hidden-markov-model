file1 = open("hmm.in", "r");

# no of strings
noOfStrings = int(file1.readline().strip())

# get string sequences
sequence1 = file1.readline().strip()
sequence2 = file1.readline().strip()

# get possible values for each state
possibleValues1 = file1.readline().strip().split(" ");

# possible observable measurement values
possibleValues2 = file1.readline().strip().split(" ");

# get probabilities
probabilities1 = file1.readline().strip().split(" ");
pes = float(probabilities1[0])
pfs = float(probabilities1[1])

probabilities2 = file1.readline().strip().split(" ");
pet = float(probabilities1[0])
pft = float(probabilities1[1])

# get # of cases
noOfCases = int(file1.readline().strip());

# inputs
input1 = file1.readline().strip()
input2 = file1.readline().strip()
input3 = file1.readline().strip()

file1.close()


# find s0 and t0 for sequence 1
first_char = sequence1[0]

if first_char == "S":
    s0 = 1
    t0 = 0
else:
    t0 = 1
    s0 = 0
    
# find inputs for sequence 1
find = input1.split(" ")[0]
given = input1.split(" ")[2]
print(find)
print(given)

def getProbability(state, given):
    probability = ()*() / ()