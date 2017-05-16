import graphics

def interpret(trees): # Hello, Friend
    for tree in trees: # Hello
        # ("word-element", "Hello")
        nodeType = tree[0] # word-element
        if nodeType == "word-element":
            graphics.word(tree[1])
        elif nodeType == "tag-element":
            # <b> Strong Text ! </b>
            tagName = tree[1]
            tagArgs = tree[2] # <a href="">Some Text</a> href="" is tagArgs
            subTrees = tree[3] # Strong Text!
            closeTagName = tree[4]

            #checking whether opening tag and close tag elements matches or not
            if(tagName != closeTagName):
                graphics.warning("Tags don't match", tagName, closeTagName)
            else:
                graphics.begintag(tagName, tagArgs)
                interpret(subTrees)
                graphics.endtag()