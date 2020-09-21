
Creating Lists
tasks =["a", "b", 1]
tasks = list(range(1,10))

Find Length
len(tasks)

Accessing Values
var1 = tasks[3]
print(tasks[2])

Check a Value in Lists
"a" in tasks                #True
"something" in tasks        #False

Using FOR Loop
for number in tasks:
    print(number)

Using WHILE Loop
i=0
while i<len(tasks):
    print(tasks[i])
    i+=1

APPEND - add SINGLE item to END of the list
tasks.append("new value")

EXTEND - add ALL values passed to the END of the list
tasks.extend(["1st value", "2nd value", "3rd value"])

INSERT - insert item at a GIVEN Position
tasks.insert(2,"New Value")


CLEAR - remove ALL items from the list
tasks.clear()

POP - remove item at GIVEN Position and RETURNS it
    bydefault-removes last and returns it
tasks.pop(4)

REMOVE - remove FIRST Item from list whose value is x
tasks.remove(x)


INDEX - RETURNS Index of specified Item in the List
tasks.index(item, start, end)

COUNT - RETURNS number of times x appears in List
tasks.count(x)

REVERSE - reverse the elements of the List
tasks.reverse()

SORT - sort the items of list in ASCENDING Order
tasks.sort()

JOIN - joins the items of list with some given string and RETURNS it
'given string'.join(tasks)


SLICING - making new list by Slicing Old one and RETURN it
tasks[start:end:step]

SWAPPING Values
tasks[0] , tasks[1] = tasks[1], tasks[0]

LIST COMPREHENSION - RETURNS the modified terms
[x*10 for x in tasks]
