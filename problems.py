# P1
def word_lengths(phrase):
  return list(map(len,phrase.split()))
  
  
print(word_lengths('How long are the words in this phrase'))


#P2
from functools import reduce
def digits_to_num(digits):
  return reduce(lambda x,y : x*10 + y, digits)
print(digits_to_num([3,4,3,2,1]))

#P3
word_list = ["hi","are","cat","dog","hello"]
def filter_words(word_list, letter):
  return list(filter(lambda x : x[0] == letter,word_list))
print(filter_words(word_list,"h"))

#P4
def concatenate(L1,L2, connector):
  return [f'{x}{connector}{y}' for x,y in zip(L1,L2)]
print(concatenate(["A","B"],["a","b"],"-"))

#P5
l1 = ["a","b","c"]
def d_list(L):
  dict1 = {}
  for i, ele in enumerate(L):
    dict1[ele] = i
  return dict1
print(d_list(l1))

#P6
l1 = [0,2,2,1,5,5,6,10]
def count_match_index(L):
  count = 0
  for i, ele in enumerate(L):
    if i == ele :
      count += 1
  return count
print(count_match_index(l1))
