#function for finding sum
def sum(a, b):
    return a+b

print(sum(2,3))

#could be also expressed as lambda function
#similar to analogy of anonymous function in functional programming

sumVariable = lambda a,b: a+b
anotherVariable = sumVariable

print(sumVariable(2, 3))
print(anotherVariable(2,5))

