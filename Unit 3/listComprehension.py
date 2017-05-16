list = [1,2,3,4,5,6,7]

evenList = [x for x in list if x %2 == 0 ]

for evenNumber in evenList:
    print(evenNumber)

#Also can be done as
#yield is Generator

def oddOnly(numbers):
    for n in numbers:
        if n % 2 == 1:
            yield n

# for x in oddOnly(list):
#     print(x)

oddList = [x for x in oddOnly(list)]

for oddNumber in oddList:
    print(oddNumber)