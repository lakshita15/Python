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