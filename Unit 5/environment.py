def envLookUp(variableName, environment):
    # environment = (parent, dictionary)
    # environment = (None, dictionary) for global environment
    if variableName in environment[1]: #check for the variable in current environment if found return the value
        return (environment[1])[variableName]
    elif environment[0] == None: # check if the current enviornment is the global if it is and variable is not found return None
        return None
    else:
        # Search in parent environment for the variable name
        return envLookUp(variableName,environment[0])

def envUpdate(variableName, variableValue, environment):
    # environment = (parent, dictionary)
    # environment = (None, dictionary) for global environment
    if variableName in environment[1]: #check for the variable in current environment if found return the update the value
        (environment[1])[variableName] = variableValue
    elif(environment[0] != None):
        # update the variable value of parent environment
        envUpdate(variableName, variableValue, environment[0])


globalEnvironment = (None, {"x": 11, "y": 22})
newEnvironment = (globalEnvironment, {"x": 33, "z": 44})
print(envLookUp("x", newEnvironment))
print(envLookUp("y", newEnvironment))

envUpdate("x", 66, newEnvironment)
print(envLookUp("x", newEnvironment))
print(envLookUp("x", globalEnvironment))