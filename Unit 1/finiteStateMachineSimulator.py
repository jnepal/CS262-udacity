

edges = {}

def fsmSimulator(input, finalNode, startNode=1 ):
    if(input == ''):
        if(startNode, '') in iter(edges):
            nextNode = edges[startNode, '']
        else:
            nextNode = None
    else:
        for char in input:
            if(startNode, char) in iter(edges):
                nextNode  = edges[startNode, char]
            else:
                nextNode = None
            startNode = nextNode
    if(nextNode in finalNode):
        print('valid String')
    else:
        print('invalid String')

#for regex = r'a+1+'
# edges[(1, 'a')] = 2
# edges[(2, 'a')] = 2
# edges[(2, '1')] = 3
# edges[(3, '1')] = 3
#
#
# fsmSimulator('aaa111', [3])
# fsmSimulator('', [1])

#for regex = 'q*'
# edges[1, ''] = 1
# edges[1, 'q'] = 1
#
# fsmSimulator('', [1])
# fsmSimulator('q', [1])
# fsmSimulator('qqqqq', [1])
# fsmSimulator('qqAqqq', [1])

#for regex = r'[a-b][c-d]?
#here accepting states = 2 or 3
edges[1, 'a'] = 2
edges[1, 'b'] = 2
edges[2, 'c'] = 3
edges[2, 'd'] = 3

fsmSimulator("ac", [2,3])
fsmSimulator("aX", [2,3])
fsmSimulator("b", [2,3])