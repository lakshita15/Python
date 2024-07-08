'''
number = int(input("Enter  Number: "))

try:
   for i in range (1,11):
      print(f"{number} * {i} is {number*i} ")
except IndexError:
   print("index error")
except Exception as e:
   print(e)


print(" printed after exception imp line")


'''
'''
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

  '''
'''
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

  '''

# #Finally makes difference in a function
# def func():
#     try:
#         list = [1,2,3,4,5,6]
#         i = int(input("Enter index "))
#         print(list[i])
#         return 1
#     except:
#         print("Some error occured")
#         return 0
    
#     print("IMPORTANT!!!!!!!") #=> This code wont run if not finally and even when no error

# z= func()
# print(z)

# def func():
#     try:
#         list = [1,2,3,4,5,6]
#         i = int(input("Enter index "))
#         print(list[i])
#         return 1
#     except:
#         print("Some error occured")
#         return 0
#     finally:
#         print("IMPORTANT!!!!!!!") #=> This code wont run if not finally and even when no error

# z= func()
# print(z)
#raising custom errors