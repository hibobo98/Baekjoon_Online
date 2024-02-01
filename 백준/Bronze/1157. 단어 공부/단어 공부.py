word = input() # AaB
word = word.lower() # aab
list_word = list(set(word.lower())) # ab

list_count = []
for w in list_word: 
    count = word.count(w)
    list_count.append(count)
    
if list_count.count(max(list_count)) >= 2:
    print("?")
else:
    idx = list_count.index(max(list_count))
    print(list_word[idx].upper())