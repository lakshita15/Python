#for x in y

# List is basically a list of items, a list of numbers, list of names
'''
for item in 'python':
    print(item)
'''
'''
for item in ['lax','1','2','3']:
    print(item)
    '''

'''for item in ['lax','10','20','30']:
    print(item[0]) // this print 0 index of each item,
     o/p =>  l,1,2,3
  '''
'''for item in ['lax','10','20','30']:
    print(item[0]) // this print 0 index of each item,
     o/p =>  l,1,2,3
  '''

#range

"""
for item in range(10):
    print(item) //print 0-9
"""

'''
for item in range(5,10):
    print(item) //print 5-9

'''

'''
for item in range(5,10,2): #2 step
    print(item) #/print 5 7 9
'''

prices = [10,20,30]
total = 0

for i in prices:
    total += i
print(f"total:{total}")