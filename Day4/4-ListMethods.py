names = ['lakshita','rachit','anahita','vinkan','ajay',"lakshita"]
'''
names.insert(3,'shaan')
print(names) #'lakshita', 'rachit', 'anahita', 'shaan', 'vinkan', 'ajay']

names.append(20)
print(names)

names.remove(20)
print(names)

names.pop() #end of list se pop
print(names)

print(names.index("ajay")) #4 give an error

print("lakshita" in names) #true just say true or false

print(names.count("lakshita")) #tell me occurence of lakshita in names list

# sort in ascending
names.sort()
print(names)

# sort in ascending
names.sort()
names.reverse()
print(names)

copy the original list 
names2 = names.copy()
'''