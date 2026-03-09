#dictionarys

mydict = {
    "name": ["red" , "green", "black"],
    "age": [1, 2, 3] 
}

print (mydict)
print (mydict["name"])

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 

# accesing 

thisdict = {
  "car": "BMW",
  "bike": "KTM",
  "scooty": "TVS"
}
x = thisdict.keys()
print (x)
thisdict["SUV"] = "MG"
print (x)
x = thisdict.values()
thisdict["bike"] = "JAVA"
print (x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
thisdict = {
  "car": "BMW",
  "bike": "KTM",
  "scooty": "TVS"
}
if "car" in thisdict:
  print ("yes")
else:
  print ("No")
if "KTM" in thisdict:
  print ("yes")
else:
  print ("No")

#changing

thisdict = {
  "car": "BMW",
  "bike": "KTM",
  "scooty": "TVS"
}
thisdict["bike"] = "JAVA"
print (thisdict)
thisdict.update({"scooty": "FZ"})
print (thisdict)

#remove

thisdict = {
  "car": "BMW",
  "bike": "KTM",
  "scooty": "TVS"
}
thisdict.pop('car')
print (thisdict)

thisdict = {
  "car": "BMW",
  "bike": "KTM",
  "scooty": "TVS"
}
thisdict.popitem()
print (thisdict)

thisdict = {
  "car": "BMW",
  "bike": "KTM",
  "scooty": "TVS"
}
del thisdict["bike"]
print (thisdict)

thisdict = {
  "car": "BMW",
  "bike": "KTM",
  "scooty": "TVS"
}
thisdict.clear()
print (thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)

#loops

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
