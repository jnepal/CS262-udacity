

#p is parse tree
def p_exp_call(p):
    'exp : IDENTIFIER LPAREN optargs RPAREN'
    p[0] = ("call", p[1], p[3])

def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ("number", p[1])

def p_optargs(p):
    'optargs: args'
    p[0] = p[1] # the work happens in "args"

def p_optargs_empty(p):
    'optargs: '
    p[0] = [ ] # no arguments return empty list

def p_args(p):
    # myFun(1)  myFun(2,3)
    'args: exp COMMA exp'
    p[0] = [p[1]] + p[3]

def p_args_last(p):
    'args: exp'
    p[0] = [p[1]]

