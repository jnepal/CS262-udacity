# HTML Interpreter to handle javascript elements

def interpret(trees):
    for tree in trees:
        treeType = tree[0]
        if treeType == "word-element":
            graphics.word(tree[1])
        elif treeType = "javascript-element":
            jsText = tree[1]
            #lex is the module to do lexical analysis
            jsLexer = lex.lex(module = jstokens)
            #yacc is module to do the parsing
            jsParser = yacc.yacc(module = jsgrammar)
            # yacc = Yet Another Compiler-Compiler

            jsTree = jsParser.parse(jsText, lexer = jsLexer)
            #jsTree is a parse tree for javascript

            result = jsInterpreter.interpret(jsTree)
            graphics.word(result)
