import evaluateExpression.evalExp as evalExp
from environment import envUpdate
from environment import envLookUp

# Evaluating statements
def evalStatement(tree, environment):
    # ("assign", x, ("number", 3))
    statementType =  tree[0]
    if(statementType == "assign"):
        variableName = tree[1]
        rightChild = tree[2]

        newValueOfVariable = evalExp(rightChild, environment)

        envUpdate(environment, variableName, newValueOfVariable)

    elif(statementType == "if-then-else"):
        # if x < 5 then A;B; else C;D;
        conditionalExpression = tree[1] # x < 5
        thenStatements = tree[2] # A;B;
        elseStatements = tree[3] # C;D;

        if(conditionalExpression):
            evalStatements(thenStatements, environment)
        else:
            evalStatements(elseStatements, environment)

    # Handling Return statements
    elif(statementType == "return"):
        # return "1+2"
        returnExpression  = tree[1]
        returnValue = evalExp(returnExpression, environment)
        raise Exception(returnValue)

    #Handling Function calls
    elif(statementType == "call"):
        #("call", "sqrt", [("number", "2")])
        #("call", "pow", [("number", "2"),("number", "3")]
        functionName = tree[1] # "pow"
        functionArgs = tree[2] # functions arguments [("number", "2")("number", "3")]

        # one function may mean different thing for different context
        functionValue = envLookUp(functionName, environment)
        if functionValue == "function":
            #("function", params, body, environment)
            functionParams = functionValue[1] #for pow(x,y) ["x","y"] is parameter
            functionBody = functionValue[2]
            functionEnvironment = functionValue[3]

            #check whether the parameter and arguments len are same
            # we cannot pass three arguments like pow(x, y, z) to function pow(x, y) which have only two parameters x and y
            if(len(functionArgs) != len(functionParams)):
                print("ERROR: Wrong number of arguments")
            else:
                # Make a new Environment Frame
                newEnvironment = (functionEnvironment, {})
                for i in range(len(functionArgs)):
                    argumentValue = evalExp(functionArgs[i], environment)
                    #Binding argument to the params
                    (newEnvironment[1])[functionParams[i]] = argumentValue

                # Evaluate the body in the new frame
                try:
                    evalStatements(functionBody, newEnvironment)
                except Exception as returnValue:
                    return returnValue
        else:
            print('ERROR: Call to a non function')




