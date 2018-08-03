
#6.1

def b(z):
  prod = a(z, z)
  print(z, prod)
  return prod

def a(x, y):
  x = x + 1
  return x * y

def c(x, y, z):
  total = x + y + z
  square = b(total) ** 2
  return square

x = 1
y = x + 1

print(c(x, y+3, x+y))

#6.2

def A(m, n):
  if m == 0:
    return n + 1
  elif m > 0 and n == 0:
    return A(m-1, 1)
  elif m > 0 and n > 0:
    return A(m-1, A(m, n-1))
  
A(3,4)


#6.3

def first(word):
  return word[0]

def last(word):
  return word[-1]

def middle(word):
  if len(word) <= 2:
    print('empty string')
  else:
    return word[1:-1]
  
def is_palindrome(word):
  if first(word) == last(word):
    if len(word) > 2:
      word = middle(word)
      return is_palindrome(word)
    return True
  return False

print(is_palindrome('gogog'))
print(is_palindrome("macbook"))
print(is_palindrome("1234321"))

#6.4

def is_power(a, b):
  if a % b == 0:
    return True
  return a % b
  
is_power(6, 4)

#6.5

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)

gcd(24, 36)

