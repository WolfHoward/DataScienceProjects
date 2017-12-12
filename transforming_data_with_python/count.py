from read import load_data
from collections import Counter

df = load_data()

words = []
headlines = ''

for item in df.loc[:,'headline']:
    headlines += str(item).lower() + ' '
    
words = headlines.split(" ")

print('100 most common words: ')
print(Counter(words).most_common(100
))


