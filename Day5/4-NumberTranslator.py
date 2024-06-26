number= input(">") #1234

convertor = {
    "1":"One",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five"
}
output = ""
for value in number:
    output += convertor.get(value,"!") +" "
print(output) 