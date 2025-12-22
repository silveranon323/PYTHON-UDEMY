words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
word_freq={}
for word in words:
    word_freq[word]=word_freq.get(word,0)+1
print(word_freq)