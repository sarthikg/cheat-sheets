DECLARATION
cat = {"name":"blue", "age":3.5, "isCute":True}
cat = dict(name="kitty")


ACCESSING
cat["name"]

JUST KEYS
cat.keys()

JUST VALUES
cat.values()
    
BOTH
cat.items()

CHECK EXISTENCE
"name" in cat           #True   #Checks only KEYS
"blue" in cat.values    #True   #Checks only VALUES

CLEAR - clears all keys and Values

COPY - makes exact same copy
c = cat.copy()

GET - to return value for a particular key (doesnt throw an error)
cat.get("name")
ū
FROMKEYS - to replace values of all keys to a common value
c = {}.fromkeys(cats, 0)

POP - to remove a particular key value pair and RETURNS the Value
cat.pop("name")

POPITEM - remove random key value pair and RETURNS it
cat.popitem()

UPDATE - updates or adds key value pairs from one dic to another
cats = {"height": 2.3}
cats.update(cat)
