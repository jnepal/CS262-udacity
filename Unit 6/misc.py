def interpret(trees):
    globalEnvironment = (None, {"javascript output":""})
    for tree in trees:
        evalElement(tree, globalEnvironment)

    return (globalEnvironment[1])["javascript output"]

# Extending our HTML Grammar
# For handling javascript token when parsing

def p_element_javascript(p):
    'element: JAVASCRIPT'
    p[0] = ('javascript-element', p[1])