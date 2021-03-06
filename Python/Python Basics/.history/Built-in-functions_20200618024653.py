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
evens = filter(lambda x: x%2 == 0, [1,2,3,4])
print(list(doubles))

# LIST COMPREHENSIONS - Iteratate over a Iterable with a condition
users= ['abc', 'bcd', 'cde', 'ace']
[user.upper() for user in users if user[0] == 'a']

# ANY/ALL - Checks if any value in the list is Truthy / Checks if all values in the list are Truthy
any([0,1,2,3])  -   True
any([False, 0]) -   False
all([1,2,3,4])  -   True
all([0,1,2,3])  -   False

# SORTED - Sorts any iterable and returns the Sorted Iterable, doesnt change the original iterable
sorted(<dictionary>, key=len)               Will Sort this with number of keys in Dictionary
sorted(<dictionary>, key=lambda x: x['key'])    Sort alphabetically with the selected key
sorted(<list>)                              Will Sort the List
sorted(<set>)                               Will sort the Set
# reversed property, values - True/False

# MIN/MAX - Finds min and max value from this values or the iterable
min(1,2,3,4)
min([1,2,3,4])
# has same key property like sorted

# ABS/SUM/ROUND - Returns absolute(converts -ive to +ive), Sums(with an optional start), Rounds off(with optional digits after decimal)
abs(-13.33)         13.33
sum([1,2,3], -6)    0
round(1.2345, 3)    1.234

# ZIP - stitches first element of list 1 with first element of list 2 and so on, till one of them is exhausted and returns a ZIP Object
zip(iter1, iter2, iter3)

# ERRORS - raising errors
raise <error-name>()