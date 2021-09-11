def digits(n):
  # return list of digits of number
  a = []
  while n:
    n, remainder = divmod(n, 10)
    a.append(remainder)
  return a

for i in range (1, 1001):
  s = 0
  l = digits(i)
  for d in l:
    s = s + d ** len(l)

  if i == s:
    print("Narcissistic: {0:5}".format(s))
