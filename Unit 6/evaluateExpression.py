# JS Interpreter , write()

def evalExp(tree, environment):
    expressionType = tree[0]

    if expressionType == "call":
        functionName = tree[1] #myFun in myFun(a, 3+4)
        functionArgs = tree[2] # [a, 3+4] in myFun(a, 3+4)
        functionValue = envLookUp(functionName, environment) #None For write

        # write() is special function that user gets to use but they provide no definition
        # so, we are not going to find it in our environment
        # but Also returns none if the function is just unknown

        if(functionName == "write"):
            # write() should have single argument so we evaluate it
            argValue = evalExpression(functionArgs[0], environment)
            outputSoFar = envLookUp("javascript output", environment)

            envUpdate("javascript output", outputSoFar + str(argValue) , environment)
            return None

        #support for anonymous function
        elif(expressionType == "function"):
            # ("function", ["x","y"], [(return", ("binop", ...)])
            functionParams = tree[1]
            functionBody = tree[2]

            return("function", functionParams, functionBody, environment)