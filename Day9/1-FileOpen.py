# f=open("F1.txt" , 'wt') #=>creates f1.txt in python folder
# f.close()

'''
f=open("F1.txt" , 'r') #=>creates o.UnsupportedOperation: not writable error as read format cannot be written
f1 = f.write("hi")
f.close()
'''
with open('myfile.txt','a') as f:
    f.write("hello")

with open('myfile.txt','r') as f:
    f.read()

