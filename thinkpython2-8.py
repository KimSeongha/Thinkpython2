
#8.2

def find_st(word, st):
  count = 0
  for letters in word:
    if letters == st:
      count += 1
  
  return count

    
find_st('banana', 'a')

#8.3

def is_palindrome(word):
  if word[::-1] == word:
    return True
  else:
    return False
  
  
is_palindrome('tomato')

#8.4

def any_lowercase1(s):
  for c in s:
    if c.islower() == False:
      return False
  return True
    
def any_lowercase2(s):
  for c in s:
    if c.islower():
      return 'True'
    else:
      return 'False'
    
def any_lowercase3(s):
  for c in s:
    flag = c.islower()
    if flag == False:
      return False
  return True

def any_lowercase4(s):
  flag = True
  for c in s:
    flag = flag and c.islower()
  return flag

def any_lowercase5(s):
  for c in s:
    if not c.islower():
      return False
  return True


any_lowercase5('ddddddd')

#8.5

#A : 65 Z : 90
#a : 97 z : 122

def rotate_word(word, n):
  for i in word:
    if ord(i) == 90 or ord(i) == 122:
      j = ord(i) - 26 + n
      if j < 65:
        j = j + 27 + n
        print(chr(j), end = "")
      elif 90 < j < 97:
        j = j + 27 +n 
        print(chr(j), end = "")
    else:  
      j = ord(i) + n
      if j < 65:
        j = j + 27 + n
        print(chr(j), end = "")
      elif 90 < j < 97:
        j = j + 27 + n
        print(chr(j), end = "")
      else:
        print(chr(j), end = "")
    
rotate_word('abcdefghijklmnopqrstuvwxyz', -1)
