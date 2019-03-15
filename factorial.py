#Returns the factorial of a number

def factorial(x):
  factors = []
  result = 1
  while x > 0:
    factors.append(x)
    x -= 1
  for number in factors:
  	result = result * number
  return result
