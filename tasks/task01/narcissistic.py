base = 3

def digits(n):
  # return list of digits of number
  a = []
  if n < 10:
    a = [n]
  else:
    while n:
      n, remainder = divmod(n, 10)
      a.append(remainder)
  return a

for i in range (1, 1001):
  s = 0
  for d in digits(i):
    s = s + d ** base

  if i == s:
    print('Narcissistic: ', i,)
