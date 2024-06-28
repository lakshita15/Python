'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

It is defined by {}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
'''

customer = {
    "name" :'Lakshita',
    "Age":30,
    "phone":"67899292",
    "is_verified": True
}

customer["birthdate"] = "15 july 2001"
print(customer)
# print(customer["number"]) 
'''
 print(customer["number"])
          ~~~~~~~~^^^^^^^^^^
KeyError: 'number'
'''
print(customer.get("name")) 

#DICTIONARY COMPREHENSIONS

#{key: value for (key, value) in iterable}. 
