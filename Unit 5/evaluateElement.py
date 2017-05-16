#Function Definitions
def evalElement(tree, environment):
    #("function",sum, [("number", "x"),("number", "y")], ["return", [("number", "x"),("number", "y")]] ) #function sum(x, y){ return x+y; }
    elementType = tree[0]
    if elementType == "function":
        functionName = tree[1]
        functionParams = tree[2]
        functionBody = tree[3]

        functionValue = ("function", functionParams, functionBody, environment)

        addToEnvironment(env, functionName, functionValue)