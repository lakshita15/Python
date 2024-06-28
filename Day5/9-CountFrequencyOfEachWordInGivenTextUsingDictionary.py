user_input = input("enter a Sentence :- ")
word_list = user_input.split(" ")

word_freq = {}
for word in word_list:
    
    word_freq[word] = word_freq.get(word,0)+1

print(word_freq)
