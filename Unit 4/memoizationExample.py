
import time
#Normal Using Recursive definition
def fibonacci(number):
    if(number <= 2):
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)

#Optimising the time using Memoization technique


chart = {} #to hold fibonacci values already calculate to reduce the recalculation

def fibo(n):
    if(n in chart):
        return chart[n]
    elif(n <= 2):
        chart[n] = 1
    else:
        chart[n] = fibo(n-1) + fibo(n-2)

    return chart[n]

def timeExecution(statement):
    startTime = time.clock()
    eval(statement)
    runTime = time.clock()-startTime


    return runTime

print(timeExecution('fibonacci(25)'))
print(timeExecution('fibo(25)'))
