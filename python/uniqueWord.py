sentence  = "sigmas121"
seen = []
notUniqueWord = []
unique = 0

for word in sentence:
    if word not in seen:
        print(word)
        seen.append(word)
        unique += 1
    else:
        unique -= 1
        notUniqueWord.append(word)

nonUnique = len(notUniqueWord)
print(f"your not unique word: {nonUnique}")
print(f"unique word: {unique - nonUnique}") 
        
    
