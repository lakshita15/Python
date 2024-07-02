
def emoji_convertor(Phrase):
    splitted_phrase = Phrase.split(" ")
    #print(splitted_phrase)
    emoji_book={
        ":)":"😃",
        ":(":"😫"
    }
    for each_character in splitted_phrase:
         new_Phrase = emoji_book.get(each_character,each_character)+" "
    return new_Phrase

Phrase = input("")
print(emoji_convertor(Phrase))