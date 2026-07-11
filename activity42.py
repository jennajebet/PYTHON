test_dict = {"codingal" : 55, "is" : 67, "best" : 2, "for" : 2, "coding" : 2}

print("the original dictionary:" + str(test_dict))

K = 2

res = 0
for key in test_dict:
    if test_dict[key]==K:
        res = res + 1

print("Frequency of K is:" + str(res))