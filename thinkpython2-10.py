

#10.1

def nest_sum(t):
  total = 0
  for i in t:
    total += sum(i)
  return total

  
sl = [[1, 2], [3], [4, 5, 6]]
nest_sum(sl)

#10.2

def cumsum(t):
  total = 0
  res = []
  for i in range(len(t)):
    total = sum(t[:(i+1)])
    res.append(total)
  return res

t = [1, 2, 3]
cumsum(t)

#10.3

def middle(t):
  n = len(t)
  t = t[1:(n-1)]
  return t

t = [1, 2, 3, 4]
middle(t)

#10.4

def chop(t):
  del t[0]
  del t[-1]
  return t

t = [1, 2, 3, 4,]
chop(t)

#10.5

def is_sorted(t):
  n = len(t)
  for i in range(n-1):
    if t[i] > t[i+1]:
      return False
  return True

print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))

#10.6 What is anagram?

def is_anagram(word1, word2):
    """Checks whether two words are anagrams

    word1: string or list
    word2: string or list

    returns: boolean
    """
    return sorted(word1) == sorted(word2)
  
is_anagram('dog', 'ogd')

#10.7

def has_duplicates(t):
  s = list(t)
  s.sort()
  for i in range(len(s) - 1):
    if s[i] == s[i+1]:
      return True
  return False

has_duplicates('tomao')

#10.8

import random

def random_birth(n):
  birth = []
  for i in range(n):
    day = random.randint(1, 365)
    birth.append(day)
  return birth
  
def find_birth(num, simu):
  count = 0
  for s in range(simu):
    stu_birth = random_birth(num)
    stu_birth.sort()
    for j in range(len(stu_birth)-1):
      if stu_birth[j] == stu_birth[j+1]:
        count += 1
  return count

find_birth(23, 10)

#10.9 ~ 10

def make_word_list1():
	t = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

def make_word_list2():
	t = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		t = t + [word]
	return t

import time

start_time = time.time()
t = make_word_list1()
end_time = time.time() - start_time

print(len(t))
print(t[:10])
print(end_time, 'seconds')

start_time2 = time.time()
s = make_word_list2()
end_time2 = time.time() - start_time2

print(len(s))
print(s[:10])
print(end_time2, 'seconds')

def make_word_list():
	word_list = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		word_list.append(word)
	return word_list

def in_bisect(word_list, word):
	if len(word_list) == 0:
		return False
	i = len(word_list) // 2
	if word_list[i] == word:
		return True
	if word_list[i] > word:
		return in_bisect(word_list[:i], word)
	else:
		return in_bisect(word_list[i+1:], word)

def in_bisect_cheat(word_list, word):
	i = bisect.bisect_left(word_list, word)
	if i == len(word_lsit):
		return False
	return word_list[i] == word

#10.11
def find_reverse():
	word_list = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if word == word[::-1]:
			word_list.append(word)
	return word_list

#10.12
def shuffle_word(word1, word2):
        res = []
        for i in range(lne(word1)):
                word = word1[i] + word2[i]
                res.append(word)
        return res

def making_word(word1, word2):
        t = shuffle_word(word1, word2)
        s = ""
        for i in range(len(t)):
                s = s + t[i]
        return s

def interlock_check(word1, word2):
        i_word = making_word(word1, word2)
        fin = open('words.txt')
        for line in fin:
                word = line.strip()
                if i_word == word:
                        return True
        return False


                
