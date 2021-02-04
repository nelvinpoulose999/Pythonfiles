# print pattern
# 1
# 12
# 123
# 1234
for i in range(1,5):    # row elements

    for j in range(1,i+1):  # column elements
        print(j,end=' ')
    print()