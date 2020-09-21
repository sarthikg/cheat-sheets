# LAMBDAS - Un-named / Anonymous Functions are Lambdas
# Normal Function
def add(num1, num2):
    return num1 + num2
# Lambda Function
lambda num1, num2: num1+num2

# MAP - Interates over Iterable with the Function and returns a Map Object
doubles = map(lambda x: x*2, [2,4,6,8])
print(list(doubles))

# FILTER - Iterated over Iterable with the Function and returns a Filter Object with all the True returns

