Phrase = input("")
splitted_phrase = Phrase.split(" ")
#print(splitted_phrase)
 
emoji_book={
    ":)":"😃",
    ":(":"😫"
}
new_Phrase = " "
for each_character in splitted_phrase:
    new_Phrase+= emoji_book.get(each_character,each_character)+" "

print(new_Phrase)