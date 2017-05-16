import ply.lex as lex

tokens = (
    'LANGLE', # <
    'LANGLESLASH', # </
    'RANGLE', # >
    'EQUAL', # =
    'STRING', # "hello"
    'WORD', # welcome!
)

#for handline comments
#if processing htmlcomment can't do anything other i.e exclusive
states = (
    ('htmlcomment', 'exclusive'),
)

t_ignore = ' ' #ignore whitespaces



#could pass the comment like this
# def t_comments(token):
#     r'(?:<!--)[a-zA-z0-9 ]*(?:-->)'
#     pass

#preffered method for handling comment
def t_htmlcomment(token):
    r'<!--'
    token.lexer.begin('htmlcomment')

def t_htmlcomment_end(token):
    r'-->'
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')

def t_htmlcomment_error(token):
    token.lexer.skip(1) #equivalent to pass

def t_newline(token):
    r'\n'
    token.lexer.lineno +=1
    pass

def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"[^"]*"'
    token.value = token.value[1:-1] #shredding off "" at beginning and at last
    return token

def t_WORD(token):
    r'[^ <>\n]+'
    return token


# webpage = '"This" is <b>my</b> webpage!'
# webpage = """Tricky "string" <i>output</i>!"""
# webpage = """Line1
#             Line2
#             """
# webpage = """This is
#             <b>webpage!"""
# webpage = 'This is <b>my</b> webpage. <!--Title of webpage-->'
webpage = "hello <!--comment --> all"
htmlLexer = lex.lex()
htmlLexer.input(webpage)

for token in htmlLexer:
    print(token)