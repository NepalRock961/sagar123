words = ['this', 'is', 'just', 'a','test', 'example']
capitalized_word = [x.capitalize() for x in words]

print('Words: ',words)
print('Capitalized Words: ',capitalized_word)

word = ['hello', 'this', 'is', 'sagar', 'aryal', 'a']
short_words = [x for x in word if len(x) <=3]
other_words = [x for x in word if x not in short_words]
words_with_e = [x for x in word if x.count('e') >=1]
print('Words: ',word)
print('Short Word: ',short_words)
print('Long Word: ',other_words)
print('Words with e: ',words_with_e)