from environment import envLookUp

# evalExp procedure to interpret javascript arithmetic
# expression. Only handle +,- and numbers for now

# environment is the context. like for knowing the value of x we first need to know in context of the assignment

def evalExp(tree, environment):
    # ("number", "5")
    # ("binop", ("number", "6"), "+", ("number", "7")) binop = binary operator such as +,-,*,/
    nodeType = tree[0]

    if(nodeType == "number"):
        return int(tree[1])
    elif(nodeType == "binop"):
        leftChild = tree[1]
        operator = tree[2]
        rightChild = tree[3]

        leftChildValue  = evalExp(leftChild, environment)
        rightChildValue = evalExp(rightChild, environment)

        if(operator == '+'):
            return leftChildValue + rightChildValue
        elif(operator == '-'):
            return leftChildValue - rightChildValue
        elif(operator == '*'):
            return leftChildValue * rightChildValue
        elif(operator == '/'):
            return leftChildValue / rightChildValue

    elif(nodeType == "identifier"):
        # ("identifier", "x)
        identifierName = tree[1]
        return envLookUp(environment, identifierName)
