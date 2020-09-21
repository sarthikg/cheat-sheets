#NO REPEATED VALUES         NO ORDER
Creating Sets:
sets = {1, 2, 3, 4, 5, 6}
sets = set(1, 2, 3, 4, 5, 6)

Check element in Set:
el in sets

Adding Element to a set:
sets.add(el)

Removing Element from a set:
sets.remove(el)

Removing Elements without a Error in case of Absence of Element in Set:
sets.discard(el)

Create a copy of Set:
setss = sets.copy()

Delete everything in Set:
sets.clear()

Union for Sets:
setss | sets

Intersection for Sets:
setss & sets

Sets Comprehension:
{x**2 for x in range(10)}