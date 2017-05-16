import ply.lex as lex

def t_javascript(token):
    # Escaping the characters is optional
    r'\<script\ type=\"text\/javascript\"\>'
    token.lexer.codeStart = token.lexer.lexpos #codeStart is variable we defined to store the lexical position
    token.lexer.begin("javascript")

def t_javascript_end(token):
    r'\<\/script\>' #</script>
    #javascript body between <script> and </script>
    #we substracted 9 characters as </script> is 9 characters long
    #token.lex.lexdata gives entire string from lexer
    token.value = token.lexer.lexdata[token.lexer.codeStart: token.lexer.lexpos-9]
    token.type = 'JAVASCRIPT'
    #For correct line position we also count line breaks
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')
    return token

webpage = '<script type="text/javascript">document.write("Hello World")</script>'
jsLexer = lex.lex(module= jstokens)
jsLexer.input(webpage)