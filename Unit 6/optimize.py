def optimize(tree): #expression trees only
    #("binop", ("number", "6"), "+", ("number", "1"))
    expressionType = tree[0]
    if expressionType == "binop":
        leftChild = optimize(tree[1]) #to support multiple optimization like 5+(2*0)
        operator = tree[2]
        rightChild = optimize(tree[3]) #to support multiple optimization like 5+(2*0)

        if operator == "*" and rightChild == ("number", "1"): #Form A*1
            return leftChild
        elif operator == "*" and rightChild == ("number", "0"): # A*0
            return ("number", "0")
        elif operator == "+" and rightChild == ("number", "0"): # A+0
            return leftChild

    return tree
