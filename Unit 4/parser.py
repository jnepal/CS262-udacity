#assumption chart[index] returns list
def addtochart(chart, index, state):
    if(state in chart[index]):
        return False
    elif(state not in chart[index]):
        chart[index] = [state]+chart[index]
        return True
#assume
#X -> ab.cd from j at chart[i]
#. is cursor
#j is the origin state
#i is current state i.e which chart state we are on or which token we are looking at
def closure(grammar, i, ab, cd, j):
    nextStates = [(rule[0],[],rule[1],i) #[] is the cursor position i.e dot(.)
                    for rule in grammar
                    if((len(cd) > 0 and rule[0] == cd[0]))]

    return nextStates

#assume
#X -> ab.cd from j at chart[i]3
#. is cursor
#j is origin state
#i is currentState is which chart state we are on or which token we are looking at
def shift(tokens,i, X, ab, cd, j):
    if(len(cd) > 0 and tokens[i] == cd[0]):
        return (X, ab + [cd[0]], cd[1:], j) #X -> abc.d
    else:
        return None


#assume
#X -> ab.cd from j at chart[i]
#. is cursor
#j is origin state
#i is currentState is which chart state we are on or which token we are looking at
#chart[j] has Y ->(tokens).X(tokens) from k

def reductions(chart, i, X, ab, cd, j):
    #we only perform reduction if X -> ab. i.e if cd is empty
    return [
            (jstate[0], jstate[1]+[X],(jstate[2])[1:], jstate[3])
            for jstate in chart[j]
            if(len(cd) == 0 and len(jstate[2]) > 0 and X == (jstate[2])[0])
    ]

def parse(tokens, grammar):
    tokens = tokens + ["end_of_input_marker"] # end_of_input_marker is lookahead pointer
    chart = {}
    startRule = grammar[0]
    for i in range(len(tokens)+1):
        chart[i] = [ ]
    startState = (startRule[0],[],startRule[1],0)
    chart[0] = [startState]
    for i in range(len(tokens)):
        while True:
            changes = False
            for state in chart[i]:
                # State === X-> ab.cd,j
                X = state[0]
                ab = state[1]
                cd = state[2]
                j  = state[3]

                # Current State == X -> ab.cd, j
                # Option 1 For each grammar rule c -> pqr
                # (Where the c's match)
                # make a next state        c -> .pqr, i
                # English : We're about to start parsing a"c", but
                # "c" may be something like "exp" with its own
                # production rules. We'll bring those production rules in

                nextStates = closure(grammar, i, ab, cd, j)
                for nextState in nextStates:
                    changes = addtochart(chart, i , nextState) or changes

                # Current State = X -> ab.cd , j
                # Option 2: If tokens[i] == c,
                # make next state       x -> abc.d,j
                # in chart [i+1]
                # English: We're looking for to parse token c next
                # and the current token is exactly c !
                # So we can parse over it and move to j+1

                nextState = shift(tokens, i , X, ab, cd, j)
                if nextState != None:
                    anyChanges = addtochart(chart, i+1, nextState) or anyChanges

                # Current State == X -> ab.cd, j
                # Option 3: If cd is [], the state is just X -> ab. ,j
                # for each p -> q.Xr, l in chart[j]
                # make a new state           p -> qX.r, l
                # in chart[i]
                # English: We just finished parsing an "x" with this token
                # but that may have been a sub-step(like matching "exp -> 2"
                # in "2+3"). We should update the higher-level rules as well.

                nextStates = reductions(chart, i , X, ab, cd, j)
                for nextState in nextStates:
                    changes = addtochart(chart, i, nextState) or changes

            # We're done if nothing changes
            if not changes:
                 break

    #print out the chart
    for i in range(len(tokens)):
        print("== chart " + str(i))
        for state in chart[i]:
            X = state[0]
            ab = state[1]
            cd = state[2]
            j = state[3]

            print ("   "+ X + "->"),
            for sym in ab:
                print(" "+ sym),
            print("."),
            for sym in cd:
                print(" "+ sym),
            print("  from " + str(j))

    acceptingState = (startRule[0], startRule[1], [], 0)
    return acceptingState in chart[len(tokens)-1]

# S -> P
# P -> ( P )
# P ->
# grammar = [
#     ("S", ["P"]),
#     ("P", ["(","P",")"]),
#     ("P", [ ])
# ]
#
# tokens = ["(","(",")",")"]
# tokens = ["(","(","(",")"]

# s -> PrisonerN
# N -> iN
# N -> i
# i -> [0-6]
# grammar = [
#     ("S", ["Prisoner", "N"]),
#     ("N", ["i", "N"]),
#     ("N", ["i"]),
#     ("i", ["0"]),
#     ("i", ["1"]),
#     ("i", ["2"]),
#     ("i", ["3"]),
#     ("i", ["4"]),
#     ("i", ["5"]),
#     ("i", ["6"])
#
# ]

# tokens = ["Prisoner","6"]
# tokens = ["Prisoner"]
# tokens = ["Prisoner", "2", "4", "6", "0", "1"]

# S -> T
# T -> aBc
# B -> bb
grammar = [
    ("S", ["T"]),
    ("T", ["a", "B", "c"]),
    ("B", ["b", "b"])
]

# tokens = ["a","b","b","c"]
tokens = ["a","b","c"]

result = parse(tokens, grammar)
print(result)

