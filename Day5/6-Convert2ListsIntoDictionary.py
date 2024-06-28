list1 =  ["HI" , "Lakshita" , "Take Care"]
list2 = [1,2,3]
#Approach 1
'''
Res_Dictionary = {}
for key in list1:
    print(key)
    for value in list2:
        print(value)
        Res_Dictionary[key] = value
        list2.remove(value)
        break

# Printing resultant dictionary
print("Resultant dictionary is : " + str(Res_Dictionary))

'''
#APPROACH 2
'''
Res_Dictionary = {list1[i] : list2[i] for i in range(len(list1))}
print("Resultant dictionary is : " + str(Res_Dictionary))

'''
#using dict() and zip()

'''
Res_Dictionary = dict(zip(list1,list2))
print("Resultant dictionary is : " + str(Res_Dictionary))
The zip() function pairs the elements in the two lists together, and dict() converts the resulting tuples to key-value pairs in a dictionary.
'''
