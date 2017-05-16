#Map Function
numberList = [1, 2, 3, 4]

def square(x):
    return x*x

squareList = list(map(square, numberList))
# for item in squareList:
#     print(item)

#also can be done as
nextSquareList = list(map(lambda x: x*x, numberList))
for item in nextSquareList:
    print(item)