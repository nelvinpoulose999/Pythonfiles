#word count, stop words
stopwords=["the",'where','is','have','with','that','had','of','you','to','and','on','by']

f=open('news','r')
dict={}
for words in f:
    #print(words)
    word=words.rstrip('\n,.,,').split(" ")

    for letters  in word:
        if letters in stopwords:
            pass
        else:
            if letters not in dict:
                dict[letters]=1
            else:
                dict[letters]+=1
print(dict)
print(max(dict, key=dict.get))

