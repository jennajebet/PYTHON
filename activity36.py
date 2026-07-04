def match_word(words):
    ctr=0
    Ist=[]
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            Ist.append(word)

    print ("List of words with first and last character same\n",Ist)
    return ctr

count = match_word(["abc", "cfc", "xyz", "aba", "1221"])
print("Number of words having first and last character same:", count)