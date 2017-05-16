def myFirstYourSecond(string1, string2):
    spacePos1, spacePos2  = findSpacePos(string1) , findSpacePos(string2)

    substring1 = string1[: spacePos1]
    substring2 = string2[spacePos2+1: ]

    if substring1 in substring2:
        print('True')
    else:
        print('False')

def findSpacePos(string):
    return string.find(' ')

myFirstYourSecond('bell hanks', 'curer bell')
myFirstYourSecond('bell hanks', 'grace hopper')
