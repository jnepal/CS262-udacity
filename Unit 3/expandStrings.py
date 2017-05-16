#Grammar for
# exp -> exp + exp
# exp -> exp - exp
# exp -> (exp)
# exp -> num

grammar = [
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"])
]

#for string "a exp"
#expanded to depth 1
# "a exp + exp"
# "a exp - exp"
# "a (exp)"
# "a num"

def expand(tokens, grammar):
    for pos in range(len(tokens)):
        for rule in grammar:
            if(tokens[pos] == rule[0]):
                yield(tokens[:pos]+rule[1]+tokens[pos+1:])

depth = 3
# utterances = [["exp"]] #start string
utterances = [["a","exp"]] #start string

for x in range(depth):
    for sentence in utterances:
        utterances = utterances + [i for i in expand(sentence, grammar)]

for sentence in utterances:
    print(sentence);


